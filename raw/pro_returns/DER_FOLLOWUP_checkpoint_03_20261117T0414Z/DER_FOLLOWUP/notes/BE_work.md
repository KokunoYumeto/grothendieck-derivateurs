# B and E work log

## Initial audits

- Read TOTAL_EXACT_2 finite_tests.tex, Proposition FT:ty in full. The kernel-to-colimit step is valid: every element of the kernel has augmentation zero; finite sums represented at different objects still map to zero in colim P_q = Z. Therefore colim J = Z and L_1 colim Z[H] = Z.
- Read INDLOCAL C.21 and C.23. C.21's run count argument gives the exact cofinality condition. C.23's comma category contraction has the stated variance and its representable converse is valid.
- Read PATHS C.P1--C.P4. Keep enriched coherence, not just equality in the ordinary homotopy category.
- Read PRETOT A.1--A.5. A.4's retraction to nondegenerate simplices uses free degeneracy completion. Lead 4(a) improperly extends this to all simplicial sets.

## Lead 4(a) correction under development

For K = Delta[2]/boundary, the nondegenerate simplices are one vertex and one 2-simplex. The injection category on these has three arrows from the vertex to the 2-simplex, so its nerve has H_1 = Z^2. K realizes S^2. Thus the asserted second weak equivalence fails. The comparison B(Delta_{<=n}/K) ~ |K| should instead be proved by skeletal induction, using homotopy pushouts of discrete presheaf diagrams and truncated representables.

## Type-category interpretation

Ty^op is the augmented simplex category of the nerve of the indiscrete groupoid on two objects: a nonempty word is its string of vertices, and a letter map is a simplex map. Its alternating runs are the nondegenerate core. This may compute bounded interval subcategories and supply explicit counterexamples for the implication table.
