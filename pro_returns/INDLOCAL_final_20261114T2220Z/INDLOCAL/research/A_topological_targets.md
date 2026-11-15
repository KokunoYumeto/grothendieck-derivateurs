# Unimodular closure forces a nondiscrete topology on a countable simple group

Author: Part A collaborator. Written 2026-11-14 21:01 UTC.

All proofs in this note are supplied directly. The topological conclusion does not use Markov's theorem as an unproved input. Write `[a,b]=a b a^{-1} b^{-1}`. A one-variable word over a group F means an element of the free product F*〈x〉. Its exponent is its image under the homomorphism F*〈x〉→Z that kills F and sends x to 1.

## 1. A finite algebraic cover gives an unsolvable unimodular equation

Let F be nonabelian simple. Suppose a finite list of words w_1(x),...,w_m(x) satisfies

    w_i(1)≠1 for every i,
    F\{1} = ⋃_{i=1}^m {g∈F : w_i(g)=1}.

We construct a word v(x) of exponent zero such that v(1)≠1 and v(g)=1 for every g≠1.

First put v_1=w_1. Given v_{i-1}(1)≠1, choose c_i∈F with

    [v_{i-1}(1), c_i w_i(1)c_i^{-1}]≠1.

Such a c_i exists. Otherwise v_{i-1}(1) centralizes every conjugate of w_i(1), and hence its normal closure. Simplicity makes that normal closure F; the center of a nonabelian simple group is trivial, a contradiction. Define

    v_i(x)=[v_{i-1}(x), c_i w_i(x)c_i^{-1}].

Then v_i(1)≠1. Whenever one of w_1(g),...,w_i(g) is 1, v_i(g)=1, by induction. Thus v_m is nonidentity at 1 and vanishes elsewhere. If m≥2 it already has exponent zero, because it is a commutator. If m=1, choose c with [w_1(1),c]≠1 and replace v_1 by [w_1(x),c], obtaining the same values with exponent zero.

Now set

    u(x)=v(x)x.

Its exponent is exactly 1. For x≠1, u(x)=x≠1; at x=1, u(1)=v(1)≠1. Hence the equation u(x)=1 has no solution in F.

It follows that every nonabelian simple group that solves all one-variable exponent-±1 equations has the following precise property:

> For every finite family of words p_1,...,p_r with p_i(1)≠1, there is a≠1 with p_i(a)≠1 for all i.

The assertion for an empty family merely uses that F is nontrivial. This is the only group-theoretic property used below.

## 2. Direct construction of a group topology

Let F be any countably infinite group satisfying the displayed finite-avoidance property. Enumerate its nonidentity elements as f_1,f_2,... . We construct a nondiscrete Hausdorff metrizable group topology on F.

### 2.1. A proper auxiliary length

Give each symbol f_i and f_i^{-1} cost i. Define ℓ(g) to be the minimum total cost of a finite word representing g, with ℓ(1)=0. Every g has a representing symbol, so ℓ is finite. Integer costs make the infimum a minimum. It has

    ℓ(g^{-1})=ℓ(g),
    ℓ(gh)≤ℓ(g)+ℓ(h),
    ℓ(g)≥1 for g≠1.

For each integer R, only the finitely many generator symbols with index at most R can occur in a word of cost at most R, and such a word has length at most R. Thus every ℓ-ball of finite radius is finite. Put c(g)=2^{ℓ(g)}. Then c(kg)≤c(k)c(g).

### 2.2. Recursive finite constraints

We choose nonidentity elements a_1,a_2,... . A formal letter of level i is a symbol (g,i,ε), with g∈F and ε∈{1,-1}; it evaluates to g a_i^ε g^{-1} and has cost

    c(g) 2^{-i}.

At stage n require the following invariant:

    For every j≤n, no finite product of formal letters
    of levels i≤n and total cost <2^{-j} evaluates to f_j.    (∗_n)

The empty product is allowed and is 1, so never creates an obstruction. For j=n the requirement is automatic: each nonempty product has cost at least 2^{-n}.

Suppose a_1,...,a_{n-1} have been chosen satisfying (∗_{n-1}). For each j<n, list the products of formal letters of levels at most n and cost <2^{-j}. This list is finite. Indeed each occurring letter satisfies c(g)2^{-i}<2^{-j}, hence ℓ(g)<i-j≤n-j. The relevant g belong to finitely many finite ℓ-balls. Every letter has cost at least 2^{-n}, so a listed product has fewer than 2^{n-j} letters.

Replace a_n by the free variable x in every listed product, and append f_j^{-1}. This gives finitely many words p(x) over F. At x=1 all letters of level n disappear; what remains is a product of earlier letters, with cost still <2^{-j}. By (∗_{n-1}) it is not f_j. Therefore each listed p has p(1)≠1.

The finite-avoidance property supplies a_n≠1 at which all these words are nonidentity. This establishes (∗_n). For n=1 there are no nonautomatic constraints, and any a_1≠1 works.

### 2.3. The metric and its separation bound

Use the following symmetric collection of weighted letters:

- every nonidentity element g∈F as an ordinary letter of cost ℓ(g);
- every formal conjugate g a_i^ε g^{-1} as above, of cost c(g)2^{-i}.

Different formal letters may represent the same group element; their costs remain attached to their respective expressions. For h∈F define L(h) as the infimum of the total costs of all finite products of these letters evaluating to h. The empty product gives L(1)=0. Ordinary letters make L finite everywhere. Reversing and inverting a word preserves its cost, and concatenation adds costs, so

    L(h^{-1})=L(h),
    L(hk)≤L(h)+L(k).

For each j≥1 one has the strict separation bound

    L(f_j)≥2^{-j}>0.

To prove it, consider any representing word of cost <2^{-j}. No ordinary nonidentity letter can occur because its cost is at least 1. The word therefore consists of finitely many formal conjugates, with some maximum level n. If n<j, every letter has cost at least 2^{-n}>2^{-j}, so the word is empty and cannot represent f_j. If n≥j, (∗_n) excludes the representation. This proves the bound.

Thus d(g,h)=L(g^{-1}h) is a genuine left-invariant metric. Furthermore L(a_i)≤2^{-i}, using the level-i letter with conjugator 1. The chosen nonidentity a_i converge to 1, so the metric topology is nondiscrete.

### 2.4. Group operations are continuous

For fixed k∈F define

    D_k=max(c(k),1+2ℓ(k)).

Conjugating a formal level-i letter with conjugator g by k produces the level-i letter with conjugator kg. Its cost is at most c(k)c(g)2^{-i}. Conjugating an ordinary nonidentity letter g by k gives an ordinary nonidentity letter with cost

    ℓ(kgk^{-1})≤2ℓ(k)+ℓ(g)≤(1+2ℓ(k))ℓ(g).

Conjugate any representing word and then take infima. This proves

    L(k h k^{-1})≤D_k L(h)     for all h∈F.

For arbitrary g,g',h,h' one consequently has

    d(gh,g'h')≤D_{h^{-1}} d(g,g')+d(h,h'),

because (gh)^{-1}(g'h')=h^{-1}(g^{-1}g')h·h^{-1}h'. Similarly

    d(g^{-1},g'^{-1})≤D_g d(g,g').

These inequalities prove continuity of multiplication at every pair and of inversion at every point. Hence d defines the asserted Hausdorff metrizable group topology.

## 3. Consequence for the surviving targets in A.28

Combining Sections 1 and 2 proves:

> Every countable nonabelian simple group that solves every one-variable equation of total exponent ±1 admits a nondiscrete Hausdorff metrizable group topology.

The group must be infinite: for a finite nonabelian simple group, the finitely many words x g^{-1}, indexed by g≠1, give exactly a finite cover of the form excluded in Section 1.

Thus a surviving simple countable quotient of the S² example in A.28 must additionally be topologizable. The proof does not show that a nondiscrete topological group fails to solve a specified countable system, and it does not assert that this necessary condition decides the remaining target class.

## 4. Primary source that prompted the finite-cover check

Anton A. Klyachko, Mikhail A. Mikheenko and Alexander Yu. Olshanskii, *Solvability of unimodular equations in groups and Lie algebras*, arXiv:2608.28045v3 (24 October 2026), primary author PDF:

https://borowiecki.dev/pdf/2608.28045

Web reference: `turn417view0`. The arXiv abstract was returned by search as `turn417academia5`; direct arXiv PDF and abstract retrieval were disabled in this session.

Section 2 quotes KOO13, Theorem 2.3, concerning simple groups with a word equation having exactly one nonsolution. No KOO13 theorem is used as an unaudited input in Sections 1–3: Section 1 proves directly that any group satisfying the stated finite-cover hypotheses fails unimodular closure. The source's existence construction and any relation it might have to other target classes remain separate from that proved implication.
