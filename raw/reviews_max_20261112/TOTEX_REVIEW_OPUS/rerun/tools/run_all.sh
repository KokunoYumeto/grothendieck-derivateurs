#!/bin/sh
# Rerun every mathematical program of the TOTEX return, sequentially, with python -I.
R="$1"; cd "$R" || exit 1
run() { out="$1"; shift; echo "=== $out: $*" >> out/RUNLOG.txt; /usr/bin/env python -I tools/run_isolated.py "$@" > "out/$out" 2>> out/RUNLOG.txt; echo "exit $?" >> out/RUNLOG.txt; }
: > out/RUNLOG.txt
run basic_shape_checks.stdout code/basic_shape_checks.py
run examples_colored_words.stdout code/examples_colored_words.py
run examples_support_orbits.stdout code/examples_support_orbits.py
run examples_affine_base.stdout code/examples_affine_base.py
run main_sign_reflection_check.json code/main_sign_reflection_check.py
run main_counterexample.out code/pretot_audit/main_counterexample.py
run independent_certificate_audit.out code/pretot_audit/audit_certificate.py
run semisimplicial_affine_checks.stdout code/pretot_audit/semisimplicial_affine_checks.py
run akr_stages.out code/akr_stages.py --partial-k2
run akr_stages_triple.out code/akr_stages.py --triple --verify-field
run akr_stages_literal.out code/akr_stages.py --literal-common-n --partial-k2
run akr_stages_triple_literal.out code/akr_stages.py --literal-common-n --triple
run akr_component_checks.out code/akr_component_checks.py
run akr_stages_critical.out code/akr_stages.py --critical-k3
echo ALLDONE >> out/RUNLOG.txt
