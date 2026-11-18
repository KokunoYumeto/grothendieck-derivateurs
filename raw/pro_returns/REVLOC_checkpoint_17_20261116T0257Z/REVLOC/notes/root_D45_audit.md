# Root audit of D.2.45

15 November 2026, 23:36 UTC. The complete final TeX was read and
independently audited by the fibrations agent. Result: passes in its
stated scope. The full target integral square and stable-spherical
pairing remain unevaluated.

The comparison operation is the actual stable James–Hopf map used
in D.2.43. Root opened Klein, arXiv:2603.07854v3, Theorem A(iii)
and its proof on printed pp.12–13, and Theorem B with its proof on
pp.13–16. The latter identifies the invariant with the Segal–Snaith
projection; equality of vaguely similar obstruction operations is
not assumed. For a stable sphere map its transfer is minus the
reduced diagonal of its integral Hurewicz class.

Root checked the tensor differential integrally. Its degree-fifteen
homology is Z/4{ab+ba} plus Z/2{ar,ra}. The resolution norm sends
c to ab+ba and u to ar+ra; the complete kernel from Z/8 plus Z/2
is <4c>. code/D45_integral_transfer.py independently checks the
integral cycles and boundary relations, all16 source elements and
all256 addition pairs. Its output is PASS and explicitly does not
compute the full-target diagonal or stable Hurewicz image.

A skeleton of dimension at most14 has H15=0, so every James–Hopf
value lies in <4c>. This excludes2c and proves survival of its
actual boundary. The original order four can decrease to two.
The15-skeleton induces an isomorphism on pi14 and surjects onto
pi15 of the full suspension spectrum; the quadratic group is
already unchanged. Naturality therefore gives equality of the
James–Hopf images. No unsupported calculation of individual12,
13 or14-cell composites is used.

Root checked the four independent James words in the low mod-two
Adams–Hilton comparison. Cubic terms start at18, so all possible
quadratic degree13 terms are covered. This proves the actual
H7 times H8 product zero, while making no integral injectivity
claim. For integral cochains dA=4B and dC congruent to AB modulo2,
E=(AB-dC)/2 satisfies dE=2B squared. Thus beta_Z theta=x squared,
and the coefficient pairing on an integral cycle is twice the
theta pairing. Its Sq1 ambiguity annihilates integral reductions.
Finite positive integral homology gives the stated vanishing
implication. The UCT/Ext-surjectivity argument proves equivalence
for all integral cycles, not for the smaller stable-spherical
subgroup; that distinction is explicit.

Root read Thomas1959, Section2 formula(2.1), printed p.899, and
TheoremI with its proof in Section5, pp.904–906. The coefficient
map for the ordinary Postnikov square is1 to4 from Z/4 to Z/8;
it kills the needed even coefficient. It cannot replace the
half-product test. The source reproduction is not part of the
authored archive.

An independent geometric proof of fourteen-skeleton survival is
retained in notes/EH5_l4_fourteen_skeleton.md. Root checked the
Stiefel cell description in Morisugi–Mukai2000 printed p.523 and
the integral top-degree-one map of mapping cones. Mod-two duality
on V9,2 gives the required value2 modulo4. This proof does not
claim a converse or evaluate an actual fifteen-cell attachment.

Build and visual verification:232 pages,136 numbered rows
(120 Proved,12 Refuted,2 Open,2 separately qualified),113 printed
bibliography entries. Initial build:2 overfull boxes,1 above2pt,
maximum14.60222pt. Both were fixed. Final build:0 overfull,
0 above2pt,0 missing characters, no undefined citations. Root
rendered and read pages135–141,226,228,229,231,232 after the final
build, covering all new proof pages, their transitions, all changed
bibliography entries and the tail. They are legible and unclipped.
