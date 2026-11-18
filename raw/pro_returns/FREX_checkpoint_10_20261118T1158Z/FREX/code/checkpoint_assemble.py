"""Assemble the statement register and checkpoint inventory from current sources."""
from pathlib import Path
import argparse, csv, datetime, hashlib, json, re, subprocess, zipfile

root = Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--checkpoint', type=int)
parser.add_argument('--registers-only', action='store_true')
args=parser.parse_args()
if not args.registers_only and args.checkpoint is None:
    parser.error('--checkpoint is required unless --registers-only is used')
checkpoint=f'FREX_checkpoint_{args.checkpoint:02d}.zip' if args.checkpoint is not None else None
archive=root.parent/checkpoint if checkpoint else None
if archive is not None and archive.exists():
    raise SystemExit(f'Refusing to overwrite existing checkpoint: {archive}')
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
aux = (root / 'FREX_paper.aux').read_text()
labels = {m[0]: (m[1],m[2]) for m in re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}', aux)}
# A theorem heading can move after its auxiliary label is evaluated. Use the
# rendered PDF heading for the user-facing proof page, keeping the aux ID.
pdf_pages=subprocess.check_output(['pdftotext','-layout',str(root/'FREX_paper.pdf'),'-'],text=True).split('\f')
heading_pages={}
for page_number,page_text in enumerate(pdf_pages,1):
    for match in re.finditer(r'(?m)^\s*(?:Theorem|Proposition|Lemma|Corollary|Example|Remark)\s+([A-G]\.\d+)\s+\(',page_text):
        heading_pages.setdefault(match.group(1),str(page_number))
sources=[]
def collect(path):
    if path in sources:return
    sources.append(path)
    for target in re.findall(r'\\input\{([^}]+)\}',path.read_text()):
        child=root/target
        if not child.suffix:child=child.with_suffix('.tex')
        collect(child)
collect(root/'FREX_paper.tex')
records=[]
for path in sources:
    text=path.read_text()
    pattern=r'\\begin\{(theorem|proposition|lemma|corollary|example|remark)\}(?:\[([^\n]*?)\])?\s*\\label\{([^}]+)\}(.*?)\\end\{\1\}'
    for m in re.finditer(pattern,text,re.S):
        kind,title,label,statement=m.groups()
        if label not in labels:
            raise ValueError(f'Missing compiled label: {label}')
        number,page=labels[label]
        page=heading_pages.get(number,page)
        status='Refuted' if 'Refuted' in (title or '') else 'Known' if 'Known' in (title or '') else 'Proved'
        refs='; '.join(dict.fromkeys(re.findall(r'\\ref\{([^}]+)\}',statement)))
        statement=re.sub(r'\s+',' ',statement).strip()
        records.append([number,statement,status,f'{path.relative_to(root)} ({label}), PDF p. {page}',refs,'',title or kind])
def key(r):
    p,n=r[0].split('.')
    return p,int(n)
records.sort(key=key)
fields=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
with (root/'FREX_results.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(fields);w.writerows(records)
with (root/'results_A_B.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(fields);w.writerows(r for r in records if r[0][0] in 'AB')

events=[]
for path in sorted(root.glob('CHECK_EVENTS_*.tsv')):
    with path.open(newline='') as f:
        for r in csv.DictReader(f,delimiter='\t'):
            events.append([r.get(k,'') for k in ['statement_id','date','who','type','outcome']])
for r in records:
    events.append([r[0],now[:10],'GPT-6 Astra (OpenAI), ChatGPT Pro, FREX run',
                   'integration and source-proof inventory',
                   f'{r[2]}; complete proof text present at {r[3]}. This inventory is not an additional independent mathematical review.'])
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)

if args.registers_only:
    print(json.dumps({'registers_refreshed_utc':now,'numbered_statements':len(records),'check_events':len(events)},indent=2))
    raise SystemExit(0)

rows=[
('A.1','Proved','Both exactness over any specified ring and totality depend only on the topological group under (S)','A.1,A.24--A.26'),
('A.2','Proved','Strong convex Ramsey and compact fixed-point equivalences','A.2--A.3'),
('A.3','INCOMPLETE','All listed implications decided except (iii); the remaining rational gate requires a nonmetrizable universal minimal flow and a distorted affine-relation image','A.5,A.7--A.12,A.16--A.19,A.23,A.30--A.33; C.12--C.13'),
('A.4','Proved','Complete table with all nine requested properties and every named example','A.22; B.3--B.4; D.9'),
('A.5','Proved','Dense compact averaging, finite-index obstruction, and both translation examples','A.4--A.8'),
('B.1','Proved','Exact totality reduction under FA, FA-empty, Op','B.1,B.7'),
('B.2','Proved with corrections','General orbit model, empty-support exception, and complete arbitrary Kan recovery','B.1,B.6--B.13,B.18--B.19'),
('B.3','Proved / Refuted','Converse to Op false; WEI criterion and open-subgroup types proved','B.2--B.3,B.6--B.9,B.12'),
('B.4','Refuted as stated','Missing admissible intersections; exact bridge criterion; ordinary relational case proved','B.5,B.14,B.17'),
('B.5','Proved','Independent cyclic and linear orders satisfy St and Op','B.4'),
('B.6','Known, rechecked','Cocycle class construction, stabilizers, and integral cycle audited','B.13'),
('C.1','Proved','Bar--cobar duality, including rational and prime coefficients','C.1'),
('C.2','Proved','Compact abelian torsors characterize exactness','C.2'),
('C.3','Proved / Refuted','Finite hom-set theorem; unrestricted converse fails for BQ','C.3'),
('C.4','INCOMPLETE','All-prime implication refuted; filtered Kan totalizations and arbitrary exact-base Kan assemblies are excluded; three-arrow obstructions exist in every degree and ordinary ultraproducts fail exactness, but the total-index restriction remains unresolved','C.5--C.16,C.22--C.31'),
('C.5','Proved','Explicit compact torsor and cocycle','C.17'),
('C.6','Refuted','Equal objectwise dimensions have different first derived limits','C.18'),
('C.7','Proved','Four-object exit index, degree-two class, and nonconstant degree-one obstruction','C.19--C.21'),
('D.1','Proved','All parameter classes satisfy the structural and totality hypotheses','D.1--D.2'),
('D.2','Proved','Exact over any nonzero ring iff b >= (k-1)a','D.3--D.5,D.9'),
('D.3','Proved','Amenable iff extremely amenable iff b >= (k-1)a; expansion obstruction corrected','D.6--D.8,D.12'),
('D.4','Proved','No parameter in this family separates exactness from amenability','D.9--D.10'),
('D.5','Proved','Unordered C_delta also fails exactness over every nonzero ring','D.11'),
('E.1','Proved with corrections','Precise closure theorem and necessary completeness assumptions','E.1--E.3'),
('E.2','Proved','Compact regime and exact obstruction subgroup','E.1,E.4'),
('E.3','Refuted','Uncountable directed surjective systems need not have dense limit projections','E.5'),
('E.4','Proved','Specified models and gaps located','E.6'),
('E.5','Known, independently reproved','Countable derived-limit zero-or-uncountable dichotomy','E.7'),
('F.1','INCOMPLETE','Available primary sources audited; original bodies of Isbell1974 and McDuff1979 not obtained; Oberst1968 checked at source','Bibliography and Part F'),
('F.2','Proved','Strict chain and full companion classification table for A.4 and all predimension parameters','F.1--F.2'),
('G.1','INCOMPLETE','All lexicographic embedding-gap diagrams pass; a coherent tree model reduces the universal Abelianization gate to a specified H2 transgression kernel and higher quotient-tree homology; vanishing remains unresolved','G.3,G.5--G.41'),
('G.2','INCOMPLETE','Intrinsic smooth-group criterion and group invariance proved; class F and strictness remain unresolved','G.1--G.4,G.6--G.41'),
('Lead 1','Proved','Exactness is determined by smooth group coinvariants','A.1,A.6'),
('Lead 2','Proved','Strong convex Ramsey equivalence and CC/Reiter','A.2'),
('Lead 3','Proved','Compact torsors and exactness in each coefficient category','C.2'),
('Lead 4','Proved with corrections','Direct Hall-flow proof; shadow graph caveat made precise','D.6--D.7'),
('Lead 5','Proved','Dense compact averaging and all finite-index obstructions','A.4--A.5'),
('Lead 6','Proved','Both amenable nonexact examples fully constructed','A.7--A.8'),
('Lead 7','Proved with corrections','Full theorem, empty F and missing Int corrections, all requested recoveries','B.1--B.19'),
('Lead 8','Proved / Refuted','Complete parameter dichotomy; proposed sparse-range candidate mechanism fails','D.1--D.12'),
('Lead 9','Proved with corrections','Three regimes, obstruction subgroup, and uncountable counterexample','E.1--E.6'),
('Lead 10','Proved / Refuted','Pair lifting valid; all-prime implication fails, total case remains unresolved','C.6--C.16'),
('Lead 11','Proved','Objectwise dimensions do not determine the obstruction','C.18'),
('Lead 12','Refuted and corrected','Orbit dictionary valid after correcting variance and fixed-point hypotheses','B.10--B.11')]
table='| Task | State | Outcome or remaining gate | Evidence |\n|---|---|---|---|\n'+'\n'.join('| '+' | '.join(r)+' |' for r in rows)+'\n'
summary='''
## Main established changes

Totality is now proved to depend only on the topological automorphism group in every strong Fraisse presentation satisfying (S). No rigidity, amalgamation enhancement, open-subgroup classification, or finite-intersection assumption is needed. The proof first transfers totality through full objectwise-cofinal subcategories using locally zero homology and a bar bicomplex, then passes through canonical relational ages. Exactness over every specified coefficient ring was already proved to be the same kind of group invariant. This settles the entire A.1 request. Totality also passes along continuous homomorphisms with dense image, excluding attempts to repair a nontotal cocycle group by changing its presentation or by realizing it as a continuous quotient of a total group. A.29 proves the same heredity for open subgroups, and exactness over each fixed ring passes to open subgroups by smooth induction.

The independently ordered poset category is exact over every unital ring, while its automorphism group is not amenable. The proof gives an explicit coherent integer weight on every finite set of linear extensions and a natural section of smooth coinvariants. An independent finite probability obstruction proves nonamenability.

The independently ordered punctured F_2-vector spaces are total and satisfy rigidity, strong amalgamation, functorial amalgamation over every base, St, Op, WEI and Fin. Their group is amenable by an explicit random-colouring and variance estimate, but a five-map parity identity obstructs F_2 and integral exactness at every target. This refutes A.3(ii) and the second clause of A.3(v). The parity identity is checked on all 168 natural orders of the seven-point target; the proof applies to all dimensions. A.31--A.33 now prove rational exactness of this same example: a Ramsey category of distinguished bases and independently ordered subset sums supplies an exact auxiliary category, and a finite simplex-code average has equal marked support marginals. The example therefore also refutes the finite-index and Fin converses in A.3(vi)--(vii) even with totality and all the named structural hypotheses. A further explicit diagram of finite-rank free abelian groups has a nonzero element of order two in its ordinary colimit, obtained by lifting the same parity identity and checking uniform natural-order averages.

The cocycle classes A_r(Lambda), for countable abelian Lambda and r >= 2, have a complete field profile: rational exactness holds precisely when Lambda is torsion, and F_p exactness holds precisely when multiplication by p on Lambda is bijective. Integral exactness holds precisely when Lambda = 0. In particular A_2(Q) is exact over every prime field but not over Q, and is not total. Finite nonzero Lambda give rationally exact examples with (Fin) that are not integrally exact. The totalization route is now excluded much more generally: C.25 proves that every filtered colimit of connected Kan simplex categories with weakly contractible base is integrally exact, for arbitrary transition functors. C.24 separately proves the rationally acyclic version for rational-vector cocycle coefficients. These are complete finite-obstruction and functor-transfer arguments, not merely computations of constant coefficients. C.26 also excludes fixed-degree coefficient-pushforward Grothendieck assemblies over an integrally exact base: the assembly is total precisely when its coefficient diagram is locally zero, and then it is integrally exact. A persistent-order set action detects the obstruction in every other case. C.27 removes the coefficient-pushforward and fixed-degree restrictions: every Grothendieck assembly of connected small Kan simplex categories over an integrally exact base is total if and only if it is integrally exact, for arbitrary transition functors. Its proof detects persistent fibre loops by cyclic covering actions and then kills all finite homotopy and homology witnesses along a suitable sequence. C.28 proves that three arrows already suffice for a rational primitive obstruction in every degree: finite translated cube faces in the ordered group Z wr Z yield a cycle pairing to r! with an explicit invariant volume cocycle. Thus arrow count alone cannot bound the degree of the obstruction. C.29 then excludes the ordinary ultraproduct route altogether: a two-arrow shift-window family has affine-witness support at least n over every nonzero ring, so the ultraproduct is neither exact over any such ring nor total. The distinguished three-arrow family itself contains a shift chain of length r, so a selected ultraproduct subcategory retaining it also has no finite affine witness. C.30 supplies an additional warning within C_delta itself: one 24-vertex target has a normalized F2 witness and no rational witness for a three-arrow family, but a complete bridge argument produces an integral witness at a later target. The finite-stage characteristic effect does not persist. C.31 excludes filtered totalizations using fixed finite edge-voltage covers: one nine-vertex partite atom has compatible strong sections into every cover, so its all-ring obstruction survives every stage. No general total counterexample follows.

The entire ordered predimension family has been classified: all are total, and exactness over any nonzero ring, amenability, and extreme amenability hold precisely when b >= (k-1)a. The low range has an explicit finite strong atom and an injective representable-module obstruction. This rules out the suggested C(2,2,1) and C(3,3,1) examples as potential exact-but-nonamenable witnesses.

Amenability with metrizable universal minimal flow implies rational exactness. Thus the remaining A.3(iii) gate is confined to nonmetrizable universal minimal flows. A.30 identifies an additional precise analytic requirement: any amenable rationally nonexact example has a cyclic smooth relation image with unit filling norm but ambient l1 norm tending to zero. No general undistortion theorem is asserted. New general lemmas show that module injectivization preserves all derived colimits on total indices and that globally bounded finite-dimensional coefficient diagrams are acyclic. For free monoids, all rank-one diagrams and all lexicographic embedding-gap diagrams pass the comparison. An intrinsic criterion in terms of smooth locally free group monoids proves that the comparison class itself is a topological-group invariant. Invariant tree orders on every finite-support orbit are classified by finite signed lexicographic flags. This excludes every global positive realization of the original DF incidence group relation, including arbitrary rectangle factorizations and additional generators. A separate twisted four-factor pattern has been realized on the complete finite V,W,X11 diagram, with injective free-monoid maps, exactly the required six integral incidence relations, and both required signed lexicographic cut chains. Its core words do not satisfy the excluded group relator. This is a finite construction, not a global diagram or a nonzero derived-colimit example. G.23--G.24 classify all invariant partial orders on the strong-singleton orbit and apply the positive abelian cone to force identical signed lexicographic flags for the two twisted cut chains; all 552 unequal ordered flag pairs are excluded. The surviving identical-flag cases still require a global coherence argument. G.25 proves that every bounded order-cut stabilizer in the locally free group completion is locally cyclic; over C_delta its stabilizer-coefficient bundle is colimit-acyclic. G.26 constructs the canonical median tree of finite-parameter cuts and proves contractibility of every subgroup-fixed nerve for the automorphism action. G.27 then proves that the canonical map from the group completion of the fixed monoid to the fixed subgroup of the group completion can fail both injectivity and surjectivity, even in explicit branched-gap examples whose positive derived Abelian colimits all vanish. G.28 proves unique splitting of every discrete central extension over any group with a total strong presentation and applies it to the affine tree stabilizers. G.29 shows that even bounded affine fixed cuts do not imply conjugacy to vertex stabilizers. G.30--G.31 supply a coherent bisimplicial tree model with locally cyclic fibres; G.32--G.33 prove root closure and collapse the degree-one stabilizer row. The remaining H2 obstruction is exactly the kernel of a specified transgression from H2 of the quotient tree space to the direct sum of its cut stabilizer groups; higher source homology equals the corresponding quotient-tree homology. G.34 gives a fully explicit finite-rank injective free-monoid diagram with all positive derived Abelian colimits zero, but with nonzero H2 of the quotient tree and nonzero transgression. Thus the transgression is genuinely needed: neither injectivity of cut groups into group coinvariants nor vanishing of quotient-tree H2 is a valid shortcut. G.35--G.36 further show that smooth cuts on support lexicographic orbits form finite raw-coordinate cells, and that every comparison on a finite union of smooth tree orbits is expressible using only raw order and coordinate equality. These statements hold on the actual strong-support tuples; an unrestricted tuple extension or product-compatible exact cover is not inferred. G.37 proves inheritance of the comparison property by action components, open subgroups, dense images, and ordinary final functors. G.38 shows that injective diagrams with strictly positive integer transition matrices can still carry the rational obstruction, so positivity at the abelian level is insufficient. G.39 proves that bifix word embeddings need not amalgamate even when both induced group maps are isomorphisms with identical unimodular positive matrices. Thus compatible positive cones and free-group amalgamation do not supply the missing word coherence. G.40--G.41 identify a finite binary cut witness for every nontrivial bounded-cut stabilizer and prove that adjoining all smooth bounded cuts leaves the quotient model weakly equivalent, including its universal cover. This makes smooth limiting cuts available but does not prove injectivity of the transgression. The unrestricted abelianization and comparison questions remain unresolved in this work.

## Corrections recorded

- FE-1's assertion of exactness in every odd characteristic is false: cyclic class permutations give an obstruction in every prime characteristic.
- The finite-index formula E_U = B(U/G_F) needs nonempty F; the empty-support case includes the noncontractible cocycle categories.
- The implication from rigidity and the stabilizer-intersection identity to (Op) needs admissible intersections. The class of finite orders with only sizes 0 and at least 2 refutes the literal version.
- Lead 12 must distinguish left and right orbit-category modules. The flat constant module here has the opposite variance from the standard Bredon homological-dimension convention.
- Moore's relevant published theorem is 7.1(5)--(6), numbered 6.1 in the supplied preprint.
- The unrestricted finite-vector-torsor test and the bounded-finite-set converse fail for B(Q,+).
- The shadow-graph sparseness assertion requires its stated numerical restriction; the predimension proof itself has a separate Hall-flow argument.
- The inverse-limit obstruction is the kernel of lim1 K -> lim1 X. The closure quotient can be larger when coordinate images are not closed, and uncountable directed surjective systems require separate treatment.
- Schochet's zero-or-uncountable statement is Proposition 3.5, not Theorem 3.5.
- Li's opposite canonical-age/orbit-category identification is used with strong amalgamation as in Theorem 4.4. The unqualified introductory full-faithfulness assertion fails for a perfect matching.
- Oberst II.4.1 assumes F2-prime; its unrestricted conjecture and asserted monoid reduction in II.4.4 are false. The original body is now checked directly from the Goettingen digitization.
- Harman--Snowden's smooth modules for a measure-dependent completed algebra are not arbitrary smooth group-ring modules; their semisimplicity theorem cannot supply the missing rational exactness argument.

## What was read and computed

Every bibliography entry records its actual opened scope. The A/B proof notes identify the supplied sources checked in full at the points used. The primary sources opened include Oberst1968 (I.2.3, II.2.1, II.4.1--4.4), Moore, KPT, Bodirsky, Kechris--Sokic, Evans--Hubicka--Nesetril, Luck, Nucinkis, Bergman, Schochet, and the free-monoid sources listed in the bibliography. This checkpoint does not claim that the complete F.1 literature request is finished.

Programs and outputs are retained in code/ and verification/. Exact integer checks verified the poset weight identities for all 4,474 labelled posets through five points and all 102,085 one-point marginal equations. A finite infeasibility certificate independently detected the ordered-poset probability obstruction. Predimension certificates check all finite atoms used in the classification and the asymmetric unordered witness. C.4 includes explicit finite-support modular primitive distributions; the finite one-target exceptional-prime example is explicitly distinguished from an exact category. The exit-category and gap-diagram certificates are also retained.

## Typesetting and checkpoint status

The current PDF was rebuilt with LuaLaTeX and its cross references and citations checked. The checkpoint status JSON records the exact page count, overfull-box count, and unresolved-reference and citation checks. Rendered pages were inspected at the new theorem blocks and the report tables; the exact page sample and inspection record are retained in verification/. The runtime lacks luaotfload, so the manuscript uses Type 1 Latin Modern fonts and explicitly loads the installed font maps. The build log and exact page/overflow inventory are retained in verification/ and the checkpoint status JSON.

Checkpoint 01 was successfully saved at 03:07:35 UTC, checkpoint 02 at 04:07:41 UTC, checkpoint 03 at 05:07:32 UTC, checkpoint 04 at 06:07:35 UTC, checkpoint 05 at 07:10:17 UTC, checkpoint 06 at 08:07:19 UTC, checkpoint 07 at 09:10:04 UTC, checkpoint 08 at 10:05:58 UTC, and checkpoint 09 at 11:00:56 UTC. This newly named checkpoint preserves the current working files without overwriting an earlier archive. Rendered images, supplied background files, downloaded source scans, reproducible format files, and previous archives are excluded. All current source, proof notes, code, outputs, and verification records are included. The all-prime-exactness gate in C.4 was refuted by A_2(Q); only its total-index restriction remains. The proposed ordered finite-coproduct totalization was rejected because it fails condition I. C.25 now excludes every filtered colimit of connected Kan simplex categories whose base is weakly contractible. The finite family first lifts to a universal covering category, and a later stage kills its finite homotopy obstruction; a strict contractible path-space lift then gives an integral affine equalizer. The dated progress ledger records the remaining main gates and the next review time.


## Attribution

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. This remains an incomplete research manuscript; the unresolved rows above are not represented as solved.
'''
attempts=(root/'notes/remaining_gates_attempts.md').read_text()
(root/'FREX_report.md').write_text('INCOMPLETE\n\n# FREX research report\n\n'+table+summary+'\n'+attempts)
reviews=sorted((root/'notes').glob('movement_review_*.json'))
review=json.loads(reviews[-1].read_text()) if reviews else {}
review_text=(f"The latest completed movement review is {review.get('review_number','not yet recorded')}; "
             f"consecutive no-movement reviews: {review.get('consecutive_no_movement_reviews','unknown')}. "
             f"Next review: {review.get('next_review_utc','not recorded')}. ")
(root/'PROGRESS_LEDGER.md').write_text('# FREX progress ledger\n\nRun started 2026-11-18 01:34:20 UTC.\nUpdated '+now+'. Checkpoints 01--09 were saved successfully at 03:07:35, 04:07:41, 05:07:32, 06:07:35, 07:10:17, 08:07:19, 09:10:04, 10:05:58 and11:00:56 UTC; this is checkpoint '+str(args.checkpoint)+'. '+review_text+'The dated review file identifies the exact movement counted. C.25 excludes every weakly contractible filtered connected-Kan simplex totalization; C.26 characterizes coefficient-pushforward cocycle assemblies; C.27 excludes arbitrary connected-Kan simplex assemblies over every exact base unless they are already integrally exact. The universal A.3(iii), total C.4, and G.1/G.2 questions remain incomplete. See MOVEMENT_REVIEWS.md for the dated before/after gates.\n\n'+table)

pdfinfo=subprocess.check_output(['pdfinfo',str(root/'FREX_paper.pdf')],text=True)
pages=int(re.search(r'^Pages:\s+(\d+)',pdfinfo,re.M).group(1))
logpath=root/'verification'/f'build_checkpoint_{args.checkpoint:02d}_final.log'
log=logpath.read_text() if logpath.exists() else ''
status={'assembled_utc':now,'numbered_statements':len(records),'state':'INCOMPLETE','pdf_pages':pages,'overfull_final':log.count('Overfull '+chr(92)+'hbox'),'undefined_citations':bool(re.search(r'Citation .*undefined',log)),'undefined_references':bool(re.search(r'Reference .*undefined',log))}
(root/'notes'/f'checkpoint_{args.checkpoint:02d}_status.json').write_text(json.dumps(status,indent=2))


exclude_suffix={'.aux','.toc','.out','.log','.bbl','.blg','.fmt','.pyc'}
included=[];excluded=[]
for p in sorted(root.rglob('*')):
    if not p.is_file(): continue
    rel=p.relative_to(root).as_posix()
    if rel=='CHECKPOINT_MANIFEST.json' or bool(re.match(r'verification/checkpoint_\d+_pages/',rel)) or '__pycache__/' in rel or rel.startswith('notes/IsbellMitchell') or rel.startswith('notes/D_IsbellMitchell'):
        excluded.append({'path':rel,'reason':'rendered page, provided-source transcription, cache, or generated manifest'})
        continue
    if p.suffix in {'.aux','.toc','.fmt','.bbl','.blg','.pyc'} or rel=='FREX_paper.out' or rel=='missfont.log':
        excluded.append({'path':rel,'reason':'reproducible build intermediate'})
        continue
    data=p.read_bytes()
    included.append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
manifest={'checkpoint':checkpoint,'assembled_utc':now,'previous_successful_checkpoint':f'FREX_checkpoint_{args.checkpoint-1:02d}.zip' if args.checkpoint>1 else None,'included':included,'excluded':excluded,'unchanged_files_in_prior_checkpoints':[]}
(root/'CHECKPOINT_MANIFEST.json').write_text(json.dumps(manifest,indent=2))
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for item in included:z.write(root/item['path'],'FREX/'+item['path'])
    z.write(root/'CHECKPOINT_MANIFEST.json','FREX/CHECKPOINT_MANIFEST.json')
assert archive.stat().st_size < 500_000_000
print(json.dumps({'archive':str(archive),'size_bytes':archive.stat().st_size,'files':len(included)+1,'statements':len(records)},indent=2))
