French correction decision fixtures

These ten reviewed JSON files are applied in this order: manual.json, then the manual_*.json files in lexicographic order. A later entry for the same source row replaces an earlier one. MANIFEST.json records each fixture hash and byte count.

Source-row identifiers refer to 1-based data rows in the supplied companion_corrections CSV files. Direct edit coordinates are Python Unicode character offsets in the original transcription unit, before any correction or build repair. Each before string must match that original source exactly.

To replay in the build workspace, extract the original French ZIP under work/fr and run python output/records/scripts/resolve_french.py. The script uses work/corrections_fr/manual*.json when present; otherwise it uses these packaged fixtures. It never changes the original source units. Run python output/records/scripts/validate_french_plan.py to reproduce the preservation and coverage audit.

The plan contains only actual variants. No-change and rejected proposals remain in the complete coverage and decision tables. Duplicate source-place corrections share one variant with all contributing source-row identifiers.
