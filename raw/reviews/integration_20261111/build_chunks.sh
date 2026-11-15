#!/bin/bash
# Rebuild and compile the chunk readers named on the command line (ids such as XVI XIIb-a), as the companion's build
# does: kit/build_reader.py, then LuaLaTeX, BibTeX, LuaLaTeX twice. One chunk at a time. Output: build_<id>.txt here.
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
for id in "$@"; do
  d="$ROOT/checks/DER_$id"
  out="$HERE/build_$id.txt"
  cd "$d" || { echo "$id: no folder"; continue; }
  [ -f derivateurs_companion.sty ] || cp "$ROOT/kit/derivateurs_companion.sty" .
  if ! python -I "$ROOT/kit/build_reader.py" "DER_$id" . > "$out" 2>&1; then echo "$id: build_reader FAILED"; cat "$out"; continue; fi
  lualatex -interaction=nonstopmode "DER_${id}_reader.tex" >> "$out" 2>&1
  bibtex "DER_${id}_reader" >> "$out" 2>&1
  lualatex -interaction=nonstopmode "DER_${id}_reader.tex" >> "$out" 2>&1
  lualatex -interaction=nonstopmode "DER_${id}_reader.tex" > "$HERE/build_${id}_last.txt" 2>&1
  err=$(grep -c '^!' "$HERE/build_${id}_last.txt")
  und=$(grep -c 'undefined' "$HERE/build_${id}_last.txt")
  pages=$(grep -o 'Output written on .*' "$HERE/build_${id}_last.txt")
  echo "$id: errors=$err undefined-warnings=$und $pages"
  grep -A3 '^!' "$HERE/build_${id}_last.txt" | head -40
  grep 'undefined' "$HERE/build_${id}_last.txt" | head -10
done
