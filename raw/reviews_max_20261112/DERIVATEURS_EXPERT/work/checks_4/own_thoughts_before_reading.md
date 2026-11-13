# GALOIS: my own analysis before opening the return (12 Nov 2026, 15:00, clock checked)

D = derivator of a cocomplete (presentable) infinity-category DD. LC_D(X) = Ho Fun(|X|, DD).
1. For such D the 1-categorical and infinity-categorical notions agree: f^* preserves colimits, hence tensors
   K (x) F by spaces, and K (x) F is locally constant; [K, Map(F, G)] = Hom(K (x) F, G); so fully faithful
   (resp. equivalence) on Ho LC implies it on the infinity-categories. Hence W_D^lc = {f : Fun(|Y|, DD) ->
   Fun(|X|, DD) is an equivalence} and it IS a fundamental localizer (relative Theorem A by
   Fun(hocolim, DD) = lim Fun). For an abstract derivator the relative Theorem A is not available.
2. **W_D^1 (1-complete) is NOT a fundamental localizer: two out of three fails**, already for D = sets:
   * -> S^1 -> *: the composite and S^1 -> * are 1-complete (connected), * -> S^1 is not (pi_1 not onto). For
   D(Z): X acyclic non-contractible, * -> X -> *.
3. Values. Sets: W_D = W_0; W^1 = pi_0-bijective and pi_1-surjective; W^lc = W_1. (n-1)-types: W_D = W_{n-1},
   W^lc = W_n (the n-topos of (n-1)-truncated objects of S/X is that of tau_{<=n} X). Spaces: all = W-infinity.
   D(k), X connected: Fun(X, D(k)) = Mod over A_X = C_*(Omega X; k); for f: A_X -> A_Y:
   W^coh = W^hom = W^1 = {homotopy fibres of f are k-acyclic} (restriction is fully faithful iff
   A_Y (x)_{A_X} A_Y = A_Y, and A_Y (x)_{A_X} A_Y = C_*(F_f) (x) A_Y); W^lc = {H_*(Omega X; k) = H_*(Omega Y; k)}
   = pi_1-iso and k-homology iso of the loop spaces of universal covers. k = Z: W^lc = W-infinity; W^1 = acyclic
   maps; W_D = W_Z; all inclusions strict. k = Q: W^lc = pi_1-iso and pi_n (x) Q iso for n >= 2 on universal
   covers. Spectra: W^lc = W-infinity.
4. Tower (Lead 4): for sets W_0 > W_1 > W_2 ...; for D(Q), stage 2 (local systems of Q-linear categories) sees
   K(Z,2) (invertible ones: Hom(Z, Q^x) = Q^x) and K(Z/p,2) (not through invertible ones for p odd, but through
   Mod over Q(zeta_p), whose centre contains zeta_p).
5. Lead 3: Klein bottle and e -> BC_2 are in W_D minus W^lc (pi_1). Expect: with W^lc the fibration statements
   hold because W^lc is a localizer of the form "inverted by X -> Fun(|X|, DD)", for which fibrations are the
   maps over which the fibre functor is locally constant.
