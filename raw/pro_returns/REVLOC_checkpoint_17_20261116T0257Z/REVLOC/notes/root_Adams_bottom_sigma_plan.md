# A finite Adams test for the two remaining incoming differentials

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. Research plan and conditional lemma, not a numerical
Ext calculation and not a numbered manuscript result.

After D.2.55 the bottom stable Z4 survives through the twelve-stage.
The only incoming sphere AHSS maps that can alter it before d8 are
d6 and d7. Each nonzero subgroup of Z4 contains twice its generator.
Thus proving that 2alpha-sigma survives through the fourteen-stage
would prove both incoming differentials zero.

Choose a minimal two-local stable CW model of Sigma-infinity L and
write P14 for its fourteen-stage. Minimal means that every integral
cellular differential is even; unit cancellation constructs such a
model. Its mod-two homology through degree fourteen is the actual
homology of L in that range, and its Steenrod coaction is the truncated
actual coaction. The bottom cell is kept and represents alpha up to
an odd unit. An ordinary minimal-space construction is unnecessary.

The sphere element 2sigma has Adams filtration two and is detected by
h0 h3 in Ext^{2,9}(F2,F2). After shifting the bottom cell to degree
seven its image lies in Ext_A^{2,16}(H*(P14),F2). With the standard
Milnor coproduct, operation-dual homology is a left A*-comodule. In
the complex A*bar tensor-power-s tensor H*(P14), its representative
is [xi1|xi1^8] tensor a7, up to the cohomologically interchangeable
product ordering. The full differential must retain this convention;
switching the tensor order without also switching the coaction and
coproduct conventions is not valid.

If that Ext class is nonzero, it cannot support an Adams differential:
it is the natural image of the permanent sphere class. It cannot be
hit either. The only possible incoming differential to filtration two
is d2 from Ext^{0,15}; this group is zero because H15(P14;F2)=0.
Higher incoming differentials would have negative source filtration.
Convergence for this finite connective spectrum therefore detects a
nonzero completed image of 2alpha-sigma, and hence its ordinary
two-local stable image is nonzero as well.

The remaining finite problem is therefore an explicit boundary test
in the cobar complex. At filtration two and total degree sixteen, the
base homology degrees are seven through fourteen and the Steenrod
dual degrees total at most nine. Only xi1,xi2,xi3 occur. A boundary
can only come from filtration one in the same internal degree.
The relevant matrices are finite and can be checked exactly over F2.

The new D.2.56 candidate supplies dimensions and explicit suspension
quotients for H13 and H14; all operations must be computed on those
actual quotients, including their Browder relations. A nonzero result
would settle both incoming maps. A zero result would only show that
this filtration-two detector fails; it would not prove the homotopy
element zero or determine a later Adams-filtration lift.

The fibrations reader independently checked this conditional Adams
argument, recommended the stable minimal CW formulation, and caught
the left-comodule convention before implementing the finite complex.
The incoming C^{1,16} can use module degree15, which is zero for P14;
the outgoing C^{3,16} needs only module degrees at most13. Thus the
entire test uses exactly the degree-at-most14 actual comodule. No full
Steenrod comodule or numerical Ext result has yet been supplied.

## Completed calculation and improved interface, 16 November 2026

The historical plan above has now been carried out. The full input is
`code/outputs/I_L14_primary.json`; the decisive smaller proof is
`notes/EH5_bottom_sigma_four_class.md`, with the independent geometric
audit `notes/FGH_D2_bottom_sigma_geometric_audit.md`. Root has read the
complete operation engine, complete cobar engine, four-class hand proof,
all thirteen incoming columns and the finite-skeleton argument. All pass.
The four-class certificate has C1/C2/C3 dimensions 13/64/150, ranks
13/49, and a nonboundary bottom h0 h3. It proves d6=d7=0.

The minimal stable-CW discussion above is unnecessary and is superseded
by the following simpler interface. Choose an ordinary finite
fourteen-skeleton P14 of the finite-type CW model of L, keeping the
bottom sphere. Restriction in cohomology is an isomorphism through
degree thirteen and injective in degree fourteen. Therefore the actual
four-class Steenrod submodule of H*(L), in degrees 7,9,11,13, restricts
injectively into H*(P14). All its operations through fourteen agree;
those above fourteen vanish in P14. Dualizing gives the actual comodule
quotient needed by the certificate, regardless of any extra homology
of the ordinary skeleton in degree fourteen. H15(P14)=0 gives the
incoming-Adams-differential exclusion exactly as above. This avoids
both a minimal-CW existence theorem and identifying the entire
comodule of an ordinary skeleton with truncated homology of L.

D.2.57 is being consolidated from these audited pieces. It will assert
E8_(7,7)=Z4, not a value for d8(H0), the stable half-product pairing,
or the actual full-target class h.
