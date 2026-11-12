#!/usr/bin/env python3
"""Verify the eight PDFs against the saved pre-refinement PDFs.

Only the two placements specified in MARGIN_PLACEMENTS.tsv are permitted to
move, once in each applicable PDF. All other extracted text and page geometry
must compare exactly in the installed PyMuPDF runtime.
"""
from __future__ import annotations

import argparse
import csv
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

import fitz


ROOT = Path(__file__).resolve().parents[3]
BOOKS = (
    ("FR", "DER_FR_diplomatique", 615),
    ("FR", "DER_FR_corrige_apparat", 622),
    ("FR", "DER_FR_texte_de_lecture", 603),
    ("FR", "DER_FR_annotated_master", 615),
    ("EN", "DER_EN_diplomatic", 438),
    ("EN", "DER_EN_corrected_apparatus", 448),
    ("EN", "DER_EN_reading", 433),
    ("EN", "DER_EN_annotated_master", 438),
)
# The 68 reader samples recorded in PDF_VISUAL_QA.md. No other pages are
# rasterized by this comparison; the eight moved-label pages are separate QA.
VISUAL_SAMPLES = {
    "DER_FR_diplomatique": [1, 2, 3, 35, 191, 320, 340, 580, 915],
    "DER_FR_corrige_apparat": [83, 115, 253, 344, 928, 939, 1050, 1082],
    "DER_FR_texte_de_lecture": [3, 81, 86, 113, 245, 335, 555, 752, 899],
    "DER_FR_annotated_master": [],
    "DER_EN_diplomatic": [1, 2, 3, 37, 190, 230, 319, 338, 915],
    "DER_EN_corrected_apparatus": [2, 3, 88, 116, 235, 253, 325, 441, 934, 942, 949, 959, 960, 961, 985, 1030, 1061],
    "DER_EN_reading": [2, 3, 85, 103, 111, 112, 244, 727, 728, 729, 753, 769, 788, 793, 880, 902],
    "DER_EN_annotated_master": [],
}
RASTER_SCALE = 1.45
TARGETS = {
    "FR": {
        "id": "BUILD-MARGIN-FR-XV-58",
        "unit": "Der-ChXV-05-11-10/Der-ChXV-05-11-10_p056-060.tex",
        "command": "printedpage", "argument": "58", "shift_tex_pt": 6.0,
        "chapter": "Chapitre XV", "trace_text": "p.58",
    },
    "EN": {
        "id": "BUILD-MARGIN-EN-XIIb-152",
        "unit": "Der-ChXIIb-012/Der-ChXIIb-012_p061-065.tex",
        "command": "msp", "argument": "page 152", "shift_tex_pt": 20.0,
        "chapter": "Chapter XII, 5", "trace_text": "[page152]",
    },
}
# A TeX point is 1/72.27 inch; PDF coordinates use 1/72 inch. Only the
# translated label may have this small position-serialization allowance.
PDF_POINTS_PER_TEX_POINT = 72.0 / 72.27
LABEL_TRANSLATION_TOLERANCE_PDF_PT = 0.002
COMPONENTS = ("text", "page_boxes", "text_spans", "vector_drawings",
              "painted_boxes", "images", "links", "annotations")


def relative(path: Path) -> str:
    """Report workspace-relative paths only."""
    return path.resolve().relative_to(ROOT).as_posix()


def digest_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical(value):
    if isinstance(value, dict):
        return {str(k): canonical(v) for k, v in sorted(value.items())}
    if isinstance(value, (tuple, list)):
        return [canonical(v) for v in value]
    if isinstance(value, (fitz.Point, fitz.Rect, fitz.Quad, fitz.Matrix)):
        return [canonical(v) for v in value]
    if isinstance(value, bytes):
        return {"bytes_sha256": hashlib.sha256(value).hexdigest(), "length": len(value)}
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    raise TypeError(f"Unsupported PDF geometry value: {type(value).__name__}")


def encoded(value) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def feed(h, value) -> None:
    data = encoded(value)
    feed_encoded(h, data)


def feed_encoded(h, data) -> None:
    h.update(len(data).to_bytes(8, "big"))
    h.update(data)


def trace_text(span) -> str:
    return "".join(chr(char[0]) for char in span["chars"])


def page_state(page) -> dict:
    boxes = {name: canonical(getattr(page, name)) for name in
             ("mediabox", "cropbox", "bleedbox", "trimbox", "artbox", "rect",
              "rotation", "transformation_matrix", "rotation_matrix", "derotation_matrix")}
    links = [{k: v for k, v in link.items() if k not in ("xref", "id")}
             for link in page.get_links()]
    annotations = []
    for annot in page.annots() or ():
        annotations.append({
            "type": annot.type, "rect": annot.rect, "flags": annot.flags,
            "colors": annot.colors, "border": annot.border,
            "opacity": annot.opacity, "vertices": annot.vertices,
            "content": annot.info.get("content", ""),
            "title": annot.info.get("title", ""),
            "subject": annot.info.get("subject", ""),
        })
    return {
        "text": page.get_text("text", sort=False),
        "page_boxes": boxes,
        "text_spans": canonical(page.get_texttrace()),
        "vector_drawings": canonical(page.get_drawings(extended=True)),
        "painted_boxes": canonical(page.get_bboxlog(layers=True)),
        "images": canonical(page.get_image_info(hashes=True)),
        "links": canonical(links), "annotations": canonical(annotations),
    }


def rendered_pixels(page):
    pixmap = page.get_pixmap(matrix=fitz.Matrix(RASTER_SCALE, RASTER_SCALE),
                            colorspace=fitz.csRGB, alpha=False, annots=True)
    pixels = pixmap.samples
    return {
        "width": pixmap.width, "height": pixmap.height, "stride": pixmap.stride,
        "channels": pixmap.n, "alpha": pixmap.alpha,
        "pixel_bytes": len(pixels), "pixel_sha256": hashlib.sha256(pixels).hexdigest(),
    }


def translation(before, after, expected_dx):
    """Only x coordinates may change. y and all nongeometric data stay exact."""
    errors, deltas = [], []

    def point(a, b, label):
        if len(a) != 2 or len(b) != 2:
            errors.append(label + ": invalid point")
            return
        if a[1] != b[1]:
            errors.append(label + ": vertical position changed")
        dx = b[0] - a[0]
        deltas.append(dx)
        if abs(dx - expected_dx) > LABEL_TRANSLATION_TOLERANCE_PDF_PT:
            errors.append(label + ": unexpected horizontal displacement")

    def rect(a, b, label):
        if len(a) != 4 or len(b) != 4:
            errors.append(label + ": invalid rectangle")
            return
        point(a[:2], b[:2], label + ": top-left")
        point(a[2:], b[2:], label + ": bottom-right")

    if {k: v for k, v in before.items() if k not in ("bbox", "chars")} != {
        k: v for k, v in after.items() if k not in ("bbox", "chars")
    }:
        errors.append("label font, paint, sequence, or other span attributes changed")
    rect(before["bbox"], after["bbox"], "span bbox")
    if len(before["chars"]) != len(after["chars"]):
        errors.append("label glyph count changed")
    else:
        for index, (a, b) in enumerate(zip(before["chars"], after["chars"])):
            if a[:2] != b[:2]:
                errors.append(f"glyph {index}: Unicode or glyph identifier changed")
            point(a[2], b[2], f"glyph {index} origin")
            rect(a[3], b[3], f"glyph {index} bbox")
    return errors, deltas


def painted_translation(before, after, expected_dx, shared_text_span_count=1):
    if len(before) != len(after) or before[0] != after[0] or before[2:] != after[2:]:
        return ["painted label operation type or layer changed"]
    a, b = before[1], after[1]
    if a[1] != b[1] or a[3] != b[3]:
        return ["painted label vertical position changed"]
    # MuPDF may group a label and unchanged body spans in one fill-text
    # operation. The global span comparison independently requires all those
    # other spans to be exactly equal. Its aggregate bbox then keeps an edge
    # fixed when that edge is set by the unchanged text. Only the edge set by
    # the moved label translates. No other paint operation gets this allowance.
    for i in (0, 2):
        dx = b[i] - a[i]
        translated = abs(dx - expected_dx) <= LABEL_TRANSLATION_TOLERANCE_PDF_PT
        unchanged_shared_edge = shared_text_span_count > 1 and dx == 0
        if not (translated or unchanged_shared_edge):
            return ["painted label-group horizontal boundary change is unexpected"]
    if a == b:
        return ["expected the target label's painted bbox to change"]
    return []


def compare_book(args):
    language, stem, expected_page, baseline, output_root = args
    baseline = Path(baseline)
    output_root = Path(output_root)
    old_path = baseline / (stem + ".pdf")
    new_path = output_root / language / (stem + ".pdf")
    old_record_path = baseline / (stem + ".json")
    new_record_path = output_root / "records/build" / (stem + ".json")
    old_record = json.loads(old_record_path.read_text())
    new_record = json.loads(new_record_path.read_text())
    old_sha, new_sha = digest_file(old_path), digest_file(new_path)
    result = {
        "book": stem, "language": language, "status": "FAIL",
        "before": {"file": relative(old_path), "sha256": old_sha,
                   "pdf_bytes": old_path.stat().st_size,
                   "source_tex_sha256": old_record.get("source_tex_sha256"),
                   "build_record": relative(old_record_path),
                   "build_record_sha256": digest_file(old_record_path)},
        "after": {"file": relative(new_path), "sha256": new_sha,
                  "pdf_bytes": new_path.stat().st_size,
                  "build_record": relative(new_record_path),
                  "build_record_sha256": digest_file(new_record_path),
                  "source_tex_sha256": digest_file(new_path.with_suffix(".tex"))},
        "unexpected_differences": [],
    }
    failures = result["unexpected_differences"]
    if old_sha != old_record.get("pdf_sha256"):
        failures.append({"component": "input_identity", "reason": "baseline PDF/build record mismatch"})
    if new_sha != new_record.get("pdf_sha256"):
        failures.append({"component": "input_identity", "reason": "final PDF/build record mismatch"})
    if result["after"]["source_tex_sha256"] != new_record.get("source_tex_sha256"):
        failures.append({"component": "input_identity", "reason": "final source/build record mismatch"})
    if failures:
        return result

    rule = TARGETS[language]
    expected_dx = rule["shift_tex_pt"] * PDF_POINTS_PER_TEX_POINT
    old_doc, new_doc = fitz.open(old_path), fitz.open(new_path)
    result["before"]["pages"] = len(old_doc)
    result["after"]["pages"] = len(new_doc)
    if len(old_doc) != len(new_doc):
        failures.append({"component": "page_count", "reason": "page count changed"})
        return result

    hashes = {version: {name: hashlib.sha256() for name in COMPONENTS}
              for version in ("before", "after", "after_with_permitted_label_restored")}
    changed_pages, target_records, raster_samples = [], [], []
    counts = {"pages": len(old_doc), "text_spans": 0, "glyphs": 0,
              "vector_drawing_records": 0, "painted_operations": 0, "image_occurrences": 0}
    exact_pages = 0

    def fail(page, component, reason, **details):
        if len(failures) < 100:
            failures.append({"physical_page": page, "component": component,
                             "reason": reason, **details})

    for index, (old_page, new_page) in enumerate(zip(old_doc, new_doc)):
        physical_page = index + 1
        before, after = page_state(old_page), page_state(new_page)
        restored = dict(after)
        counts["text_spans"] += len(before["text_spans"])
        counts["glyphs"] += sum(len(s["chars"]) for s in before["text_spans"])
        counts["vector_drawing_records"] += len(before["vector_drawings"])
        counts["painted_operations"] += len(before["painted_boxes"])
        counts["image_occurrences"] += len(before["images"])
        differing_components = [name for name in COMPONENTS if before[name] != after[name]]
        if differing_components:
            changed_pages.append({"physical_page": physical_page,
                                  "components": differing_components})
        else:
            exact_pages += 1

        for name in COMPONENTS:
            if name not in ("text_spans", "painted_boxes") and before[name] != after[name]:
                fail(physical_page, name, "non-permitted content or geometry changed")

        heading = before["text"].splitlines()[0] if before["text"].splitlines() else ""
        targets = [i for i, span in enumerate(before["text_spans"])
                   if heading == rule["chapter"]
                   and trace_text(span).replace(" ", "") == rule["trace_text"]
                   and span["bbox"][0] > old_page.rect.width * 0.8]
        if len(targets) > 1:
            fail(physical_page, "target", "more than one target span on page")
        target_index = targets[0] if len(targets) == 1 else None
        if target_index is not None and physical_page != expected_page:
            fail(physical_page, "target", "target is on an unexpected physical page")

        if len(before["text_spans"]) != len(after["text_spans"]):
            fail(physical_page, "text_spans", "span count changed")
            span_diffs = []
        else:
            span_diffs = [i for i, (a, b) in enumerate(zip(before["text_spans"], after["text_spans"])) if a != b]
            for i in span_diffs:
                if i != target_index:
                    fail(physical_page, "text_spans", "non-target span changed", span_index=i)

        if len(before["painted_boxes"]) != len(after["painted_boxes"]):
            fail(physical_page, "painted_boxes", "painted-operation count changed")
            paint_diffs = []
        else:
            paint_diffs = [i for i, (a, b) in enumerate(zip(before["painted_boxes"], after["painted_boxes"])) if a != b]

        allowed_paint = None
        if target_index is not None and len(before["text_spans"]) == len(after["text_spans"]):
            a, b = before["text_spans"][target_index], after["text_spans"][target_index]
            label_errors, deltas = translation(a, b, expected_dx)
            allowed_paint = a["seqno"]
            shared_text_span_count = sum(s["seqno"] == allowed_paint for s in before["text_spans"])
            if allowed_paint >= len(before["painted_boxes"]) or allowed_paint >= len(after["painted_boxes"]):
                label_errors.append("label paint-sequence index is outside bbox log")
            else:
                label_errors.extend(painted_translation(before["painted_boxes"][allowed_paint],
                                                        after["painted_boxes"][allowed_paint], expected_dx,
                                                        shared_text_span_count))
            if span_diffs != [target_index]:
                label_errors.append("expected exactly the target span to move on this page")
            if paint_diffs != [allowed_paint]:
                label_errors.append("expected exactly the target painted bbox to move on this page")
            for error in label_errors:
                fail(physical_page, "target", error)
            target_records.append({
                "rule_id": rule["id"], "unit": rule["unit"],
                "command": rule["command"], "argument": rule["argument"],
                "physical_page": physical_page, "span_index": target_index,
                "paint_sequence_index": allowed_paint, "trace_text": trace_text(a),
                "text_spans_in_same_paint_operation": shared_text_span_count,
                "painted_operation_bbox_before": before["painted_boxes"][allowed_paint][1],
                "painted_operation_bbox_after": after["painted_boxes"][allowed_paint][1],
                "font": a["font"], "font_size_pdf_pt": a["size"],
                "before_bbox": a["bbox"], "after_bbox": b["bbox"],
                "expected_shift_tex_pt": rule["shift_tex_pt"],
                "expected_shift_pdf_pt": expected_dx,
                "observed_min_dx_pdf_pt": min(deltas) if deltas else None,
                "observed_max_dx_pdf_pt": max(deltas) if deltas else None,
                "vertical_coordinates_exactly_unchanged": all(ca[2][1] == cb[2][1]
                    and ca[3][1] == cb[3][1] and ca[3][3] == cb[3][3]
                    for ca, cb in zip(a["chars"], b["chars"])),
                "status": "PASS" if not label_errors else "FAIL",
            })
            if not label_errors:
                restored["text_spans"] = list(after["text_spans"])
                restored["text_spans"][target_index] = a
                restored["painted_boxes"] = list(after["painted_boxes"])
                restored["painted_boxes"][allowed_paint] = before["painted_boxes"][allowed_paint]
        for i in paint_diffs:
            if i != allowed_paint:
                fail(physical_page, "painted_boxes", "non-target painted operation changed", operation_index=i)

        for name in COMPONENTS:
            before_bytes = encoded(before[name])
            after_bytes = before_bytes if name not in differing_components else encoded(after[name])
            restored_bytes = (before_bytes if restored[name] == before[name] else
                              after_bytes if restored[name] == after[name] else encoded(restored[name]))
            feed_encoded(hashes["before"][name], before_bytes)
            feed_encoded(hashes["after"][name], after_bytes)
            feed_encoded(hashes["after_with_permitted_label_restored"][name], restored_bytes)
        if physical_page in VISUAL_SAMPLES[stem]:
            before_pixels, after_pixels = rendered_pixels(old_page), rendered_pixels(new_page)
            same_pixels = before_pixels == after_pixels
            raster_samples.append({"physical_page": physical_page,
                                   "scale": RASTER_SCALE, "colorspace": "RGB", "alpha": False,
                                   "before": before_pixels, "after": after_pixels,
                                   "exactly_equal": same_pixels})
            if not same_pixels:
                fail(physical_page, "reviewed_sample_pixels", "previously reviewed page pixels changed")

    if len(target_records) != 1:
        failures.append({"component": "target", "reason": "expected exactly one target label per PDF",
                         "observed": len(target_records)})
    if len(changed_pages) != 1 or changed_pages[0]["physical_page"] != expected_page:
        failures.append({"component": "changed_pages", "reason": "expected only the specified label page to change"})
    result["counts"] = counts
    result["exactly_unchanged_pages"] = exact_pages
    result["changed_pages"] = changed_pages
    result["targets"] = target_records
    result["reviewed_sample_pixels"] = raster_samples
    if len(raster_samples) != len(VISUAL_SAMPLES[stem]):
        failures.append({"component": "reviewed_sample_pixels", "reason": "reviewed sample count differs from specification"})
    result["component_sha256"] = {version: {name: h.hexdigest() for name, h in values.items()}
                                  for version, values in hashes.items()}
    result["all_components_equal_after_restoring_only_permitted_label"] = (
        result["component_sha256"]["before"] ==
        result["component_sha256"]["after_with_permitted_label_restored"])
    if not result["all_components_equal_after_restoring_only_permitted_label"]:
        failures.append({"component": "normalized_hashes", "reason": "content remains different after permitted label restoration"})
    # Detect accidental replacement of a PDF while this process was reading it.
    if digest_file(old_path) != old_sha or digest_file(new_path) != new_sha:
        failures.append({"component": "input_identity", "reason": "PDF changed during comparison"})
    result["status"] = "PASS" if not failures else "FAIL"
    old_doc.close()
    new_doc.close()
    return result


def markdown(report):
    lines = ["# Margin refinement comparison", "", f"**Result: {report['status']}**.", "",
             "The comparison covers every physical page of the eight final PDFs and their saved pre-refinement versions. It permits one specified margin-label translation per PDF. All other compared values must be exactly equal; no numerical tolerance is applied to non-target content or geometry.", "",
             f"Runtime: Python {report['python_version']}; PyMuPDF {report['pymupdf_version']}. Completed: {report['completed_utc']}.", "",
             "## Scope", "",
             "The compared values are unsorted extracted page text; page, crop, trim, bleed, and art boxes and page transforms; every text span's font, paint attributes, Unicode/glyph sequence, origins, and glyph rectangles; extended vector-drawing records including clipping/group records; all painted-operation bounding boxes; image digests, transforms, and positions; link destinations and rectangles; and annotation content and geometry. PDF object numbers, document creation/modification metadata, and annotation dates are outside the geometry comparison.", "",
             "The French target is edition label `p. 58` in Chapter XV, shifted right by 6 TeX pt. The English target is manuscript label `[page 152]` in Chapter XII.5, shifted right by 20 TeX pt. A TeX point is converted to PDF coordinates by 72/72.27. Only these translated label coordinates have a 0.002 PDF-point serialization allowance; their vertical positions, text, font, and paint attributes must remain exact.", "",
             "A PDF fill-text operation can contain the target label together with many body-text spans. Every non-target span is still required to be exactly unchanged. For that one shared operation, an aggregate horizontal bounding edge may remain fixed where the unchanged body text determines it, while a label-determined edge moves by the permitted distance. The JSON records the operation's span count and before/after rectangles. Other painted-operation boxes must remain exactly equal.", "",
             "## Per-book result", "",
             "| Book | Pages before / after | Unchanged pages | Target physical page | Label shift (TeX pt) | Result |",
             "|---|---:|---:|---:|---:|---|"]
    for book in report["books"]:
        target = (book.get("targets") or [{}])[0]
        lines.append(f"| `{book['book']}` | {book['before'].get('pages', '?')} / {book['after'].get('pages', '?')} | {book.get('exactly_unchanged_pages', '?')} | {target.get('physical_page', '?')} | {target.get('expected_shift_tex_pt', '?')} | {book['status']} |")
    lines += ["", f"Compared physical pages: **{report['totals']['pages']}**. Exactly unchanged pages: **{report['totals']['exactly_unchanged_pages']}**. Permitted moved labels: **{report['totals']['permitted_labels']}**.", "",
              "The JSON report records exact before/after label rectangles, observed coordinate shifts, per-component aggregate hashes, input PDF hashes, and matching compile-record hashes. Restoring only each validated label span and its painted bounding box to the saved coordinates must make every aggregate component hash equal.", "",
              "## Previously reviewed page images", "",
              f"Exactly **{report['totals']['raster_samples']}** reader pages from the sample lists in `PDF_VISUAL_QA.md` were rendered from both saved and final PDFs, at the same 1.45 scale, in RGB with no alpha channel. **{report['totals']['raster_samples_equal']}** have exactly equal rendered pixel hashes and image dimensions. Each page's before/after pixel identity is recorded in the JSON. No other pages were rasterized by this comparison.", "",
              "The unchanged sample pixels and whole-book geometry comparison supply evidence for carrying forward those visual observations to the final PDF identities. They do not replace visual inspection of the moved labels or validate mathematical arguments.", "",
              "## PDF identities", "", "| Book | Saved PDF SHA-256 | Final PDF SHA-256 |", "|---|---|---|"]
    for book in report["books"]:
        lines.append(f"| `{book['book']}` | `{book['before']['sha256']}` | `{book['after']['sha256']}` |")
    lines += ["", "## Reproduction", "", "Run from the extracted workspace root after all eight PDFs and build records are complete:", "", "```sh", "python output/records/scripts/compare_margin_refinement.py --baseline work/pre_margin_refinement --jobs 2", "```", "",
              "The baseline directory must contain the eight saved PDFs and their matching build JSONs. Their expected identities are recorded above. The command reads the current PDFs under `output/FR/` and `output/EN/`, verifies their compile-record and TeX-source hashes, and writes this Markdown report plus `MARGIN_REFINEMENT_COMPARISON.json`. It exits with a nonzero status on any unpermitted difference. It does not modify PDFs or TeX sources."]
    if report["status"] != "PASS":
        lines += ["", "## Differences requiring resolution", "", "See each book's `unexpected_differences` array in the JSON report. A failed comparison cannot be used to carry forward visual review."]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", default="work/pre_margin_refinement")
    parser.add_argument("--output-root", default="output")
    parser.add_argument("--jobs", type=int, default=2)
    args = parser.parse_args()
    if sum(map(len, VISUAL_SAMPLES.values())) != 68:
        raise SystemExit("Expected exactly 68 previously reviewed raster samples")
    baseline, output_root = ROOT / args.baseline, ROOT / args.output_root
    # Paths written to the report must remain workspace-relative.
    relative(baseline)
    relative(output_root)
    placement_path = output_root / "records/MARGIN_PLACEMENTS.tsv"
    with placement_path.open(newline="", encoding="utf-8") as handle:
        placements = list(csv.DictReader(handle, delimiter="\t"))
    for language, rule in TARGETS.items():
        rows = [r for r in placements if r["language"] == language]
        if len(rows) != 1 or any(rows[0][field] != rule[field] for field in
                                 ("id", "unit", "command", "argument")) or float(rows[0]["horizontal_shift_pt"]) != rule["shift_tex_pt"]:
            raise SystemExit(f"{language}: MARGIN_PLACEMENTS.tsv does not match the two reviewed placements")
    work = [(language, stem, page, str(baseline), str(output_root)) for language, stem, page in BOOKS]
    results = {}
    with ProcessPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        futures = {pool.submit(compare_book, item): item[1] for item in work}
        for future in as_completed(futures):
            stem = futures[future]
            result = future.result()
            results[stem] = result
            print(f"{stem}: {result['status']}; {result.get('exactly_unchanged_pages', 0)} exactly unchanged pages", flush=True)
    books = [results[stem] for _, stem, _ in BOOKS]
    report = {
        "schema": "margin-refinement-comparison-v1", "status": "PASS" if all(b["status"] == "PASS" for b in books) else "FAIL",
        "completed_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "python_version": sys.version.split()[0], "pymupdf_version": fitz.VersionBind,
        "script": relative(Path(__file__)), "script_sha256": digest_file(Path(__file__)),
        "placement_record": relative(placement_path), "placement_record_sha256": digest_file(placement_path),
        "non_target_numeric_tolerance": 0,
        "target_translation_tolerance_pdf_pt": LABEL_TRANSLATION_TOLERANCE_PDF_PT,
        "reviewed_sample_specification": VISUAL_SAMPLES,
        "reviewed_sample_raster_scale": RASTER_SCALE,
        "books": books,
        "totals": {
            "books": len(books), "pages": sum(b.get("counts", {}).get("pages", 0) for b in books),
            "exactly_unchanged_pages": sum(b.get("exactly_unchanged_pages", 0) for b in books),
            "permitted_labels": sum(len(b.get("targets", [])) for b in books),
            "unexpected_differences": sum(len(b["unexpected_differences"]) for b in books),
            "raster_samples": sum(len(b.get("reviewed_sample_pixels", [])) for b in books),
            "raster_samples_equal": sum(s["exactly_equal"] for b in books for s in b.get("reviewed_sample_pixels", [])),
        },
    }
    destination = output_root / "records"
    (destination / "MARGIN_REFINEMENT_COMPARISON.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (destination / "MARGIN_REFINEMENT_COMPARISON.md").write_text(markdown(report), encoding="utf-8")
    print(f"Overall: {report['status']}; {report['totals']}", flush=True)
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
