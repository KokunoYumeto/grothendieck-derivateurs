"""Write RUNS.md: per configuration the tokens, the dollars per page, the script checks, and the extrapolations to the
whole works. Reads runs/RUNS.jsonl, runs/<config>/<sample>_result.json, checks/CHECKS.json, selection/MANIFEST.json.
usage: python -I -B report.py
"""
import glob
import json
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_tc as T  # noqa: E402
import run as RUN  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
N_LM, N_DER = 1500, 1171


def work_lengths():
    """Mean characters per page of the whole works, measured the same way as the samples (page segments)."""
    sp = os.path.dirname(T.LM_FILE)
    keys = {}
    for f in os.listdir(sp):
        m = re.match(r"LM_(.+?)_checked(_fixed)?\.tex$", f)
        if m and (m.group(2) or m.group(1) not in keys):
            keys[m.group(1)] = os.path.join(sp, f)
    lm = [len(p) for k in sorted(keys) for _, p in T.split_pages(T.read(keys[k]), "LM")]
    der_chars = 0
    for f in sorted(glob.glob(os.path.join(os.path.dirname(T.DER_FILE), "DER_*.tex"))):
        s = T.read(f)
        b = s[s.index("\\begin{document}") + len("\\begin{document}"):]
        der_chars += sum(len(p) for _, p in T.split_pages(b, "DER"))
    return {"lm_pages_measured": len(lm), "lm_files": len(keys), "lm_mean_chars": statistics.mean(lm),
            "der_chars": der_chars, "der_mean_chars": der_chars / N_DER}


def sample_stats(s):
    import checks as CH
    return {"formulas": len(CH.formulas(s)), "displays": s.count("\\["), "tikzcd": s.count("\\begin{tikzcd}"),
            "footnotes": s.count("\\footnote"), "texttt": s.count("\\texttt{["), "comments": len(CH.comments(s)),
            "deleted": s.count("\\deleted{"), "inserted": s.count("\\inserted{"), "unsure": s.count("\\unsure{"),
            "unsure_two": CH.unsure_bars(s), "illegible": s.count("\\illegible{"), "margin": s.count("\\margin{"),
            "uline": s.count("\\uline{")}


def money(x):
    return "$%.2f" % x if x >= 1 else "$%.3f" % x


def main():
    rs = [json.loads(x) for x in T.read(RUN.RUNS).splitlines() if x.strip()]
    done = {r["run"]: r for r in rs if r["event"] == "done"}
    sub = {r["run"]: r for r in rs if r["event"] == "submitted"}
    man = json.load(open(os.path.join(T.ROOT, "selection", "MANIFEST.json"), encoding="utf-8"))
    chk = json.load(open(os.path.join(T.ROOT, "checks", "CHECKS.json"), encoding="utf-8"))
    W = work_lengths()
    n_hits = {w: len(json.load(open(os.path.join(T.ROOT, "selection", "HITS_%s.json" % w), encoding="utf-8"))["glossary"])
              for w in ("LM", "DER")}
    order = [c for c in RUN.CONFIGS if c in done]
    total = sum(done[c]["billed_usd"] for c in order)
    L = []
    A = L.append
    A("# Translation comparison: La Longue Marche and Les Dérivateurs into English")
    A("")
    t_first = min(r["submitted"] for r in rs if r["event"] == "submitted")
    t_last = max(r["ended"] for r in rs if r["event"] == "done")
    A("Runs from %s to %s (UTC). Made by Claude (Claude Code, Opus 5.5) at the user's request of 10 November 2026." % (
        t_first.replace("T", " ")[:16], t_last.replace("T", " ").replace("Z", "")[:16]))
    A("")
    A("Seven configurations translated the same French with the same prompt: five pages of each work (one page of each "
      "for the reference, Claude Fable 5.2 at max). Below: what each run cost, what it would cost for the whole works, "
      "and the script checks of every output. Nothing here judges which translation is best; the blind grading "
      "(`blind/`, `key/KEY.json`) does that.")
    A("")
    A("Total billed for the comparison: **%s** at batch and Flex prices (budget $15), %d runs, one at a time. List "
      "price (no batch or Flex discount) is twice each figure." % (money(total), len(order)))
    A("")
    A("## The texts")
    A("")
    A("| sample | what | source file (lines) | characters |")
    A("|---|---|---|---|")
    for s in ("LM", "DER", "LM_ref", "DER_ref"):
        m = man[s]
        A("| `source/%s.tex` | %s | `%s` (%d-%d) | %s |" % (s, m["what"], m["source_file"], m["lines"][0],
                                                             m["lines"][1], f"{m['chars']:,}"))
    A("")
    sl = sample_stats(T.read(os.path.join(T.ROOT, "source", "LM.tex")))
    sd = sample_stats(T.read(os.path.join(T.ROOT, "source", "DER.tex")))
    A("- **LM**: package LM_P049 after its second pass (`LM_P049_checked.tex`; no `_checked_fixed` exists for it), "
      "scans 483-487, consecutive: prose, %d formulas (%d displays), %d `\\deleted`, %d `\\inserted`, %d `\\unsure` "
      "(%d bars between alternative readings), %d `\\illegible`, %d `\\margin`, %d `\\uline`, his abbreviations. The "
      "window was chosen among the five-scan windows of the second-passed packages for the number of glossary entries "
      "it contains (%d) and a length near the mean (%s characters per scan against %s over %s scans)." % (
          sl["formulas"], sl["displays"], sl["deleted"], sl["inserted"], sl["unsure"], sl["unsure_two"],
          sl["illegible"], sl["margin"], sl["uline"], n_hits["LM"], f"{man['LM']['chars'] / 5:,.0f}",
          f"{W['lm_mean_chars']:,.0f}", f"{W['lm_pages_measured']:,}"))
    A("- **DER**: `DER_XVIII-a.tex` of `corrected_french_20261111`, edition pages 1-5 (manuscript pages 50-60), "
      "consecutive: the opening of §4 (4.1 \"Pseudo-topos. Problème du produit\" and the start of 4.2), prose, %d "
      "formulas (%d displays, %d tikz-cd diagrams), %d footnotes, %d editors' `\\texttt{[...]}` additions, %d "
      "comments (running heads, [sic] notes). `UNEXPLAINED.md` lists no line for DER_XVIII-a (nor for DER_XIV), so no "
      "line had to be avoided." % (sd["formulas"], sd["displays"], sd["tikzcd"], sd["footnotes"], sd["texttt"],
                                   sd["comments"]))
    A("- **Reference pages** (Fable 5.2 at max): the first page of each sample, LM scan 483 and DER page 1.")
    A("- Each source file's sha256 is in `selection/MANIFEST.json`. No source file was changed by this work. Another "
      "session rewrote the files of `corrected_french_20261111` during the runs (10 Nov, 23:16 and 23:20 UTC); "
      "`DER_XVIII-a.tex` came back byte for byte the same (its sha256 still matches), so the sample is "
      "current. Three other chunks changed a little, which moves the DER total used below by a few hundred "
      "characters.")
    A("")
    A("## The prompt")
    A("")
    A("One prompt per work, identical for every configuration: `prompt/system_LM.txt`, `prompt/system_DER.txt` "
      "(template `prompt/PROMPT_TEMPLATE.txt`, parts `prompt/PROMPT_PARTS.txt`, built by `scripts/prepare.py`); the user "
      "message of each request is `prompt/user_<sample>.txt` (for DER it also lists the chunk's macro definitions used "
      "on the pages, for reference). It asks for a faithful English in his voice and register (his own English of "
      "*Pursuing Stacks* as the model, American spelling); every macro, page anchor and comment line kept, the words "
      "inside the text-carrying macros translated (`\\deleted` included; both readings of `\\unsure{A|B}` when they "
      "are words); formulas copied character for character, only French in `\\text{...}` translated; paragraphs kept; "
      "only the translated LaTeX returned.")
    A("")
    A("The terms are the glossary entries (`translation_glossary_20261110`, decision files `scripts/entries_*.txt`) "
      "whose French occurs on the pages, found with the glossary's own regular expressions (`scripts/list_hits.py`, "
      "`selection/HITS_*.json`): %d entries for LM, %d for DER, written compactly (one line each, related entries "
      "sometimes joined). Of the notation and typesetting " % (n_hits["LM"], n_hits["DER"]) +
      "decisions, the prompt carries those that act on the prose: his abbreviations written out, quotation marks "
      "``...'', the editors' brackets translated, `\\uline` kept, the apparatus of the transcription. Those that "
      "would change a formula are left out, because the formulas must come back unchanged; on these pages they are: "
      "LM `\\boldsymbol{\\Gamma}` as one macro for the doubled Gamma, `(1)\\qquad` as `\\tag{1}`, `\\mathrm{Norm}` as "
      "`\\operatorname{Norm}`, `\\longrightarrow` in running text as `\\to`; DER `\\mathcal{U}` as `\\mathfrak{U}`, "
      "`\\mathrm{Hom}` as `\\operatorname{Hom}`, (Ens) as (Sets), \"déf\" as \"def\" over the equality sign, "
      "`\\longrightarrow` in running text as `\\to`. They are mechanical and can be applied by script after the "
      "translation (for DER the macros `\\Hom`, `\\uHom`, `\\Ens`, `\\defeq` carry four of them, so the English "
      "preamble does it); the two pending decisions (natural or sharp, Fraktur S or calligraphic S) are copied as "
      "read. Two lines of the prompt go slightly beyond the glossary: \"likewise pseudo-topoi\" (from topos, plural "
      "topoi) and \"bi-contrafoncteur → bi-contrafunctor\" (from contrafoncteur).")
    A("")
    A("## Configurations and cost")
    A("")
    A("Prices per million tokens, input/output: Opus 5.5 $2/$10, Fable 5.2 $4/$20, Sonnet 5.5 $1/$5 (Message Batches "
      "API, half the list price); GPT-6.1 Sol $1/$5 (Flex tier). Output tokens include the thinking (Anthropic) or "
      "the reasoning tokens (OpenAI); \"thinking\" below is the output minus the visible translation, which was "
      "counted with the token-counting endpoint (Anthropic) or reported by the API (OpenAI). All requests: adaptive "
      "thinking, output cap 128,000 tokens, no prompt caching.")
    A("")
    A("| configuration | tokens in (LM + DER) | tokens out (LM + DER) | of which thinking | billed | $ per page LM | "
      "$ per page DER | minutes |")
    A("|---|---|---|---|---|---|---|---|")
    ext = []
    for c in order:
        d = done[c]
        req = {r["sample"]: r for r in d["requests"]}
        cfg = RUN.CONFIGS[c]
        ins = [req[s]["input_tokens"] for s in cfg["samples"]]
        outs = [req[s]["output_tokens"] for s in cfg["samples"]]
        th = []
        for s in cfg["samples"]:
            r = req[s]
            if r.get("thinking_tokens_estimated") is not None:
                th.append(r["thinking_tokens_estimated"])
            elif r.get("reasoning_tokens") is not None:
                th.append(r["reasoning_tokens"])
        lm_s, der_s = cfg["samples"]
        pl = req[lm_s]["billed_usd"] / RUN.PAGES[lm_s]
        pd = req[der_s]["billed_usd"] / RUN.PAGES[der_s]
        A("| %s | %s + %s | %s + %s | %s | %s | %s | %s | %s |" % (
            cfg["name"], f"{ins[0]:,}", f"{ins[1]:,}", f"{outs[0]:,}", f"{outs[1]:,}",
            " + ".join(("≈0" if x < 50 else f"{x:,}") for x in th) if th else "n/a", money(d["billed_usd"]),
            money(pl), money(pd), d["wall_minutes"]))
        cl = req[lm_s]["billed_usd"] / man[lm_s]["chars"] * W["lm_mean_chars"] * N_LM
        cd = req[der_s]["billed_usd"] / man[der_s]["chars"] * W["der_chars"]
        ext.append((cfg["name"], pl * N_LM, cl, pd * N_DER, cd, c == "fable52-max"))
    A("")
    A("The three Anthropic models share a tokenizer, so their input counts are the same; GPT-6.1 Sol's tokenizer counts "
      "about two thirds as many tokens for the same text. \"≈0\": Sonnet 5.5 at effort high chose not to think (its "
      "output equals the counted translation within the counting error). The visible translation itself is about "
      "4,500 (LM) and 7,900 (DER) tokens for the Anthropic models.")
    A("")
    A("Batch IDs, stop reasons and per-request figures: `runs/RUNS.jsonl`, `runs/<configuration>/<sample>_result.json`; "
      "one ledger row per run in `compute_cost_ledger/LEDGER.jsonl` (ids `trcmp-<configuration>`).")
    A("")
    A("## Extrapolation to the whole works")
    A("")
    A("Two estimates per work: the cost per page times the pages, and the cost per character of French times the "
      "characters of the whole work (which corrects for the samples being a little shorter or longer than the "
      "average page). LM: about %s scan pages at %s characters each (the mean over the %s second-passed scans); "
      "DER: the %s pages of the corrected French, %s characters in all (%s per page). Same prompt, five pages per "
      "request, batch or Flex prices, no caching." % (f"{N_LM:,}", f"{W['lm_mean_chars']:,.0f}",
                                                     f"{W['lm_pages_measured']:,}", f"{N_DER:,}",
                                                     f"{W['der_chars']:,}", f"{W['der_mean_chars']:,.0f}"))
    A("")
    A("| configuration | LM, 1,500 pages: per page | by length | DER, 1,171 pages: per page | by length | both works "
      "(by length) | against Opus 5.5 high |")
    A("|---|---|---|---|---|---|---|")
    base = [b + d2 for name, a, b, c2, d2, ref in ext if name == RUN.CONFIGS["opus55-high"]["name"]]
    for name, a, b, c2, d2, ref in ext:
        A("| %s%s | %s | %s | %s | %s | %s | %s |" % (
            name, " *" if ref else "", money(a), money(b), money(c2), money(d2), money(b + d2),
            ("%.2f×" % ((b + d2) / base[0])) if base else "n/a"))
    A("")
    A("\\* The reference translated one page per request, so its fixed share of the prompt per page is five times that "
      "of the others; its figures are an upper bound for five-page requests.")
    A("")
    A("## Script checks")
    A("")
    A("`scripts/checks.py`, on every full output against its French (`checks/CHECKS.json`; one detail file per output "
      "in `checks/`, with every changed formula, every flagged sentence and every missing term).")
    A("")
    A("1. **Formulas and macros back unchanged.** Every formula (inline, display, math environments) compared in order "
      "with the French after masking the words inside `\\text{...}`: identical / identical up to spacing / changed / "
      "missing / added. Page anchors (`\\scanpage`, `\\mspage`, `\\printedpage`, `\\msp`) in order; the comment "
      "lines; the count of every macro outside formulas; the bars of `\\unsure{A|B}`.")
    A("2. **No French left.** French function words (le, la, des, que, qui, dans, ...) and elisions (l', d', qu') in "
      "the running text, and sentences with several of them; accented words other than étale, dévissage and names; "
      "and French left in the wording of `\\text{...}` boxes inside formulas (masked in check 1, to be translated).")
    A("3. **Paragraph lengths.** Paragraphs split at blank lines and paired in order; the running text (formulas and "
      "macro names removed) English/French; flagged below 0.7 or above 1.5.")
    A("4. **Glossary.** For each glossary entry on a French page, whether its English form occurs on the same page of "
      "the output (\"entry-pages\"), and occurrences covered; British spellings (the glossary decided American).")
    A("")
    for work in ("LM", "DER"):
        A("### %s" % work)
        A("")
        A("| configuration | stop | only LaTeX | formulas: identical / spacing / changed / missing / added (of French) "
          "| anchors in order | comments | macro counts differing | French words / flagged sentences / elisions / "
          "French \\text{} boxes in formulas | paragraphs EN/FR, median ratio (min-max), flagged | glossary "
          "entry-pages, occurrences | British |")
        A("|---|---|---|---|---|---|---|---|---|---|---|")
        for c in order:
            cfg = RUN.CONFIGS[c]
            s = [x for x in cfg["samples"] if x.split("_")[0] == work][0]
            r = chk.get("%s/%s" % (c, s))
            if not r:
                continue
            f, p, g, fl = r["formulas"], r["paragraphs"], r["glossary"], r["french_left"]
            md = r["macros_differing"]
            A("| %s%s | %s | %s | %d / %d / %d / %d / %d (%d) | %s | %s | %s | %d / %d / %d / %d of %d | "
              "%d/%d, %s (%s-%s), %d | %d/%d, %d/%d | %d |" % (
                  cfg["name"], "", r["stop_reason"],
                  "yes" if r["clean_output"] else "no", f["identical"], f["spacing_only"], len(f["changed"]),
                  len(f["missing"]), len(f["added"]), f["french"], "yes" if r["anchors"]["same_sequence"] else "no",
                  "all" if r["comments"]["same"] else "%d of %d" % (r["comments"]["english"], r["comments"]["french"]),
                  ", ".join("%s %d→%d" % (k, v[0], v[1]) for k, v in md.items()) or "none",
                  fl["french_words"], len(fl["flagged_sentences"]), fl["elisions"],
                  len(fl["french_in_formula_text"]), fl["formula_texts"], p["paragraphs_english"],
                  p["paragraphs_french"], p["ratio_median"], p["ratio_min"], p["ratio_max"], len(p["flagged"]),
                  g["present"], g["entry_pages"], g["occurrences_covered"], g["occurrences_french"],
                  len(g["british_spellings"])))
        A("")
    A("Details that the tables compress (from the detail files):")
    A("")
    for c in order:
        cfg = RUN.CONFIGS[c]
        for s in cfg["samples"]:
            r = chk.get("%s/%s" % (c, s))
            if not r:
                continue
            notes = []
            f = r["formulas"]
            for a, b in f["changed"][:4]:
                notes.append("changed `%s` → `%s`" % (a[:90], b[:90]))
            if len(f["changed"]) > 4:
                notes.append("%d more changed formulas" % (len(f["changed"]) - 4))
            notes += ["missing `%s`" % x[:90] for x in f["missing"][:3]]
            notes += ["added `%s`" % x[:90] for x in f["added"][:3]]
            if r.get("marks_by_page"):
                notes.append("marks lost or added, by page: %s" % ", ".join(r["marks_by_page"]))
            if r["anchors"]["missing"] or r["anchors"]["added"]:
                notes.append("anchors missing %s, added %s" % (r["anchors"]["missing"], r["anchors"]["added"]))
            if r["comments"]["missing"]:
                notes.append("comment lines changed or missing: %d" % len(r["comments"]["missing"]))
            fl = r["french_left"]
            if fl["flagged_sentences"]:
                notes.append("French-looking: \"%s\"" % "\"; \"".join(x[:80] for x in fl["flagged_sentences"][:3]))
            if fl["french_word_counts"]:
                notes.append("French words: %s" % ", ".join("%s %d" % kv for kv in fl["french_word_counts"].items()))
            if fl["accented_words"]:
                notes.append("accented: %s" % ", ".join(fl["accented_words"][:12]))
            if fl.get("french_in_formula_text"):
                notes.append("French left in \\text{} of formulas: %s" % ", ".join(
                    "\"%s\"" % x for x in fl["french_in_formula_text"]))
            for x in r["paragraphs"]["flagged"][:3]:
                notes.append("paragraph ratio %s (FR \"%s...\")" % (x["ratio"], x["french"][:60]))
            if r["glossary"]["missing"]:
                notes.append("terms not found: %s" % "; ".join(r["glossary"]["missing"][:8]))
            if r["glossary"].get("fewer"):
                notes.append("terms found fewer times than their French: %s" % "; ".join(r["glossary"]["fewer"][:6]))
            if r["glossary"]["british_spellings"]:
                notes.append("British: %s" % ", ".join(r["glossary"]["british_spellings"]))
            if not r["clean_output"]:
                notes.append("output starts: `%s`" % r["output_start"][:60])
            A("- **%s, %s**: %s" % (cfg["name"], s, "; ".join(notes) if notes else "nothing to report"))
    A("")
    A("Limits of the checks: they test form, not sense. A formula can be right and the sentence around it wrong; a term "
      "can be present on the page and still be used in the wrong place; the French-word list catches untranslated "
      "sentences, not mistranslated ones; paragraph ratios catch omissions and additions of some size only.")
    A("")
    A("## The blind set")
    A("")
    A("`blind/<work>_<letter>.tex`: each full output, byte for byte, letters assigned at random per work "
      "(`scripts/blind.py`, random.SystemRandom); the letter-to-configuration mapping in `key/KEY.json`; the French in "
      "`source/` (`LM.tex`, `DER.tex`, and `LM_ref.tex`, `DER_ref.tex` for the one-page reference). No blind file "
      "names a model or a provider (checked by script). The grader should read only `blind/`, `source/` and "
      "`prompt/`; `runs/`, `checks/`, `key/` and this file name the configurations, and `selection/` holds how the "
      "pages were chosen (hashes, glossary hits). In each work one blind file covers only the first page: it "
      "translates `source/LM_ref.tex` or `source/DER_ref.tex`.")
    A("")
    A("## Files")
    A("")
    A("`scripts/`: `common_tc.py` (samples, glossary machinery), `list_hits.py`, `prepare.py`, `run.py` (one run at a "
      "time, budget and one-batch-at-a-time checks, ledger rows), `checks.py`, `blind.py`, `report.py`. Keys were read "
      "only through `claude_tools/run_with_note_key.py` (Anthropic, account B, `Untitled 1939.md`) and "
      "`enr_pilot.call` (OpenAI, `Untitled 1936.md`); none was printed or stored.")
    with open(os.path.join(T.ROOT, "RUNS.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("RUNS.md written; total billed $%.4f" % total)


if __name__ == "__main__":
    main()
