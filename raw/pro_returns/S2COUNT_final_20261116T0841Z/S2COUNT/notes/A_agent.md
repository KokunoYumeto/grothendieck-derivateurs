# Part A: independent structural proof

The six-element example is an instance of M_r, the rectangular band on
{0,1} x {0,1}, with identity and r extra elements y_j, all having the same
left and right multiplication as e=x00. Every product of two nonidentity
elements is the band element with row of the first and column of the second.

**Settled:** B M_r is homotopy equivalent to the wedge, for every word w
in the alphabet {1,...,r}, of S^{|w|+2}. In particular r=1 gives exactly
one sphere in every dimension at least 2, and r=2 gives 2^{n-2} spheres
in dimension n.

The proof has two independent ingredients:

1. Integral algebra: R=Z[M_r] has an integral basis e,u=1-e,a=x10-e,
   b=x01-e,c=x11-x10-x01+e,t_j=y_j-e. Its only radical product is ab=c.
   The two idempotents e,u are orthogonal. The relative bar over
   E=Ze+Zu has cycles b tensor t_w tensor a as a primitive integral
   homology basis. Interior paths are words in t_j,c and the two-letter
   token ab. The differential replaces ab with c, so the latter two
   tokens form a contractible pair and the tensor algebra retracts onto
   the words in the t_j. A short exact recursive projective resolution
   gives the same homology in all degrees.

2. Explicit spheres: let S^1 have two vertices and two directed edges,
   both from its first vertex to its second. Join it with n-1 two-point
   spaces to obtain S^n, with 2^n top simplices indexed by bit strings.
   Send a top simplex to the bar simplex whose entries are chosen,
   according to those bits, from (x01,e), (y_j1,e), ..., (y_jk,e),
   (x10,e), where n=k+2. Each interior adjacent product is e, so every
   face identification respects the map. The image fundamental cycle
   is exactly b tensor t_w tensor a. Wedge these sphere maps. They
   induce an integral homology isomorphism; both sides are simply
   connected; the homological Whitehead theorem applies.

The original exploratory cycle with first entry x10-x11 was discarded:
it is not the primitive basis cycle. No result uses that exploratory
choice. Correct endpoint differences are x01-e and x10-e.

Consequences: all positive-degree cup products over Z or any field are
zero, all positive-degree Steenrod operations vanish, every ordinary
triple Massey product of positive-degree classes is the singleton {0},
and phantom maps from B M_r to any target vanish. The explicit spheres
and a homotopy inverse supply a degree-one map to S^3 when r>=1.

Sources consulted: attached Sweeney arXiv:2502.05276v2, Examples 5.2
and 5.3; attached Ben-Bassat arXiv:2610.38760v1, introductory example,
main theorem and Karoubi conventions. The present proof does not use
Ben-Bassat's theorem. Literature search for rectangular-band inflation
classifying spaces found no source for this particular equivalence;
no priority claim is made. Web records for Sweeney:
https://arxiv.org/abs/2502.05276 and
https://arxiv.org/pdf/2502.05276v2 .
