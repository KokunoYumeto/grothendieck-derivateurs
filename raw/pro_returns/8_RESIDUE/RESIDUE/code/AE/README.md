# Reproducing Parts A and E computations

All computations are deterministic. The C++ enumerator requires a C++17 compiler; Python checks use Python 3 and SymPy.

Run from the root directory containing RESIDUE:

```sh
g++ -O3 -std=c++17 RESIDUE/code/AE/monoids.cpp -o RESIDUE/code/AE/monoids
RESIDUE/code/AE/monoids 2> RESIDUE/code/AE/monoids_run.txt
python RESIDUE/code/AE/monoid_classification.py > RESIDUE/code/AE/monoids_classification_run.txt
python RESIDUE/code/AE/path_chain.py > RESIDUE/code/AE/path_chain_run.txt
python RESIDUE/code/AE/chain_closure_check.py > RESIDUE/code/AE/chain_closure_check_run.txt
python RESIDUE/code/AE/relative_posets.py > RESIDUE/code/AE/relative_posets_run.txt
python RESIDUE/code/AE/verify_certificates.py > RESIDUE/code/AE/verification_run.txt
python RESIDUE/code/AE/core_fundamental_groups.py > RESIDUE/code/AE/core_fundamental_groups_run.txt
python RESIDUE/code/AE/complete_homotopy_table.py > RESIDUE/code/AE/complete_homotopy_table_run.txt
python RESIDUE/code/AE/transient_probe.py > RESIDUE/code/AE/transient_probe_run.txt
```

`relative_posets_homotopy_table.csv` concerns fixed alternating words (-,+)^n for n=1,2,3. It is not a table of the full Grothendieck subcategories on all word types of length at most six. The empty relative poset is included in the catalogue but has no endpoint rows. No bounded table is described as an unbounded comparison theorem.
