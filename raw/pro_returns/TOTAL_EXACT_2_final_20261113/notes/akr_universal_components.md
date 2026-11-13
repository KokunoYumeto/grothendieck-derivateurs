# Universal repaired C.1: completed and independently audited

Final proof: `sections/akr_universal_components.tex`.
Historical proof: `sections/akr_universal_components_draft.tex` is
preserved, with its original Draft labels and status.

## Outcome and exact scope

For every admissible sequence `(a_m)` and every choice of actual-length
repaired targets, every generated arrow is injective on binary graph
components. Every parallel pair has an acyclic component transition
relation and

`L_H(f,g) <= L_U(f,g)+1`.

Every repaired attachment preserves the entire old cycle-functor
colimit and therefore the entire old binary H2. In particular the
first-stage class `kappa_+ - kappa_-` survives the infinite union.
The binary category of elements has nonzero integral H2 for every
admissible construction. This settles the full universal quantifier
in the user's Part C.1 and the former TOTEX C.6.

The proof includes arbitrary target relabelings and path enumerations.
It also verifies robustness to optional unused underlying target points:
represented-by-V status is preserved and reflected by all arrows,
whole beta paths have constant status, and all graph and component
arguments restrict to the represented points. Actual factorizations and
the full-underlying-point path bound remain in force.

## Proof structure

1. A forbidden pair in a source's generating cover at birth forces
   routing of the whole source arrow through any comparison image
   containing the pair. The proof moves the whole arrow through
   successive neighboring copies using (10), (11), and old routing.

2. Point visibility intervals have width at most `max(1,2n-2)`;
   C.1 gives `s>=15n`. Short circular intervals satisfy the Helly
   property. Descent therefore represents every nonempty pointwise
   equalizer as one existing arrow image.

3. Maintain the corresponding routing/Helly assertions on component
   sets while retaining factorizations as actual arrows. A component
   image intersection of size at least two descends to an actual
   commuting span `fu=gv`. It cannot terminate at V's singleton;
   at W, the two components are forbidden. For f≠g, the source of
   this span is strictly earlier than the common source S.

4. An original component path of r≥3 vertices becomes a reduced
   component path of r−1 vertices for `(v,u)`; an original component
   cycle gives a reduced cycle of the same length. Every nonconstant
   reduced point path with p vertices extends to an original point
   path with p+1 vertices. Nontrivial endpoint returns contradict
   point acyclicity; a constant final loop contradicts g-injectivity.
   Source-rank induction gives no component cycles and the bound
   `L_H<=L_U+1`. An intersection of size at most one has path size
   at most three directly, and f≠g implies `L_U>=2`.

5. At a new attachment, `L_U<=n` and C.1 gives `k>=n+1`.
   The strict graph-colimit theorem implies that the new component
   set is the repaired set necklace for Hf,Hg. Its path sizes are
   at most n+1≤k, so all component copy maps are injective; proper
   visibility widths are at most 2n<s/3. Routing and Helly extend,
   closing the stage induction without assuming the conclusion.

6. An equalizer graph is an existing arrow image, and this arrow
   is now known to preserve components. The exact fixed-path kernel
   is zero. The two independent first-stage circle groups have
   augmentation `(a,b)↦a+b`, so their difference generates an
   infinite cyclic H2 class. Finite-stage injections and the filtered
   union of nerve chains preserve it.

## Audit record

- The root independently checked the entire birth-cover and component
  induction, the strict graph-colimit dependency, numerical bounds,
  and arbitrary first-stage lengths. Passed.
- `main_compact_duality` independently checked all source descent,
  path/cycle reductions, actual-arrow versus component assertions,
  noncircularity, and the optional unused-point extension. Passed.
  Full audit: `notes/akr_universal_components_independent_audit.md`.
- `finite_tests_literature` independently checked the full canonical
  argument and the unused-point extension. Passed. Its requested
  precision adjustment has been incorporated: the final corollary
  invokes the represented-fixed-set variant for enlarged targets.

## Scope of completion

No mathematical item in the assigned universal C.1 question remains
undecided. The proof does not claim that every link individually has
vanishing H2; it proves the required attachment maps have zero old
kernel, which suffices for the requested universal nonzero H2 result.
It also does not assert categorical pullback/equalizer universal
properties or universal ordinary graph convexity, neither of which
is needed for the completed claim.
