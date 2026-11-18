# Moore normalization of the A34.6 search parameter

This applies the already proved reflection A34.3 / supplied REVLOC D.2.39(q). It is a search normalization within the accepted A34.6 reduction, not a new principal-row movement or an actual separator.

Let V be the connected primary pointed CW type in A34.6, and put

\[
C=M(\mathbb F_p,1)\wedge V,\qquad
A'=Q\Sigma^3C.
\]

The Moore-smash reflection gives

\[
\min\operatorname{Rev}(C\to*)=
\min\operatorname{Rev}(V\to*),\qquad
\operatorname{loc}(\Sigma^\infty C)=
\operatorname{loc}(\Sigma^\infty V).
\]

For completeness, use the actual suspension degree-p map on Sigma V. Its telescope is simply connected and has vanishing reduced integral homology, hence is contractible. The successive cofibers of its powers are built by cofiber extensions from C, and their homotopy colimit is Sigma²V. This proves the reverse reversible inclusion; the forward inclusion is smash closure. Taking suspension spectra proves the stable equality, or one may use the same telescope in spectra. This does not use the H-space p map on V.

If r is the lowest degree with G=H~_r(V;Z) nonzero, then

\[
\widetilde H_i(C;\mathbb Z)\cong
\widetilde H_{i-1}(V;\mathbb F_p).
\]

These groups are F_p-vector spaces. If G/pG is nonzero, the first nonzero degree of C is r+1, with bottom group G/pG. If G/pG=0, the first nonzero degree is r+2: the mod-p universal coefficient sequence in degree r+1 surjects onto G[p], which is nonzero for every nonzero primary torsion group. Thus the lowest homology degree n of A' is r+4 in the first case and r+5 in the divisible-bottom case. In both cases its bottom group has nonzero mod-p quotient, and the A34.6 bound may be written d=n-1. This removes the divisible-bottom branch by changing the generator, not by ignoring its original degree shift.

The connective spectrum **underlying** the infinite-loop space A' is

\[
E'=\Sigma^\infty\Sigma^3C
 \simeq \Sigma^4(\mathbb S/p\wedge\Sigma^\infty V).
\]

Multiplication by p² is null on the Moore spectrum. To see this directly, let i:S→S/p and q:S/p→Sigma S be the cofiber maps. Since q(p id)=p q=0, exactness of stable Hom makes p id on S/p factor as i h. But p i=0, so its square is zero. Smashing preserves this nullhomotopy. Hence p² id_E'=0, and every homotopy group of A' has exponent dividing p². At odd primes one can sharpen this to p: the usual pi_1(S)=Z/2 calculation gives pi_1(S/p)=0, and the cofiber exact sequence identifies End(S/p) with Z/p.

This exponent assertion concerns E' and therefore pi_*A'. It is **not** an assertion that p² kills the suspension spectrum Sigma-infinity A'; the latter has the extended-power summands in Snaith's splitting and has not been supplied such a uniform exponent.

A' remains aspherical for the original assumed reversible class, and its Snaith linear summand gives the same stable ideal as in A34.6. The rest of that proof therefore provides a possibly new null H-space separator for A' if the original hypothetical counterexample exists. No theorem has been found here that contradicts the resulting bounded-exponent generator together with an infinitely generated null H-space witness.
