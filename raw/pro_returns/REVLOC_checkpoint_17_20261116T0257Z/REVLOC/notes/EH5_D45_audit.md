# Independent audit of D.2.45

Status: full mathematical PASS, 2026-11-15.

I read `sections/D2_integral_transfer.tex` in full and checked the
tensor differential, the norm map, the skeleton argument, and the
integral coefficient calculation independently.

## Opened primary interfaces

* John R. Klein, *On the stable Hopf invariant*, arXiv:2603.07854v3,
  <https://arxiv.org/pdf/2603.07854>: Theorem A(iii), printed p.3;
  the transfer proof pp.12--13; Theorem B p.4 and its comparison
  proof pp.13--16.  This identifies the operation with the
  Segal--Snaith projection and supplies the exact norm identity.
* Emery Thomas, *The suspension of the generalized Pontrjagin
  cohomology operations*,
  <https://msp.org/pjm/1959/9-3/pjm-v9-n3-p26-p.pdf>, Section 2,
  formula (2.1), printed p.899.  Its coefficient map at q=4 is
  `Z/4 -> Z/8, 1 -> 4`, not the map `1 -> 2`.  Thus it loses the
  even coefficient under investigation, exactly as stated.

## Decisive checks

The odd degree of a7 gives d(ab)=-4aa and d(ba)=4aa.  The
degree-fifteen kernel has the saturated integral basis
`ab+ba,ar,ra`; degree-sixteen relations give orders `4,2,2`.
The norm sends c to ab+ba and u to ar+ra.  Hence its complete
kernel on `Z/8{c}+Z/2{u}` is precisely `<4c>`.

For a target of dimension at most fourteen, its integral H15 is
zero, so the transfer identity puts the entire James--Hopf image
in this kernel.  The nonzero boundary of 2c follows from the
already audited metastable exact sequence.  At the fifteen-
skeleton the stable pi15 map is surjective, whereas the quadratic
pi15 map is an isomorphism, giving equality of full images.

The four low loop products used to prove H7*H8=0 have independent
James words.  A minimal Adams--Hilton differential in the required
degree has only these quadratic terms: there is no possible cubic
term at that degree.  Thus the asserted mod-two product vanishing
is justified on the actual target.

For an integral lift A of a with dA=4B, the mod-two vanishing lets
one choose C with dC=AB modulo two.  The cochain
`E=(AB-dC)/2` is integral and satisfies `dE=2B^2`.  It therefore
represents the desired half-product and has integral Bockstein
`x^2`.  The Sq1 ambiguity annihilates reductions of integral cycles.

Finally finite-type rational acyclicity makes H15 integral torsion.
Its UCT annihilator inside H15(F2) is `Ext(H14(Z),F2)`, which is
exactly the image of reduction of integral H15.  Thus the stated
equivalence for ALL integral cycles is correct; it is not a claim
that these cycles are all stably spherical.

No gap or mathematical correction was found.  The draft's
Halperin--Lemaire citation key was already being repaired by root.
The independently saved ordinary-cone proof of survival through
dimension fourteen is in `EH5_l4_fourteen_skeleton.md`.
