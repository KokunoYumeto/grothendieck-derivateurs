# Fixed paths in selected point and third-coordinate AKR branches

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026. The computations below concern specified finite full substages and the indicated prospective attachments. They do not prove an arbitrary-stage invariant or settle C.1.

## What the program tests

`code/finite_akr_point_fixed.py` builds the repaired first stage with s=45,n=3. Its point branches add a single s=153,n=3 attachment for the specified two coordinates of the lexicographically first W-arrow into P12 or P13. Here P12=`Q_0_1_0_1` and P13=`Q_0_1_0_2`, with zero-based source coordinates. The mixed branch imports the independently authored `akr_v3_mix.build('cross_13')`: it adds the disjoint sum P12+P13 and an s=297,n=3 attachment for the two lexicographically first W-arrows carried by its summands.

The program checks component injectivity for every arrow. It then checks all parallel pairs with source size at least four, both for disconnected fixed subsets in the actual source and for every possible fixed subset of the two generating copy maps in a prospective attachment of that pair. The latter subsets lie in the entire old target Y: the prospective arrows have source Y. In the P12 edge branch and the P13 edge branch this genuinely tests a source with nonzero M(Y)=K(Y)/F(Y).

The prospective target is not built. For each actual point-path length, the program collects all collisions β_i(t)=β_j(t), records their combined signatures and tests one representative of each signature. Every undiscovered copy pair has zero active-path signature and contributes exactly the common fixed set. Thus no copy-pair sampling is involved. The exact formula and its unbounded proof are now in `sections/akr_beta_fixed_subsets.tex`, label `C:beta-fixed-subsets`.

That proved lemma assumes finite injective f,g and no nontrivial directed cycle in their point relation. It uses each actual path's vertex count l, with l≤n≤k and s=4k+1. Its four-branch calculation only needs l≤k, so it covers all admissible numerical choices and is independent of the size-three finite tests. At most 2L−1 fixed subsets occur, where L is the largest path vertex count (or one when there is no nonconstant path). The accompanying `C:beta-small-overlap` is also proved, but additionally assumes component-injective f,g and at most one common point in their images.

## Results

All listed branches have no disconnected fixed subgraph in the tested old pairs, no disconnected prospective copy equalizer, and no failure of H-component injectivity on any actual arrow.

| Finite branch | New graph vertices / edges / components | Cycle rank / protected copies | Larger-source pairs | Exact prospective fixed subsets |
|---|---:|---:|---:|---:|
| P12 point pair (v1,v2) | 13617 / 6885 / 6886 | 154 / 153 | 11628 | 35186 |
| P12 point pair (v1,v3) | 13617 / 6885 / 6885 | 153 / 153 | 11628 | 35186 |
| P12 point pair (v3,v1) | 13617 / 6885 / 6885 | 153 / 153 | 11628 | 35186 |
| P13 point pair (v1,v2) | 13617 / 6885 / 6733 | 1 / 0 | 11628 | 35186 |
| W-cross attachment after P12+P13 | 52569 / 26433 / 26433 | 297 / 297 | 131868 | 396194 |

The four point-branch outputs are respectively `finite_akr_point_fixed.out`, `finite_akr_point_fixed_02.out`, `finite_akr_point_fixed_20.out`, and `finite_akr_point_fixed_P13_edge.out`. The mixed output is `finite_akr_point_fixed_cross13.out`. The mixed run takes approximately 44 seconds; the point runs approximately 3 seconds each in this environment.

For the point branches, a single larger-source hom-set contributes all pairs, namely the 153 maps from the old P12 or P13 into Y. For the mixed branch, three larger-source hom-sets contribute the 131868 pairs. This is a serious structural limitation: the runs are not complete second or third stages.

## Admissible numerical sequences

For every s=153 point branch, the program records

    a0=2, a1=8/5, a2=128/85, a3=511/340.

The prospective copy calculation uses s=4617,n=3. The required loss 3n/s is at most 1−a3/a2=1/512. It covers all 10656036 unordered pairs of prospective copy indices, via three or five distinct signatures according to the path-length pattern.

For the mixed branch, the builder supplies

    a0=2, a1=8/5, a2=512/325, a3=16384/10725.

The program takes the next value a4=64943/42900 and uses s=1017,n=3. The stage-two operation visible in this branch is a sum, so its parameters need not coincide with those of the separate s=153 point branches. In particular, a future s=297 attachment must not be asserted admissible after an s=153 point branch using the same sequence: the latter has already forced a2 close to 3/2.

## Small-source coverage and component arcs

The large parallel-pair loop deliberately omits V- and W-source pairs. A point source cannot have a disconnected fixed subgraph. Distinct W-arrow images have at most one common point, both by the audited AKR routing invariant and by the program's direct point-pair incidence check in each finite object. A bijective incoming W-arrow similarly treats the size-three clone of W. The remaining small objects have no distinct parallel maps into the new selected targets.

For W-source pairs, the exact prospective fixed subsets are a full f(W) or g(W), an empty set, or a singleton: two distinct three-point images with overlap at most one have nonconstant paths of length at most three, with at most one length-three path. Full W-images have one binary edge component and the third point in a different ambient component, by the verified H-injectivity. Thus the same connected-fixed-subgraph condition holds for these omitted pairs. Equal pairs f=g reduce to the already checked component-injective arrow image. This explains the small-source cases without claiming that millions of W pairs were individually enumerated.

For every W-arrow h, the program also computes its component arc E→C, where E=[hv1]=[hv2] and C=[hv3]. Every selected object has E≠C and no pair of opposite component arcs. Hence no W-source pair has a nontrivial component-relation cycle. At the P12 (v1,v2) target this is a directed star with one E-component and 6885 distinct isolated C-components. The P13 (v1,v2) target has 6580 distinct E-components and 6732 distinct C-components; it genuinely combines M(Y)=Z with inherited third-coordinate interactions.

## A component-path inflation that does occur

The absence of path inflation in the larger-source loop must not be extrapolated to every W-source pair. The supplementary exact component-arc mode found 6493 W-pairs in the P12 (v1,v3) branch whose point relation has longest path of two vertices but whose H-component relation has a path of three vertices. One explicit pair, in the program's concrete point labels, is

    f=(0,153,1),  g=(154,613,6121),
    component path 5109→6733→6121.

There are no component cycles, and the common admissible bound n=3 accommodates this increase. It is therefore not a failure of the specified attachment. It does refute the stronger proposed invariant that component paths always have length at most point paths.

The supplementary outputs are `finite_akr_point_components_02.out` and `finite_akr_point_components_P13_edge.out`, produced using `--only-component-arcs`. This mode explicitly marks that it does not rerun the larger fixed-subgraph tests. All five full fixed-search outputs have now also been refreshed with these W-component checks. The reversed P12 (v3,v1) branch has the same 6493 inflation pairs among 6795 component-path-three candidates. The P12 edge, P13 edge, and mixed cross branches have no W-path inflation of this kind; the latter two have respectively 6579 and 12771 component-path-three candidates. No all-stage conclusion follows from these results.

## Why further branches remain necessary

The proved small-overlap corollary `C:beta-small-overlap` explains why the point-attachment copy tests are intrinsically easy even when their source has M≠0: the two original copy images meet in at most one point. The mixed W-cross branch goes beyond one-point overlap, but its tested truncated domains still remain connected. The exact fixed-path kernel theorem identifies what a future failure must supply: a path between disconnected fixed components and a nonzero class of (g−f)σ in the old colimit. No such pair or nonzero class was found here.
