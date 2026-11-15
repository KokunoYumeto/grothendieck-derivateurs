# dump_classes.py -- save one representative table for each class (iso + anti-iso) of monoids of order n
import sys, numpy as np
from catlib import enum_tables
from enum_monoids import canon_classes
n = int(sys.argv[1])
tabs, nodes = enum_tables(n, 1, [0] * n, [0] * n, maxsol=400000)
reps, best = canon_classes(tabs.astype(np.int64))
idx = sorted(reps.values())
np.save("monoid_classes_order%d.npy" % n, tabs[idx])
print(n, len(tabs), len(idx))
