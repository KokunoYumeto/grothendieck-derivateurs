"""Completeness check of the English units against the French, paragraph by paragraph (12 Nov 2026).

The checks of check_units.py compare whole units (formulas, anchors, labels, macro counts, paragraph counts and length
ratios between 0.7 and 1.5). This script looks inside the paragraphs, for what those checks cannot see:
  - sentences: the sentences of each French paragraph are aligned with the English ones by length (Gale and Church);
    a French sentence left without an English counterpart, or a group of sentences whose English is much shorter, is
    flagged ("sentence");
  - the text between formulas: where a paragraph's formulas are the same in both languages, the wording between two
    formulas is compared, in windows of three gaps (word order moves words across a formula) ("between formulas");
  - footnotes (\\footnote, \\footnotetext): compared one by one, in order, as paragraphs of their own ("footnote");
  - the editors' notes in typewriter type (\\texttt{[...]}): compared one by one, in order ("editors' note");
  - numbers in the running text (page, proposition and section numbers, cross-references): the multiset of the
    French paragraph against the English ("numbers");
  - French left in the English: sentences with French function words, French words of the subject, elisions, accented
    words ("French left"); also inside the editors' notes and footnotes;
  - paragraph length ratios under 0.8 for paragraphs of 200 characters and more ("paragraph");
  - the last paragraph of each unit (a cut-off answer) ("unit end").
Each flag is a candidate, read by hand before it goes into the gap list (COMPLETENESS_20261112.csv).

usage: python -I -B completeness.py [--en DIR] [UNIT ...]
  --en DIR: read the English units from DIR/<folder>/<unit>.tex (default translation/)
Writes checks/completeness/FLAGS.jsonl and checks/completeness/STATS.json.
"""
import collections
import importlib.util
import json
import math
import os
import re
import statistics
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
_spec = importlib.util.spec_from_file_location("cmp_checks", os.path.join(T.HERE, "cmp", "checks.py"))
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)
_spec2 = importlib.util.spec_from_file_location("check_units", os.path.join(T.HERE, "check_units.py"))
K = importlib.util.module_from_spec(_spec2)
_spec2.loader.exec_module(K)

OUT = os.path.join(T.ROOT, "checks", "completeness")

FN = re.compile(r"\\(footnote|footnotetext)(?![A-Za-z])\s*(\[[^\]]*\])?\s*\{")
TT = re.compile(r"\\texttt\s*\{")
# French words that are not English words (function words and words of the subject); "on", "a", "de", "en", "ce",
# "par" are left out (English words, names, Latin).
FRENCH_WORDS = set("""le la les des du au aux une est sont que qui dans avec sur cette ces cet mais donc ainsi pas très
nous je il elle ils elles leur leurs aussi comme entre où sans sous vers chez déjà encore toujours après avant depuis peut
faut fait été cela ceci ça quand lorsque puis alors tout toute tous toutes soit soient et ou un dont lequel laquelle
lesquels celle celui ceux ici sera serait était avait ont avons être avoir même plutôt notamment ne se sa son ses mon ma
mes pour sinon car voir aussi bien peu moins quelconque quelconques telle tels telles si ssi foncteur foncteurs
morphisme morphismes catégorie catégories flèche flèches ensemble ensembles objet objets espace espaces théorème lemme
corollaire démonstration remarque remarques exemple exemples hypothèse hypothèses axiome axiomes
équivalence équivalences propriété propriétés cas sens ceci cela autrement dit c'est n'est qu'il qu'on
d'un d'une l'on dès lors également
""".split())
ELISION = re.compile(r"(?<![A-Za-z])(?:l|d|qu|j|n|c|s|m|t)['’](?=[A-Za-zÀ-ÿ])", re.I)
ACCENT = re.compile(r"[àâçéèêëîïôûùüÿœ]", re.I)
# Accented words that are English or names here (checked by hand on the English units, 12 Nov 2026).
ACCENT_OK = set(K.ACCENT_OK) | {"étale", "étales", "coétale", "coétales", "dérivateurs", "dérivateur", "poincaré",
                                "künzer", "čech", "malgoire", "maltsiniotis", "grothendieck", "möbius", "hölder",
                                "fréchet", "cartan", "bénabou", "deligne", "giraud", "illusie", "verdier", "théorème",
                                "naïve", "naïvely", "naïveté", "rôle", "rôles", "déjà", "à", "vis-à-vis", "pêle-mêle",
                                "élan", "clichés", "cliché", "résumé", "café", "exposé", "exposés", "debâcle",
                                "débâcle", "coördinate", "été", "dévissage", "mélange", "séminaire", "géométrie",
                                "algébrique", "éléments", "récoltes", "semailles", "sémantique"}
ABBREV = re.compile(r"(?:\b(?:cf|resp|p|pp|prop|th|thm|cor|déf|def|lemme|lem|no|nos|n°|ch|chap|sect|ex|e\.g|i\.e|"
                    r"c\.à\.d|c-à-d|etc|loc|cit|op|vol|fig|eq|éq|M|MM|Mr|St|vs|resp|ibid|id|al|approx|n|nb|NB|"
                    r"a\.b\.c|sq|sqq|cad)\.$)|(?:\b[A-Za-z]\.$)|(?:\d\.$)", re.I)


def arg_end(s, i):
    return C.arg_end(s, i)


def take_args(s, rx):
    """The arguments of every match of rx (ending at an opening brace), and s with each argument replaced by a mark."""
    args, out, i = [], [], 0
    for m in rx.finditer(s):
        if m.start() < i:
            continue
        b = m.end() - 1
        e = arg_end(s, b)
        args.append(s[b + 1:e - 1])
        out.append(s[i:m.start()] + " ¤ ")
        i = e
    out.append(s[i:])
    return args, "".join(out)


def prose(s):
    t = C.prose(s)
    return t.replace("¤", " ").strip()


def sentences(t):
    """Split a running text (math replaced by §) into sentences: at . ! ? followed by space and a capital, a bracket
    or a § (a formula), unless the word before is an abbreviation."""
    out, start = [], 0
    for m in re.finditer(r"[.!?](?:['’\")\]]*)\s+(?=[A-ZÀ-Ý(\[«“\"§]|\\)", t):
        word = t[max(start, m.start() - 12):m.start() + 1].split()[-1] if t[start:m.start() + 1].split() else ""
        if ABBREV.search(word):
            continue
        out.append(t[start:m.end()].strip())
        start = m.end()
    rest = t[start:].strip()
    if rest:
        out.append(rest)
    return [x for x in out if x]


def letters(s):
    """Length of a sentence for the alignment: its characters other than spaces, the formula marks counted as 3."""
    return len(re.sub(r"\s", "", s.replace("§", "xxx")))


def norm_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


PRIORS = {(1, 1): 0.89, (1, 0): 0.0049, (0, 1): 0.0049, (2, 1): 0.0445, (1, 2): 0.0445, (2, 2): 0.011,
          (3, 1): 0.004, (1, 3): 0.004}


def gale_church(F, E, c, s2):
    """Align the sentence lengths F (French) and E (English); returns beads [(i0, i1, j0, j1)]."""
    n, m = len(F), len(E)
    INF = float("inf")
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    Bk = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0.0
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            best, arg = INF, None
            for (a, b), pr in PRIORS.items():
                if i - a < 0 or j - b < 0 or D[i - a][j - b] == INF:
                    continue
                l1, l2 = sum(F[i - a:i]), sum(E[j - b:j])
                mean = (l1 + l2 / c) / 2 if (l1 and l2) else max(l1, l2 / c, 1)
                delta = (l2 - l1 * c) / math.sqrt(max(mean, 1) * s2)
                p = max(2 * (1 - norm_cdf(abs(delta))), 1e-300)
                cost = D[i - a][j - b] - math.log(pr) - math.log(p)
                if cost < best:
                    best, arg = cost, (a, b)
            D[i][j], Bk[i][j] = best, arg
    beads, i, j = [], n, m
    while i > 0 or j > 0:
        a, b = Bk[i][j]
        beads.append((i - a, i, j - b, j))
        i, j = i - a, j - b
    return beads[::-1]


def numbers(t):
    return collections.Counter(re.findall(r"(?<![\w§])\d+(?:[.,]\d+)*", t))


def french_left(t):
    """Sentences of an English running text with French in them: [(kind, excerpt)]."""
    out = []
    for chunk in re.split(r"[.;:!?]\s|\n|§|\(|\)", t):
        ws = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ’']+", chunk)
        fr = [w for w in ws if w.lower().strip("'’") in FRENCH_WORDS]
        el = ELISION.findall(chunk)
        n = len(fr) + len(el)
        if (n >= 2 and n / max(len(ws), 1) >= 0.2) or n >= 3:
            out.append(("French words: %s" % " ".join(sorted(set(fr + el))), chunk.strip()[:200]))
    acc = sorted({w for w in re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ-]+", t) if ACCENT.search(w)
                  and w.lower() not in ACCENT_OK and w.lower().strip("-") not in ACCENT_OK})
    if acc:
        out.append(("accented words: %s" % " ".join(acc), t[:200]))
    return out


# French words of a sentence that are usually translated by a word with the same first letters (a cognate: catégorie,
# category; homotopie, homotopy; cofinal ...): where one is missing from the English of its sentence, a clause may be
# missing. "Usually" is measured on the whole book (calibrate): a stem counts when it occurs 5 times or more and its
# cognate is in the aligned English 90 per cent of the time or more.
FR_STOP = set(FRENCH_WORDS) | set("""comme cette toutes entre alors donc aussi encore toujours seulement lorsque
quand comment pourquoi parce puisque autre autres même mêmes chaque certain certains certaine certaines plusieurs
quelque quelques aucun aucune autant beaucoup moins assez trop jamais rien personne chose choses faire faite faites
dire voici voilà avoir être sont était étaient serait seraient pourrait pourraient devrait devraient doit doivent
peuvent pouvons vouloir veut voulons ailleurs ensuite enfin cependant pourtant néanmoins toutefois ainsi selon
""".split())


def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    return "".join(ch for ch in w if unicodedata.category(ch) != "Mn")


def ftoks(s):
    return {norm(w) for w in re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ]{5,}", s) if w.lower() not in FR_STOP}


def etoks(s):
    return {norm(w) for w in re.findall(r"[A-Za-z]{4,}", s)}


def cognate_in(f, es):
    """True when the English words es have a cognate of the French word f: the same first five letters (four when f
    has six or more), or f's first six letters inside an English word (nonsurjective)."""
    k = 5 if len(f) < 6 else 4
    return any(e[:k] == f[:k] for e in es) or (len(f) >= 6 and any(f[:6] in e for e in es))


def cognate_misses(ftxt, etxt, reliable):
    es = etoks(etxt)
    return sorted(f for f in ftoks(ftxt) if f[:5] in reliable and not cognate_in(f, es))


def page_of(text_before):
    m = list(re.finditer(r"\\printedpage\{([^}]*)\}", text_before))
    return m[-1].group(1) if m else "^"


def msp_of(text_before):
    m = list(re.finditer(r"\\msp\{([^}]*)\}", text_before))
    return m[-1].group(1) if m else ""


class Unit:
    def __init__(self, unit, folder, en_dir):
        self.unit = unit
        fr_doc = T.read(os.path.join(T.ROOT, "source", unit + ".tex")).replace("\r\n", "\n")
        en_doc = T.read(os.path.join(en_dir, folder, unit + ".tex")).replace("\r\n", "\n")
        self.fr = K.protect(T.english_anchors(T.body_text(fr_doc)))
        self.en = K.protect(T.english_anchors(T.body_text(en_doc)))
        self.flags = []
        self.stats = collections.Counter()

    def flag(self, kind, where, detail, fr, en, score=None):
        self.flags.append({"unit": self.unit, "page": where[0], "ms_page": where[1], "para": where[2], "kind": kind,
                           "detail": detail, "french": fr[:700], "english": en[:700],
                           "score": None if score is None else round(score, 3)})


def pair_paragraphs(PF, PE):
    if len(PF) == len(PE):
        return list(zip(PF, PE)), 0
    import difflib

    def sig(p):
        return tuple(re.sub(r"\s", "", x) for x in C.formulas(p)) + tuple(C.anchors(p))
    sm = difflib.SequenceMatcher(None, [sig(p) for p in PF], [sig(p) for p in PE], autojunk=False)
    pairs, unmatched = [], 0
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == "equal" or (a2 - a1) == (b2 - b1):
            pairs += list(zip(PF[a1:a2], PE[b1:b2]))
        else:
            unmatched += max(a2 - a1, b2 - b1)
    return pairs, unmatched


def compare_text(u, where, kind, tf, te, P):
    """Sentence alignment of one French running text with its English; flags dropped or shortened sentences."""
    SF, SE = sentences(tf), sentences(te)
    u.stats["sentences_french"] += len(SF)
    u.stats["sentences_english"] += len(SE)
    if not SF:
        return
    if not SE:
        if letters(tf) >= 15:
            u.flag(kind, where, "no English for this text", tf, te, 0.0)
        return
    LF, LE = [letters(x) for x in SF], [letters(x) for x in SE]
    if len(SF) * len(SE) > 40000:
        return
    # On these units the English keeps Grothendieck's sentences: of 5,869 paragraphs with sentences, 5,822 have as
    # many English sentences as French, 42 one more, 5 one fewer; the alignment has 13,211 beads 1:1, 170 2:2, 44 1:2,
    # 8 2:1 and no 1:0 (12 Nov 2026). So every paragraph with fewer English sentences and every bead that joins
    # French sentences is flagged, and every bead whose English is under 0.75 of its French (30 letters or more).
    if len(SE) < len(SF):
        u.flag(kind, where, "fewer English sentences (%d French, %d English)" % (len(SF), len(SE)), tf, te,
               letters(te) / max(letters(tf), 1))
    for i0, i1, j0, j1 in gale_church(LF, LE, P["c"], P["s2"]):
        lf, le = sum(LF[i0:i1]), sum(LE[j0:j1])
        ftxt, etxt = " ".join(SF[i0:i1]), " ".join(SE[j0:j1])
        miss = cognate_misses(ftxt, etxt, P["reliable"]) if i1 > i0 and j1 > j0 else []
        if j1 == j0 and lf >= 15:
            u.flag(kind, where, "French sentence without English (%d letters)" % lf, ftxt, "", 0.0)
        elif i1 - i0 > j1 - j0 and j1 > j0:
            u.flag(kind, where, "French sentences joined (%d:%d, ratio %.2f)" % (i1 - i0, j1 - j0, le / max(lf, 1)),
                   ftxt, etxt, le / max(lf, 1))
        elif i1 > i0 and lf >= 30 and le / lf < 0.75:
            u.flag(kind, where, "English shorter (%d:%d sentences, ratio %.2f)" % (i1 - i0, j1 - j0, le / lf),
                   ftxt, etxt, le / lf)
        elif len(miss) >= 2 or (miss and lf >= 30 and le / lf < 0.85):
            u.flag(kind, where, "French words without their usual English (%s; ratio %.2f)" % (
                ", ".join(miss), le / max(lf, 1)), ftxt, etxt, le / max(lf, 1))


def gaps_between_formulas(u, where, pf, pe):
    """Where the formulas of a paragraph are the same in both texts (in order), compare the wording between them."""
    def split(p):
        parts, fs, i = [], [], 0
        s = C.strip_comments(p)
        for m in C.MATH.finditer(s):
            parts.append(s[i:m.start()])
            fs.append(re.sub(r"\s", "", C.mask_text(m.group(0))))
            i = m.end()
        parts.append(s[i:])
        return parts, fs
    gf, ff = split(pf)
    ge, fe = split(pe)
    if ff != fe or len(ff) < 1:
        return
    LF = [letters(prose(x)) for x in gf]
    LE = [letters(prose(x)) for x in ge]
    n = len(LF)
    for k in range(n):
        a, b = max(0, k - 1), min(n, k + 2)
        wf, we = sum(LF[a:b]), sum(LE[a:b])
        if LF[k] >= 45 and LE[k] < 0.35 * LF[k] and wf >= 60 and we < 0.6 * wf:
            u.flag("between formulas", where, "wording between formulas %d and %d: French %d, English %d characters "
                   "(window %d/%d)" % (k, k + 1, LF[k], LE[k], wf, we), prose(gf[k]), prose(ge[k]), we / wf)


def check_unit(unit, folder, en_dir, P):
    u = Unit(unit, folder, en_dir)
    fr, en = C.strip_comments(u.fr), C.strip_comments(u.en)
    PF, PE = C.paragraphs(fr), C.paragraphs(en)
    pairs, unmatched = pair_paragraphs(PF, PE)
    u.stats["paragraphs_french"] += len(PF)
    u.stats["paragraphs_english"] += len(PE)
    if unmatched:
        u.flag("paragraph", ("", "", -1), "%d paragraphs not paired (French %d, English %d)" % (unmatched, len(PF),
                                                                                                len(PE)), "", "")
    pos = 0
    for k, (pf, pe) in enumerate(pairs):
        at = fr.find(pf[:60], pos)
        if at >= 0:
            pos = at
        where = (page_of(fr[:pos + len(pf)]), msp_of(fr[:pos + len(pf)]), k)
        # footnotes, compared one by one
        nf, mf = take_args(pf, FN)
        ne, me = take_args(pe, FN)
        u.stats["footnotes"] += len(nf)
        if len(nf) != len(ne):
            u.flag("footnote", where, "footnotes: French %d, English %d" % (len(nf), len(ne)), pf, pe)
        for a, b in zip(nf, ne):
            ta, tb = prose(a), prose(b)
            if letters(ta) >= 40 and letters(tb) / max(letters(ta), 1) < 0.7:
                u.flag("footnote", where, "footnote shorter (ratio %.2f)" % (letters(tb) / letters(ta)), ta, tb,
                       letters(tb) / letters(ta))
            compare_text(u, where, "footnote", ta, tb, P)
            for kind, ex in french_left(tb):
                u.flag("French left", where, "in a footnote: " + kind, ta, ex)
        # editors' notes in typewriter type
        tf_, _ = take_args(mf, TT)
        te_, _ = take_args(me, TT)
        u.stats["editors_notes"] += len(tf_)
        if len(tf_) != len(te_):
            u.flag("editors' note", where, "notes in typewriter type: French %d, English %d" % (len(tf_), len(te_)),
                   prose(mf), prose(me))
        for a, b in zip(tf_, te_):
            ta, tb = prose(a), prose(b)
            la, lb = letters(ta), letters(tb)
            if (la >= 25 and lb / la < 0.6) or (la >= 8 and lb == 0):
                u.flag("editors' note", where, "note shorter (%d -> %d characters)" % (la, lb), ta, tb, lb / max(la, 1))
            if re.search(r"[A-Za-zÀ-ÿ]{3}", tb):
                for kind, ex in french_left(tb):
                    u.flag("French left", where, "in an editors' note: " + kind, ta, tb)
                ws = [w for w in re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ']+", tb) if w.lower() in FRENCH_WORDS]
                if ws and not french_left(tb):
                    u.flag("French left", where, "in an editors' note, French word(s): %s" % " ".join(ws), ta, tb)
        # the paragraph's running text without its footnotes
        tf, te = prose(mf), prose(me)
        lf, le = letters(tf), letters(te)
        u.stats["letters_french"] += lf
        u.stats["letters_english"] += le
        if lf >= 200 and le / lf < 0.8:
            u.flag("paragraph", where, "paragraph ratio %.2f (%d -> %d characters)" % (le / lf, lf, le), tf, te,
                   le / lf)
        compare_text(u, where, "sentence", tf, te, P)
        gaps_between_formulas(u, where, mf, me)
        # numbers in the running text
        cf, ce = numbers(tf), numbers(te)
        miss = cf - ce
        if miss:
            u.flag("numbers", where, "numbers of the French not in the English: %s; English has %s" % (
                ", ".join("%s×%d" % (x, n) if n > 1 else x for x, n in sorted(miss.items())),
                ", ".join(sorted((ce - cf).elements())) or "nothing else"), tf, te)
        for kind, ex in french_left(te):
            u.flag("French left", where, kind, tf, ex)
    # the end of the unit: the last paragraph's last words
    if pairs:
        tf, te = prose(pairs[-1][0]), prose(pairs[-1][1])
        if letters(tf) >= 30 and letters(te) / max(letters(tf), 1) < 0.6:
            u.flag("unit end", (page_of(fr), msp_of(fr), len(pairs) - 1), "last paragraph shorter", tf, te)
    # the wording inside formulas and diagrams (text boxes, \parbox, tabular cells, TikZ nodes): formula by formula
    MF = [m for m in C.MATH.finditer(fr)]
    ME = [m for m in C.MATH.finditer(en)]
    u.stats["formulas"] += len(MF)
    if len(MF) == len(ME):
        for a, b in zip(MF, ME):
            ra = " ".join(x for x in K.text_runs(a.group(0)))
            rb = " ".join(x for x in K.text_runs(b.group(0)))
            la, lb = letters(re.sub(r"\\[A-Za-z]+\*?|[{}$]", " ", ra)), letters(re.sub(r"\\[A-Za-z]+\*?|[{}$]", " ", rb))
            if la:
                u.stats["formulas_with_wording"] += 1
            if la >= 25 and lb / la < 0.6:
                where = (page_of(fr[:a.start()]), msp_of(fr[:a.start()]), -1)
                u.flag("formula wording", where, "wording inside a formula shorter (%d -> %d letters)" % (la, lb), ra,
                       rb, lb / la)
    else:
        u.flag("formula wording", ("", "", -1), "formulas: French %d, English %d" % (len(MF), len(ME)), "", "")
    return u


def calibrate(units, en_dir):
    """The ratio c (English letters per French letter) and the variance s2 of the alignment, from the paragraphs; then
    the French stems whose cognate is in the aligned English sentence 90 per cent of the time or more (5 occurrences
    or more)."""
    xs, ys, texts = [], [], []
    for un in units:
        u = Unit(un["id"], un["folder"], en_dir)
        fr, en = C.strip_comments(u.fr), C.strip_comments(u.en)
        PF, PE = C.paragraphs(fr), C.paragraphs(en)
        if len(PF) != len(PE):
            continue
        for pf, pe in zip(PF, PE):
            _, mf = take_args(pf, FN)
            _, me = take_args(pe, FN)
            texts.append((prose(mf), prose(me)))
            a, b = letters(prose(pf)), letters(prose(pe))
            if a >= 30 and b:
                xs.append(a)
                ys.append(b)
    c = sum(ys) / sum(xs)
    s2 = statistics.mean([(y - c * x) ** 2 / x for x, y in zip(xs, ys)])
    occ, hit = collections.Counter(), collections.Counter()
    for tf, te in texts:
        SF, SE = sentences(tf), sentences(te)
        if not SF or not SE or len(SF) * len(SE) > 40000:
            continue
        LF, LE = [letters(x) for x in SF], [letters(x) for x in SE]
        for i0, i1, j0, j1 in gale_church(LF, LE, c, s2):
            if i1 == i0 or j1 == j0:
                continue
            es = etoks(" ".join(SE[j0:j1]))
            for f in ftoks(" ".join(SF[i0:i1])):
                occ[f[:5]] += 1
                hit[f[:5]] += cognate_in(f, es)
    reliable = {k for k, n in occ.items() if n >= 5 and hit[k] / n >= 0.9}
    return {"c": c, "s2": s2, "reliable": reliable}


def main(argv):
    en_dir = os.path.join(T.ROOT, "translation")
    if argv[:1] == ["--en"]:
        en_dir, argv = argv[1], argv[2:]
    units = [u for u in T.units() if not argv or u["id"] in argv]
    P = calibrate(T.units(), en_dir)
    c, s2 = P["c"], P["s2"]
    print("alignment: c = %.3f, s2 = %.2f, %d cognate stems" % (c, s2, len(P["reliable"])))
    os.makedirs(OUT, exist_ok=True)
    flags, stats = [], collections.Counter()
    for un in units:
        u = check_unit(un["id"], un["folder"], en_dir, P)
        flags += u.flags
        stats.update(u.stats)
    with open(os.path.join(OUT, "FLAGS.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for x in flags:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    stats = dict(stats, units=len(units), c=round(c, 4), s2=round(s2, 3), cognate_stems=len(P["reliable"]),
                 flags=len(flags),
                 flags_by_kind=dict(collections.Counter(x["kind"] for x in flags)))
    T.write(os.path.join(OUT, "STATS.json"), json.dumps(stats, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps(stats, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:])
