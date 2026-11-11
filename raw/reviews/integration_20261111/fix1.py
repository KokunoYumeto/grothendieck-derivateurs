import sys
sys.stdout.reconfigure(encoding='utf-8')
p = 'new_XIIb-a.tex'
s = open(p, encoding='utf-8').read()


def rep(a, b, cnt=1):
    global s
    assert s.count(a) == cnt, (s.count(a), a[:60])
    s = s.replace(a, b)


rep(r"""A final functor induces a bijection on connected components and, by the argument with coverings at ms.~101, a surjection on fundamental groups. If $H$ is totally $W_0$-aspherical, the test $p=\mathrm{id}$ shows that $U/H$ is nonempty and connected, and then so is every final image of $U/H$; the same reasoning applies to $W_1$ with ``simply connected''.""",
    r"""A final functor induces a bijection on connected components, and a final image of a $1$-connected category is $1$-connected (the argument with coverings at ms.~101). If $H$ is totally $W_0$-aspherical, the test $p=\mathrm{id}$ shows that $U/H$ is nonempty and connected, and then so is every final image of $U/H$; for $W_1$ the same reasoning applies with $1$-connectedness.""")

rep(r"""A chain of arrows of $P_A$ either lies in $A$, or lies in $T_1$, or consists of a chain in $A/c$ followed by a chain in $T_1$ together with one of the two labels. Hence
\[
 NP_A=NA\ \cup\ \bigl(N(A/c)*NT_1\bigr)_\alpha\ \cup\ \bigl(N(A/c)*NT_1\bigr)_\beta ,
\]
where $*$ is the join, the two joins meet in $N(A/c)\amalg NT_1$, and each meets $NA$ in $N(A/c)$. A functor $h:A\to A'$ under $U$ induces maps of all these pieces. The categories $A/c$ and $A'/h(c)$ have terminal objects, so the maps of joins and of their intersections are weak equivalences whatever $h$ is; if $h\in W_\infty$, the map $NP_A\to NP_{A'}$ is a weak equivalence by the gluing lemma for unions of simplicial sets. For $W_R$ one uses the Mayer--Vietoris sequences of the same unions.\hfill$\square$""",
    r"""A chain of arrows of $P_A$ either lies in $A$, or lies in $T_1$, or consists of a chain in $A$, a crossing arrow $(g,\lambda)$ with $\lambda\in\{\alpha,\beta\}$, and a chain in $T_1$; the chain in $A$ together with $g$ is a chain of $A/c$. Write $J=N(A/c)*NT_1$ for the join, and $J_\alpha\cup J_\beta$ for two copies of $J$ glued along $NT_1$. Then $NP_A$ is the pushout of simplicial sets
\[
 NA\longleftarrow N(A/c)\amalg N(A/c)\hookrightarrow J_\alpha\cup J_\beta ,
\]
in which the left map forgets the arrow to $c$ and the right map is a monomorphism; it is therefore a homotopy pushout. A functor $h:A\to A'$ under $U$ induces a map of these diagrams. The categories $A/c$ and $A'/h(c)$ have terminal objects, so their nerves and the joins $J$ are contractible, and the maps on $N(A/c)\amalg N(A/c)$ and on $J_\alpha\cup J_\beta$ are weak equivalences whatever $h$ is. If $h\in W_\infty$, the map $NP_A\to NP_{A'}$ is then a weak equivalence. For $W_R$ one uses the Mayer--Vietoris sequences of the same pushouts.\hfill$\square$""")

rep(r"""\textit{Let $U\hookrightarrow X$ be a sieve whose complement is one object $t$ with only its identity, and $H=\operatorname{Hom}_X(-,t)|_U$. For a nonzero commutative ring $R$, the inclusion is a trivial $W_R$-cofibration if and only if $H$ is totally $W_R$-aspherical, that is, if and only if it is $W_R$-dwy\'erienne.}""",
    r"""\textit{Let $U\hookrightarrow X$ be a sieve whose complement is one object $t$ with only its identity, and suppose that $H=\operatorname{Hom}_X(-,t)|_U$ is not empty. For a nonzero commutative ring $R$, the inclusion is a trivial $W_R$-cofibration if and only if $H$ is totally $W_R$-aspherical, that is, if and only if it is $W_R$-dwy\'erienne.}""")

rep(r"""By the one-point formula (commentary at ms.~85 and on Chapter~II, ms.~36bis), $B(X\amalg_UA)$ is the mapping cone of $B(A/p_!H)\to BA$; if $A/p_!H$ is empty the cone adds a disjoint point. The inclusion of $BA$ is an $R$-homology isomorphism exactly when $A/p_!H$ is nonempty with the $R$-homology of a point.""",
    r"""A chain of arrows of $X\amalg_UA$ that does not lie in $A$ is a chain of $A/p_!H$ followed by $t$, so $N(X\amalg_UA)$ is $NA$ with the cone on $N(A/p_!H)$ attached along the forgetful map, and $B(X\amalg_UA)$ is the mapping cone of $B(A/p_!H)\to BA$. The inclusion of $BA$ is an $R$-homology isomorphism exactly when the reduced $R$-homology of $A/p_!H$ vanishes, that is, when $A/p_!H$ has the $R$-homology of a point.""")

rep(r"\textbf{Theorem (immersions for $W_\infty$ and for homology).}\ours",
    r"\textbf{Theorem (total immersions for $W_\infty$).}\ours")

rep(r"""The same proof works for $W_R$, with ``$R$-acyclic'' in place of ``weakly contractible''. For the strict class the situation is as follows. $W_R$-dwy\'erienne sieves are stable under composition (the restriction of a totally $W_R$-aspherical presheaf to a cosieve on which it is nonempty is totally $W_R$-aspherical, after which part~(a) applies; we do not reproduce the proof of the restriction statement). For $W_\infty$ the question is undecided; it is equivalent to the question left open in the commentary at ms.~111, whether a presheaf all of whose direct images have integrally acyclic categories of elements has only weakly contractible ones.""",
    r"""The same proof works for the homology localizers $W_R$, with the homological form of the criterion ($R$-acyclic in place of weakly contractible). For the strict class, the $W_R$-dwy\'erienne sieves are also stable under composition: the restriction of a totally $W_R$-aspherical presheaf to a cosieve on which it is nonempty is totally $W_R$-aspherical, after which part~(a) applies; the proof of the restriction statement is not reproduced here. For $W_\infty$-dwy\'erienne sieves the question is undecided. It comes down to the question left open in the commentary at ms.~111: does a presheaf all of whose direct images have integrally acyclic categories of elements have only weakly contractible ones?""")

a = s.index(r"\begin{dcomment}{development}{p114}{The endpoint product is not a cofibration}")
s = s[:a] + open('endpoint_block.tex', encoding='utf-8').read()
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print(s.count(r'\begin{dcomment}'), s.count(r'\end{dcomment}'))
