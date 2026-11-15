# Margin refinement comparison

**Result: PASS**.

The comparison covers every physical page of the eight final PDFs and their saved pre-refinement versions. It permits one specified margin-label translation per PDF. All other compared values must be exactly equal; no numerical tolerance is applied to non-target content or geometry.

Runtime: Python 3.12.14; PyMuPDF 1.26.6. Completed: 2026-11-12T19:31:44+00:00.

## Scope

The compared values are unsorted extracted page text; page, crop, trim, bleed, and art boxes and page transforms; every text span's font, paint attributes, Unicode/glyph sequence, origins, and glyph rectangles; extended vector-drawing records including clipping/group records; all painted-operation bounding boxes; image digests, transforms, and positions; link destinations and rectangles; and annotation content and geometry. PDF object numbers, document creation/modification metadata, and annotation dates are outside the geometry comparison.

The French target is edition label `p. 58` in Chapter XV, shifted right by 6 TeX pt. The English target is manuscript label `[page 152]` in Chapter XII.5, shifted right by 20 TeX pt. A TeX point is converted to PDF coordinates by 72/72.27. Only these translated label coordinates have a 0.002 PDF-point serialization allowance; their vertical positions, text, font, and paint attributes must remain exact.

A PDF fill-text operation can contain the target label together with many body-text spans. Every non-target span is still required to be exactly unchanged. For that one shared operation, an aggregate horizontal bounding edge may remain fixed where the unchanged body text determines it, while a label-determined edge moves by the permitted distance. The JSON records the operation's span count and before/after rectangles. Other painted-operation boxes must remain exactly equal.

## Per-book result

| Book | Pages before / after | Unchanged pages | Target physical page | Label shift (TeX pt) | Result |
|---|---:|---:|---:|---:|---|
| `DER_FR_diplomatique` | 915 / 915 | 914 | 615 | 6.0 | PASS |
| `DER_FR_corrige_apparat` | 1082 / 1082 | 1081 | 622 | 6.0 | PASS |
| `DER_FR_texte_de_lecture` | 899 / 899 | 898 | 603 | 6.0 | PASS |
| `DER_FR_annotated_master` | 915 / 915 | 914 | 615 | 6.0 | PASS |
| `DER_EN_diplomatic` | 915 / 915 | 914 | 438 | 20.0 | PASS |
| `DER_EN_corrected_apparatus` | 1061 / 1061 | 1060 | 448 | 20.0 | PASS |
| `DER_EN_reading` | 902 / 902 | 901 | 433 | 20.0 | PASS |
| `DER_EN_annotated_master` | 915 / 915 | 914 | 438 | 20.0 | PASS |

Compared physical pages: **7604**. Exactly unchanged pages: **7596**. Permitted moved labels: **8**.

The JSON report records exact before/after label rectangles, observed coordinate shifts, per-component aggregate hashes, input PDF hashes, and matching compile-record hashes. Restoring only each validated label span and its painted bounding box to the saved coordinates must make every aggregate component hash equal.

## Previously reviewed page images

Exactly **68** reader pages from the sample lists in `PDF_VISUAL_QA.md` were rendered from both saved and final PDFs, at the same 1.45 scale, in RGB with no alpha channel. **68** have exactly equal rendered pixel hashes and image dimensions. Each page's before/after pixel identity is recorded in the JSON. No other pages were rasterized by this comparison.

The unchanged sample pixels and whole-book geometry comparison supply evidence for carrying forward those visual observations to the final PDF identities. They do not replace visual inspection of the moved labels or validate mathematical arguments.

## PDF identities

| Book | Saved PDF SHA-256 | Final PDF SHA-256 |
|---|---|---|
| `DER_FR_diplomatique` | `4934273b62dc796ad9339d4004a069cb06c8f55464e5714548dee65f5968d878` | `ea63b05972a83fa916b041dd5c85441ea6b6da0401eee5e2f27f7f0a527aa4ad` |
| `DER_FR_corrige_apparat` | `3485b84f93b41ff806ba0b215428c364d916e669c9129c23adf1c03e1a8e66ff` | `08c6e300cff88207d0a1ebda84e49284f622ef2ad4ac983a63c8b226ee10fdb1` |
| `DER_FR_texte_de_lecture` | `688e48b970216c6b8d0187a9bdb07608d894238ac54ccf351bef21b69d752d9c` | `158d9b545a5434c61c97d2bb8c28baddd6bed31a34d5dda61c5fd2c19867a59e` |
| `DER_FR_annotated_master` | `166cd16ae8ce8ac58ffc3662949cdeb3882fe9df6f999778ab8695082aef0f15` | `cd4a5d286b349ef65ab16ca4b01eb0885efaba7088b3459807e7b4264153a7df` |
| `DER_EN_diplomatic` | `c173784fcbe138d28bb1c6d4770730793b6899c25a1214beb2f0f0487558018c` | `544d3b3f84665aa0c7e29db2f43306254f648d897656ed9bd2cb590655f439d1` |
| `DER_EN_corrected_apparatus` | `0fefb9fb72c5dbbb4ad7193562bf9a10fda3d486df94fa3ea5cf69d890bf1ae4` | `30cb37db498e4decf10701ac0ff3c579282170bba3be808c577617eb71b39fd6` |
| `DER_EN_reading` | `73de1e53f5f9cc4ab24b69cbbe3d9158dd9a0e2380e8351b73a39f28b685b185` | `eb43fd6b673ef04ee3403e43057ff8838a74501d39162232d3a3d117a4b97d7b` |
| `DER_EN_annotated_master` | `338312f0566b62559fb69ede7dd73d2973bf4a8167f817d98c4db25a87b40394` | `bc06085d66aa1339943cda859069c8dfa0359390e7877eb870d17ccccaca151b` |

## Reproduction

Run from the extracted workspace root after all eight PDFs and build records are complete:

```sh
python output/records/scripts/compare_margin_refinement.py --baseline work/pre_margin_refinement --jobs 2
```

The baseline directory must contain the eight saved PDFs and their matching build JSONs. Their expected identities are recorded above. The command reads the current PDFs under `output/FR/` and `output/EN/`, verifies their compile-record and TeX-source hashes, and writes this Markdown report plus `MARGIN_REFINEMENT_COMPARISON.json`. It exits with a nonzero status on any unpermitted difference. It does not modify PDFs or TeX sources.
