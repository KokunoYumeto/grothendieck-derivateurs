# Ordered graph exploration and the Ramsey exactness argument

AI-produced; no priority claim. All target vertices in the code and in
the displayed witnesses are numbered from zero.

## Universal outcome

`sections/ordered_graphs.tex` proves directly that a category with finite
hom-sets, common successors, and the morphism Ramsey property has exact
integral colimits. This resolves the ordered finite simple graph candidate
in the exact direction. It is stronger than the first finite-field
observation sent to root.

The key obstruction is the ideal `augmentation(kernel D)=d Z`. If `d != 1`,
choose a character of `Z/d` taking `1` to a circle point whose distance from
zero is at least `1/3` (use `1/2` for `d=0`, `floor(d/2)/d` otherwise). Extend
the induced character on `im D` to the free target using Smith normal form.
It gives a tuple of circle-valued potentials on p-embeddings. Partition each
circle into `3k+1` intervals. A monochromatic q-copy makes the sum of the k
potential differences have absolute value `<1/3`, contradiction. Thus the
obstruction ideal is the unit ideal. This proof avoids any passage from
modular exactness to integral exactness.

The primary Ramsey source is Hubička and Nešetřil, *All those Ramsey
classes*, arXiv:1606.07979v4 (3 September 2019), opened in full via
https://arxiv.org/pdf/1606.07979 . Corollary 4.3, printed p.51, explicitly
states that finite simple graphs with a free ordering are Ramsey. Printed
p.6 defines embeddings by preservation **and reflection** of relations;
printed p.3 defines the coloring property. All finite ordered graphs are
rigid, so copies and embeddings agree. Common successors are ordered
disjoint unions. An earlier statement of the exactness implication was
not identified; no novelty claim is made.

## Reproducible runs

```
python TOTEX2/code/finite_ordered_graphs.py --max-n 6 --output TOTEX2/code/finite_ordered_graphs_results.json > TOTEX2/code/finite_ordered_graphs.out
python TOTEX2/code/finite_ordered_graphs.py --max-n 0 --random-n 7 --samples 20000 --output TOTEX2/code/finite_ordered_graphs_random7.json > TOTEX2/code/finite_ordered_graphs_random7.out
python TOTEX2/code/finite_ordered_graphs_verify.py > TOTEX2/code/finite_ordered_graphs_verify.out
```

Observed runtimes: 4.462 seconds for exhaustive n<=6 and 6.092 seconds for
the random n7 sample. The latter uses Python Random seed 20261113 and
samples with replacement; its counts are sample counts, not counts of
isomorphism classes or distinct targets.

The exhaustive code checks all `2^(n choose 2)` graphs on the fixed ordered
vertex set. It records full rank-pair histograms for each family over Q,
F2, F3, and the first coefficient certificate for every successful field.
An extra augmentation row increases rank iff an affine kernel vector
exists. Rational arithmetic uses Fraction; finite fields use modular
inverses. The independent verification program does not import the search
program, reconstructs all induced path embeddings from edge sets, checks
the marginals and augmentation, and compares ranks using SymPy's exact
DomainMatrix over QQ, GF(2), GF(3).

For n<=5 no affine equalizer was found for either family over any of the
three fields, exhaustively. For n6 the counts (Q,F2,F3) were (42,34,42)
for the three vertices, (8,0,8) for the two edges. The n7 random sample of
20000 produced (243,199,240), respectively (51,14,48). Those random counts
carry no universal or exhaustive inference.

## Explicit integer certificates

Three vertex inclusions into q=the increasing induced 3-path:

- Target vertices 0,...,5; edges 01,12,13,15,23,24,34,35.
- `t=(012)-(015)+(124)-(134)+(235)`.
- All three marginals are the single vertex basis vector `[2]`.
- Integral augmentation 1; ranks D/Daug are 5/6 over Q,F2,F3.

Two edge inclusions into q:

- Target vertices 0,...,6; edges 01,12,23,35,56,14,45.
- `t=(012)+(123)+(235)+(356)-(014)-(145)-(456)`.
- The two edge marginals agree by telescoping along edge-state paths
  01->12->23->35->56 and 01->14->45->56.
- Integral augmentation 1; ranks 6/7 over all three fields.
- The same t equalizes the three vertex maps, with common marginal
  `[2]+[3]-[4]`.

The first n6 rational edge certificate has denominator 2 and therefore
does not prove integral equalization. Its integral annihilator has
augmentation 2. It is included to demonstrate the genuine coefficient
distinction in the finite target; it does not obstruct a larger target.

## Boundaries

The finite searches alone make no claims about arbitrary functors,
all-stage categories of elements, or the main totality implication. The
universal ordered-graph conclusion is provided by the proved Ramsey
criterion. No full seven-vertex exhaustive enumeration was needed after
the explicit integer witness and universal theorem were obtained.
