# Nested commutator maps in the countable-target construction

Author: Part A collaborator. Updated 2026-11-14 20:57 UTC.

This note records checked algebra used to test the diagonal construction in A.27. It does not settle the remaining countable-target problem. Throughout, `[a,x]=a x a^{-1} x^{-1}`.

## 1. A generating-set and translation lemma

Let F be a nonabelian simple group and a≠1. Put S_a={[a,x]:x∈F} and K=〈S_a〉. The identity

    x[a,y]x^{-1}=[a,x]^{-1}[a,xy]

holds by multiplication. It puts every conjugate of every generator of K in K; replacing x by x^{-1} proves equality under conjugation. Thus K is normal in F. Since a is noncentral, at least one [a,x] is nonidentity, so simplicity gives K=F.

Consequently, for every nonconstant function f:F→T to any set T, there is a b∈F such that f is nonconstant on S_a b. Indeed, otherwise f(s b)=f(b) for every s∈S_a and b∈F, because 1∈S_a. This makes f invariant under left multiplication by every s and every s^{-1}, hence by 〈S_a〉=F, a contradiction.

The conclusion chooses b for one specified function f. It does not supply a single b for a countable family of functions. That simultaneous choice is not used without proof.

## 2. Two nested commutators cannot be constant

For a,b≠1 and c∈F, the function x↦[a,[b,x]c] is nonconstant. If it were constant, evaluation at x=1 would make its value [a,c]. Write s=[b,x]. The equation

    a s c a^{-1} c^{-1} s^{-1} = a c a^{-1} c^{-1}

then says that every s centralizes c a^{-1} c^{-1}. Section 1 shows that these s generate F. Thus c a^{-1} c^{-1} lies in Z(F)=1, contradicting a≠1.

Right multiplication of this function by an additional fixed element also preserves its nonconstancy.

## 3. A precise finite-simple counterexample to arbitrary depth

The arbitrary-depth statement obtained by simply iterating Section 2 is false for nonabelian simple groups. In A_5, write permutations as zero-based one-line tuples, with (p q)(i)=p(q(i)). Take the following constants, in order from the innermost commutator to the outermost:

1. a_1=(1,2,3,4,0);
2. a_2=(1,2,3,4,0);
3. a_3=(1,2,4,0,3);
4. a_4=(0,1,3,4,2);
5. a_5=(0,2,1,4,3);
6. a_6=(0,2,1,4,3).

All six constants are nonidentity even permutations. The function

    x ↦ [a_6,[a_5,[a_4,[a_3,[a_2,[a_1,x]]]]]]

is identically 1 on all 60 elements of A_5. Its successive image cardinalities are

    60, 12, 6, 4, 3, 2, 1.

The complete finite verification is `code/a_nested_commutator_checks.py`; its machine-readable output is `code/a_nested_commutator_checks.json`. The script both computes the image sets and separately evaluates every one of the 60 substitutions through all six commutators. No heuristic search remains in the verification.

This is a finite target example only. A.28 already excludes finite target images by the Higman input. The example identifies the failed induction; it does not refute the needed statement for any of the remaining infinite targets.

The same script also verifies a repetition-free variant. In inner-to-outer order, take (1,2,3,4,0), (1,2,4,0,3), (0,1,3,4,2), (0,2,1,4,3), (0,3,4,1,2), and (1,4,3,0,2). All constants are pairwise distinct; the image ranks are 60,12,6,5,3,2,1. Thus requiring pairwise distinct coefficients, as occurs before a chosen index in the repetition-free diagonal enumeration, does not itself repair the general induction.

## 4. Exact scope of the current construction

A.27 proves its diagonal block for mixed-identity-free targets, torsion-free two-conjugacy-class targets, and nonabelian uniformly simple targets. A.28 attaches these blocks over countable subgroups and interleaves all one-variable unimodular adjunctions. I independently audited its final equation-closure and Higman image restrictions, including the matrix-logarithm argument for arbitrary characteristic-zero coefficient fields.

For the S² construction, a nontrivial countable image would have an infinite simple quotient. The proved exclusions force such a quotient to have a mixed identity, fail every finite uniform simplicity bound, contain an infinite-order element, fail local linearity, and solve every one-variable unimodular equation over itself. No implication among these remaining requirements is claimed here.

## 5. Primary-source intake and its limited use

Opened the primary PDF of Henry Bradford, Kıvanç Ersoy, Jakob Schneider and Andreas Thom, *Mixed identities for simple locally finite groups*, arXiv:2608.14537v1 (14 August 2026):

- https://arxiv.org/pdf/2608.14537 — web reference `turn391view0`;
- https://arxiv.org/abs/2608.14537 — web reference `turn390view1`.

The introduction and Theorem A classify mixed identities in infinite simple locally finite groups. This does not resolve the remaining target class in Section 4, because the Higman argument already excludes locally finite target images. No theorem about arbitrary simple groups or arbitrary nested commutator compositions is inferred from that source.

Searches also located the primary *One-dimensional actions of Higman's group* page, https://discreteanalysisjournal.com/article/11151-one-dimensional-actions-of-higman-s-group (`turn395search7`). The possible relevance of simple left-orderable overgroups was communicated as a research direction only. No mixed identity, nonuniformity, or target example is asserted on the basis of this search hit.
