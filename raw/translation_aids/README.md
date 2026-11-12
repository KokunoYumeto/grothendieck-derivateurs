# Translation aids for the English *Les Dérivateurs* and *La Longue Marche*

The working files that prepared the English translations of Grothendieck's *Les Dérivateurs* and *La Longue Marche à
travers la théorie de Galois*: the glossary that fixes the English words, notation and typesetting of both works, and
the comparison of translation models from which the route for the full translation was chosen. Both works use them,
so this folder is the one copy; the repository of *La Longue Marche*
([grothendieck-longue-marche](https://github.com/KokunoYumeto/grothendieck-longue-marche)) links here.

| Folder | What it is | Made | By |
|---|---|---|---|
| [`translation_glossary_20261110/`](translation_glossary_20261110/) | Terminology, notation and typesetting tables: `GLOSSARY_DER.csv` (171 entries) and `GLOSSARY_LM.csv` (116), `NOTATION_DER.csv`, `NOTATION_LM.csv`, `TYPESETTING.csv`; the decision files and scripts they are built from (`scripts/`); the n-gram, alphabet, operator-name, symbol and macro inventories of the French transcriptions and the search lists with their outputs (`inventory/`). Its [README](translation_glossary_20261110/README.md) gives the counts, the English sources in order of authority, and each decision with its reason. | 10 Nov 2026 | Claude Fable 5.2 (a Claude Code subagent) |
| [`translation_comparison_20261111/`](translation_comparison_20261111/) | The same French (five scans of *La Longue Marche*, package LM_P049; five edition pages of *Les Dérivateurs*, Ch. XVIII) translated by eight configurations with one prompt, then graded blind: the samples (`source/`), the prompt (`prompt/`), each run's output, log and usage (`runs/`), the script checks (`checks/`), the anonymized versions and the key (`blind/`, `key/`), the two blind gradings (`grading/`), how the pages were chosen (`selection/`) and the scripts (`scripts/`). [RUNS.md](translation_comparison_20261111/RUNS.md) has the costs, the checks, the grades and the decision: GPT-6.1 Sol at reasoning effort max for both works. | runs 10 Nov 2026 (22:48–23:59 UTC, the Sol max run last), grading and decision 11 Nov 2026 | Set up, run and checked by Claude Opus 5.5 (Claude Code). Translations by Claude Opus 5.5 (effort high and max), Claude Fable 5.2 (medium, high, and max for the one-page reference), Claude Sonnet 5.5 (high) and GPT-6.1 Sol (reasoning effort high and max). Blind grading by Claude Fable 5.2 (g1) and Claude Opus 5.5 (g2). |

- The French samples in `translation_comparison_20261111/source/` are excerpts of our transcriptions: *La Longue
  Marche* after its second pass, *Les Dérivateurs* in the corrected French of 11 November 2026. The translations in
  it are trial translations of those pages, not the published English.
- In these copies the first name of the user who ran the project is replaced by "user", local paths included. Python
  caches are left out. Nothing else is changed, so the scripts still name the local folders they read and the cost
  figures are those recorded at the time.
- To the extent that we hold any rights in these AI-produced files, they are dedicated to the public domain under
  CC0 1.0.
