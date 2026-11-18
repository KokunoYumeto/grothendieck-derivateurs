#!/usr/bin/env python3
"""Assemble the human-readable report from the maintained proof/source ledgers."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
rows=[
('A.1','Proved; Lead1(a)–(c)','A.1–A.2'),
('A.2','Proved; explicit repaired K* cone','A.15'),
('A.3','Proved; strict at every n≥3, also n=2','A.3–A.8'),
('A.4','Proved for every fundamental localizer; exact intermediate criterion','A.10–A.14'),
('A.5','Cosieve closure and composition refuted for every finite n≥2; all inclusions decided','A.9'),
('B.1','Known; compressed R12 proof audited','B.1'),
('B.2','Classification proved; D₁⇒D refuted; strict 2-category version proved','B.4; B.7; B.9'),
('B.3','Every implication decided, including within set presheaves','B.3; B.5–B.8'),
('B.4','Proved for every bounded reachability interval','B.2'),
('B.5','Corrected manuscript statements proved','B.10'),
('C.1','Proved; integral obstructions checked independently','C.1–C.3'),
('C.2','Complete classification proved','C.4'),
('C.3','Low localizers and represented derivators classified; arbitrary-derivator W7 proved','C.5–C.8'),
('C.4','Ordinary, strict and total endpoint classes determined','C.7'),
('D.1','Principal filteredness assertion refuted; requested C_delta FreeMon subcase still under investigation','D.6–D.7; notes/D_Cdelta_attempts_*.md'),
('D.2','Lead3 formulas and hand computation proved','D.1–D.3'),
('D.3','Proved for every FreeMon diagram on Δ_inj','D.6–D.7'),
('D.4','Free-group alternative proved; earlier examples audited','D.4–D.5'),
('E.1','Lead4(a) false as stated; corrected comparison and (b),(c) proved','E.1–E.4'),
('E.2','Groups determined for every n, finite and arbitrary acts','E.5'),
('F.1','Corrected manuscript ledger proved','F.1–F.3'),
('F.2','Source access, exact inspected statements and search record supplied','Bibliography; source ledger below'),
('G.1','Both assertions refuted for Wtilde itself','G.1–G.3'),
('G.2','General weak-axiom assertions refuted; each Wtilde case decided; repairs proved','G.4–G.10'),
('G.3','Both implications proved; immediate direction and manuscript passage identified','G.6'),
('G.4','General infinite lemma refuted; fractions and model cases proved','G.11–G.14'),
('Lead1','(a)–(d) proved','A.1–A.2; A.15'),
('Lead2','All formulas and classification proved','C.1–C.4'),
('Lead3','All clauses proved, with stronger exact-index theorem','D.1–D.7'),
('Lead4','(a) refuted as written; corrected comparison and (b)–(d) proved','E.1–E.5'),
('Lead5','(a)–(c) proved with precise coherent interpretation; suggested converse refuted','B.2–B.8'),
('Lead6','Proved for every fundamental localizer','A.10–A.14')]
lines=['| Prompt item | Outcome | Statements / record |','|---|---|---|']
lines += ['| '+' | '.join(row)+' |' for row in rows]
text='\n'.join(lines)+'\n\n'+(R/'notes/report_core.md').read_text()
register=json.loads((R/'code/outputs/assemble_register.json').read_text())
bib=json.loads((R/'code/outputs/F_bibliography_ledger.json').read_text())
text+=f'\nCurrent register: **{register["claims"]} numbered statements**, with '+', '.join(f'{v} {k}' for k,v in register['status_counts'].items())+f'. Bibliography: **{bib["entries"]} entries**, {bib["opened"]} opened at the recorded passages and {bib["not_opened_body"]} whose body was not obtained.\n\n'
text+=(R/'notes/F_source_ledger.md').read_text()
text+='\n## Typesetting and visual inspection\n\n'
build=json.loads((R/'code/outputs/master_build.json').read_text())
text+=('The first G standalone build had one 50.8849pt overflow from an unbreakable Mathlib module name; the first combined check had one 62.95pt overflow from a bibliography URL. Both were corrected in source with break opportunities. These are **two distinct initial defects**; repeated appearances in intermediate logs are not counted as new defects.\n\n')
text+=f'The current master build, `{build["timestamp_utc"]}`, has {build["pages"]} pages, {len(build["overfull_boxes"])} overfull boxes, {build["over_2pt"]} boxes over 2pt, and {len(build["warnings"])} recorded warnings. All '+str(len(build['commands']))+' compilation commands returned zero. Full logs and exact commands are retained in `'+build['log_directory']+'`.\n\n'
qa=R/'code/outputs/pdf_visual_qa.json'
if qa.exists():
    d=json.loads(qa.read_text());text+=d.get('report_text','Visual inspection manifest: `code/outputs/pdf_visual_qa.json`.')+'\n\n'
else:text+='Rendering and visual inspection are still pending; the zero-overflow log is not presented as a substitute for the requested visual review.\n\n'
text+='## Checkpoints and preservation\n\nSession start: **2026-11-17 01:14:17 UTC**. Hourly checkpoint archives use new names and are never overwritten, renamed or removed. Attached inputs are excluded. The final/current work directory contains the source files, report, register, bibliography, all proof notes, exact programs and outputs, source-access records, and build logs.\n\n'
p=R/'code/outputs/checkpoint_preservation.json'
if p.exists():
    d=json.loads(p.read_text());text+=f'The preservation audit checks {d["entries_checked"]} entries from {d["checkpoint_archives"]} prior checkpoint archive(s). {d["superseded_versions_preserved"]} superseded versions are retained byte for byte under `history/`; unchanged files remain at their active paths. **No prior file is intentionally omitted.** The complete per-file source, retained path, SHA-256 and supersession reason are in `history/preservation_manifest.csv`. Older drafts are historical records; the master paper and current report give the current mathematical claims.\n\n'
else:text+='The checkpoint preservation audit will compare every earlier archive byte for byte and retain each superseded file under `history/`; its manifest will identify the active replacement.\n\n'
text+='The three-hour progress check falls at 04:14 UTC, with hourly reassessment afterwards under the user’s rule. The exact C_delta question and attempts remain visible until settled.\n'
(R/'DER_FOLLOWUP_report.md').write_text(text)
summary={'outcome_rows':len(rows),'report_words':len(text.split()),'claims':register['claims'],'unsettled_requested_subcase':'FreeMon comparisons over C_delta'}
(R/'code/outputs/assemble_report.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
