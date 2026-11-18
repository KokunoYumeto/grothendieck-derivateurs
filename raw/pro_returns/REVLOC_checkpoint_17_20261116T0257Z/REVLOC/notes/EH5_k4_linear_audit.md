# Independent audit of the fourth-suspension linear coefficient

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026. Independent audit of the root's finite Steenrod witness.

**PASS.** The argument below excludes the linear f coefficient for every
actual map Sigma⁵B->Sigma²B, where B=K(F2,2). It assumes no other
coefficient normalization and no multiplicativity of the map. This does
not by itself exclude the remaining commutator-only k pattern.

Let u,v,w,t,s be Serre's polynomial generators of degrees 2,3,5,9,17,
with v=Sq1u, w=Sq2v, t=Sq4w, and s=Sq8t. An actual map between
the indicated suspensions induces a degree-minus-three homomorphism

    phi: H~*(B;F2) -> H~*−3(B;F2)

commuting with every Steenrod square. A nonzero linear f coefficient is
exactly phi(u³)=v. Reduced H0 is zero. The following nine identities hold
in the source by Cartan and Adem:

    Sq4(u²)=u⁴;
    Sq3(uv)=vw+uv²;
    Sq2(u³)=u⁴+uv²;
    Sq6(v²)=v⁴;
    Sq4(vw)=vt+v⁴;
    Sq10(uvw)=u²v²w²;
    Sq9(ut)=vs+ut²;
    Sq8(vt)=vs;
    Sq4(uwt)=ut²+u²v²w².

Here is a direct check of the less immediate last three formulas.
Adem gives Sq5t=Sq6t=Sq7t=0 and Sq2t=Sq3t=Sq4t=0, while
Sq1t=w², Sq8t=s and Sq9t=t². Also Sq1w=v² and Sq2w=Sq3w=0.
Cartan on ut, vt, and uwt now gives precisely the displayed formulas.
The sixth formula is the top square because |uvw|=10.

Since phi(u²) lies in H1B=0, the first identity gives phi(u⁴)=0.
The second gives phi(vw)=phi(uv²), because phi(uv) lies in H2B
and its third square vanishes by instability. The third consequently
gives

    phi(uv²)=phi(vw)=w.

The fourth gives phi(v⁴)=0, since phi(v²) has degree3. The fifth
then gives coefficient_t phi(vt)=1: the degree-five basis is w,uv;
Sq4w=t, whereas Sq4(uv)=u²w+v³ is decomposable.

The sixth and seventh identities give

    phi(u²v²w²)=0,        phi(ut²)=phi(vs),

because Sq10 on degree7 and Sq9 on degree8 vanish by instability.
Taking the s coefficient in the ninth identity therefore gives

    coefficient_s phi(vs)=coefficient_s Sq4(phi(uwt))=0.

Indeed phi(uwt) has degree13, and B has no polynomial generator in
degree13. Every degree-thirteen class is decomposable. Cartan preserves
decomposability, since a positive-degree factor cannot acquire a scalar
term under a Steenrod operation. Thus its fourth square cannot contain
the indecomposable generator s.

But the eighth identity gives

    coefficient_s phi(vs)=coefficient_s Sq8(phi(vt))
                         =coefficient_t phi(vt)=1.

The last equality is exact on the whole degree-nine group: its basis is
u³v,u²w,v³,t; the first three are decomposable and cannot yield s,
whereas Sq8t=s. This contradiction proves the assertion.

Only the one fixed coefficient phi(u³)=v was used. The root subsequently
removed the extra fixed low rows from the search program and reran it;
the current file has a single fixed add call, for u³ mapping to v.
Every other coefficient is free. The root's refreshed trace certificate
in code/outputs/D2_k4_linear_module_24.json identifies precisely these
nine source-square equations and the one fixed coefficient.

The topological degree shift is exact: target cohomology Sigma²H^dB
pulls back to source Sigma⁵H^{d−3}B. Steenrod operations commute with
both suspensions. The relevant nonzero homology coefficient sends the
degree-three b label of the unit to the degree-six f label of B, dual
to u³, hence induces phi(u³)=v. There is no stable-to-unstable converse
being asserted.

Primary inputs are the already opened Serre1953 Section2 generator
calculation and the Steenrod Cartan/Adem/instability identities. No
new external theorem or higher homotopy-group calculation is needed.
