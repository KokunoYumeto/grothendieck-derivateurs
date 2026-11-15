"""Shared inclusion policy for current deliverables and historical retention."""
from pathlib import Path

SOURCE_REPRODUCTIONS = {'D_Thomason.txt', 'D_PoorRinot2025.txt', 'A_HH1979.txt', 'A_Klyachko2005.txt', 'D_CATHOT.txt', 'D_MSZ.txt', 'A_BDH_p38.png', 'Cpaths_DwyerKan1980Calculating.txt', 'D_FisherLodha2026.txt', 'D_MixedLF2026.pdf', 'D_PoorRinot2025.pdf', 'D_Raptis.txt', 'D_FisherLodha2026.pdf', 'A_PalmerWu.txt', 'D_MycielskiRN1968.txt', 'A_BDH1980.pdf', 'D_nonsingular_2026.txt', 'D_MycielskiRN1968.pdf', 'Cpaths_Mycielski_erratum_page.png', 'D_MixedLF2026.txt', 'A_Klyachko2005.pdf', 'Cpaths_DwyerKan1980Simplicial.txt', 'Cpaths_Mycielski_Ryll_Nardzewski_1968_erratum.pdf', 'A_BDH1980.txt', 'D_Cisinski.txt', 'Cpaths_DwyerKan1980Function.txt', 'D_nonsingular_2026.pdf'}


def is_source_reproduction(rel):
    rel = Path(rel)
    return rel.name in SOURCE_REPRODUCTIONS or "_D_mrn_pages" in rel.parts


def should_include(rel):
    rel = Path(rel)
    if any(part in (".build", "__pycache__", "_D_mrn_pages") for part in rel.parts):
        return False
    if is_source_reproduction(rel):
        return False
    if len(rel.parts) == 1 and rel.suffix in {".aux", ".bbl", ".blg", ".log", ".toc", ".out", ".fls", ".fdb_latexmk"}:
        return False
    return True
