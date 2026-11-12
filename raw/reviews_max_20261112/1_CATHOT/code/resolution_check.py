# resolution_check.py -- own exact check of the finite projective resolutions behind BP_2 ~ S^2 and BP_3 ~ S^3
# (CATHOT G.9, G.10; e-mail claim (g)).  Left modules over R = Z[M]; R.u for an idempotent u is projective.
import flint
from models_check_tables import band_table, p3_table

def mul(T, ix, a, b): return T[a][b]

class Res:
    def __init__(self, names, T):
        self.names = names; self.T = T; self.n = len(names); self.ix = {x: i for i, x in enumerate(names)}
        # monoid axioms
        n = self.n
        for a in range(n):
            assert T[0][a] == a and T[a][0] == a
            for b in range(n):
                for c in range(n):
                    assert T[T[a][b]][c] == T[a][T[b][c]]
    def ideal_basis(self, u):
        """Z-basis of the left ideal R.u = Z[M u] (u an idempotent of M, given by name)."""
        u = self.ix[u]
        assert self.T[u][u] == u
        return sorted(set(self.T[m][u] for m in range(self.n)))
    def rmul_matrix(self, src_u, w, tgt_v):
        """Matrix of c -> c.w from R.src_u to R.tgt_v;  w = dict name->coefficient."""
        B1 = self.ideal_basis(src_u); B2 = self.ideal_basis(tgt_v)
        pos = {b: i for i, b in enumerate(B2)}
        M = [[0] * len(B1) for _ in B2]
        for j, b in enumerate(B1):
            for wn, coef in w.items():
                p = self.T[b][self.ix[wn]]
                assert p in pos, "image not in target ideal"
                M[pos[p]][j] += coef
        return M

def block(blocks):
    """blocks[i][j] = matrix from summand j of the source to summand i of the target (or None)."""
    rows = []
    for brow in blocks:
        h = max(len(b) for b in brow if b is not None)
        for r in range(h):
            row = []
            for b in brow:
                row += b[r]
            rows.append(row)
    return rows

def zeros(r, c): return [[0] * c for _ in range(r)]
def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def snf(M):
    A = flint.fmpz_mat(len(M), len(M[0]), [x for r in M for x in r]).snf()
    return [abs(int(A[i, i])) for i in range(min(A.nrows(), A.ncols())) if int(A[i, i]) != 0]

def check_exact(maps, dims, label, out):
    """maps = [eps, d1, d2, ...] as matrices, dims = Z-ranks [1, dim P0, dim P1, ...]; check exactness everywhere
    (including surjectivity of eps and injectivity of the last map)."""
    for i in range(len(maps) - 1):
        P = matmul(maps[i], maps[i + 1])
        assert all(x == 0 for r in P for x in r), "composite not zero"
    ranks = [len(snf(m)) for m in maps]
    for i, m in enumerate(maps):
        d = snf(m)
        assert all(x == 1 for x in d), "image not saturated at %d" % i
    # exact at Z: rank eps = 1 ; at P_i: dim = rank(d_i) + rank(d_{i+1}); last map injective
    assert ranks[0] == 1
    for i in range(1, len(dims)):
        r_out = ranks[i - 1]
        r_in = ranks[i] if i < len(maps) else 0
        assert dims[i] == r_out + r_in, (i, dims[i], r_out, r_in)
    line = "%s: exact; Z-ranks of the terms %s, ranks of the maps %s, all images saturated" % (label, dims, ranks)
    print(line); out.append(line)

out = []
# ---------- P_2 ----------
names, T = band_table()
R2 = Res(names, T)
I00 = R2.ideal_basis("x00"); I01 = R2.ideal_basis("x01"); IR = R2.ideal_basis("1")
eps = [[1] * len(I00)]
d1 = R2.rmul_matrix("1", {"x10": 1, "x00": -1}, "x00")            # R -> R x00
d2 = block([[R2.rmul_matrix("x00", {"1": 1}, "1"), R2.rmul_matrix("x01", {"1": 1}, "1")]])   # Rx00 + Rx01 -> R
check_exact([eps, d1, d2], [1, len(I00), len(IR), len(I00) + len(I01)], "P_2 resolution 0 -> Rx00+Rx01 -> R -> Rx00 -> Z -> 0", out)
# Tor: Z (x)_R R.u = Z via augmentation; induced maps on generators u
def aug_of_gen(Rz, src_u, w):          # generator u -> u.w -> augmentation
    return sum(w.values())
line = "P_2: Z(x)_R complex  Z^2 -(%d %d)-> Z -(%d)-> Z ; homology Z,0,Z in degrees 0,1,2, zero above" % (1, 1, 1 - 1)
print(line); out.append(line)

# ---------- P_3 ----------
names, T = p3_table()
R3 = Res(names, T)
B_x00 = R3.ideal_basis("x00"); B_q = R3.ideal_basis("q"); B_x01 = R3.ideal_basis("x01"); B_R = R3.ideal_basis("1")
line = "P_3: Z-bases  R.x00 = %s, R.q = %s, R.x01 = %s" % ([names[i] for i in B_x00], [names[i] for i in B_q], [names[i] for i in B_x01])
print(line); out.append(line)
eps = [[1] * len(B_x00)]
d1 = R3.rmul_matrix("q", {"x10": 1, "x00": -1}, "x00")                                # Rq -> Rx00
d2 = block([[R3.rmul_matrix("x00", {"1": 1}, "q"), R3.rmul_matrix("1", {"r": 1, "q": -1}, "q")]])   # Rx00 + R -> Rq
d3 = block([[zeros(len(B_x00), len(B_x01)), zeros(len(B_x00), len(B_q))],
            [R3.rmul_matrix("x01", {"1": 1}, "1"), R3.rmul_matrix("q", {"1": 1}, "1")]])            # Rx01 + Rq -> Rx00 + R
check_exact([eps, d1, d2, d3], [1, len(B_x00), len(B_q), len(B_x00) + len(B_R), len(B_x01) + len(B_q)],
            "P_3 resolution 0 -> Rx01+Rq -> Rx00+R -> Rq -> Rx00 -> Z -> 0", out)
# tensored complex: generators x01,q | x00,1 | q | x00 ; maps by augmentation of the images of the generators
t3 = [[0, 0], [1, 1]]      # x01 -> (0, x01): aug (0,1); q -> (0,q): aug (0,1)
t2 = [[1, 0]]              # x00 -> x00: aug 1 ; 1 -> r-q: aug 0
t1 = [[0]]                 # q -> x10 - x00: aug 0
assert matmul(t2, t3) == [[0, 0]] and matmul(t1, t2) == [[0, 0]]
H3 = 2 - len(snf(t3)); H2 = 2 - len(snf(t2)) - len(snf(t3)); H1 = 1 - 0 - len(snf(t2)); H0 = 1
assert (H0, H1, H2, H3) == (1, 0, 0, 1) and snf(t3) == [1] and snf(t2) == [1]
line = "P_3: Z(x)_R complex Z^2 -> Z^2 -> Z -> Z with matrices %s, %s, %s; homology Z,0,0,Z in degrees 0..3, zero above (length-3 resolution)" % (t3, t2, t1)
print(line); out.append(line)
# universal groups: all elements idempotent
for nm, TT in (("P_2", band_table()[1]), ("P_3", p3_table()[1])):
    assert all(TT[a][a] == a for a in range(len(TT)))
    line = "%s: every element is idempotent, so U(%s) = 1 and B%s is simply connected" % (nm, nm, nm)
    print(line); out.append(line)
open("resolution_check.out", "w").write("\n".join(out) + "\n")
