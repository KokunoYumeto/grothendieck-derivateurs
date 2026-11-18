# Parts E and H.5: working record

## Decisive corrections

1. Part E.1 is false already over `[2]`. The four-point fence `a -> b <- d -> c`, with values `0,1,1,2`, has contractible strict fibers and comma categories. Its homology coefficient system is constant `Z`. The pullback over `0 -> 2` is the discrete pair `{a,c}`. This refutes even the claimed sufficiency in the prompt. Exact finite verification: `code/EH5_fence_counterexample.py` and `code/outputs/EH5_fence_counterexample.json`.

2. H.5(ii) incorrectly equates containing `W_Z` with Loc (6 b). POLES B.13 explicitly distinguishes these. Every listed `W_a` contains `W_1` and is nontrivial; reversibility would then force every map to be an equivalence by successive desuspension of `S^2`, then `S^1`, then `S^0`. Thus all six fail Loc (6 b). Containment of `W_Z` is a separate question.

## Proposed exact repair for E.1 (proof being written)

Replace the comma condition by the simplex condition: for all `[n] -> B` and all vertices `i`, `E_{sigma(i)} -> E x_B [n]` is a homology equivalence. Its homology fibers form local systems `M_q`. The exact remaining condition is hypercentral action: the transfinite upper-central module filtration exhausts every `M_q`.

For arbitrary local systems `M` on a space `B`, invariance under all integral homology equivalences over `B` is equivalent to hypercentral action. Necessity: if the upper-central filtration does not exhaust, recursively choose `g_i` so successive `(g_i-1)` products on some element never vanish. Over the countable rose representing these loops, take a mapping telescope of maps fixing the rose and acting by `g_i-1` on an attached 2-sphere. The base inclusion is an ordinary homology equivalence; its relative twisted homology is the nonzero direct limit of `M` under these endomorphisms. Sufficiency: transfinite extension of trivial systems, exact sequences and filtered colimits.

For finitely generated `pi_1`, hypercentral means elementwise augmentation-ideal-power torsion. Uniform nilpotence is not necessary: `direct_sum_n Z[t,t^-1]/(t-1)^n` over the circle is a counterexample, also over a two-petalled rose by pullback.

The necessary homology-fiber condition follows from the same telescope and the relative homology spectral sequence. There is only one nonzero base-degree column, so no spectral-sequence cancellation can hide an individual fiber homology group. Need to spell out comparison between categorical and simplicial tests using the category of simplices and the homology-sharp spectral sequence.
