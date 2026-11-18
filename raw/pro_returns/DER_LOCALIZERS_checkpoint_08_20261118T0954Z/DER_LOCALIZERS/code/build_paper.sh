#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")/.."
mkdir -p build
lualatex -interaction=nonstopmode -halt-on-error -output-directory=build DER_LOCALIZERS_paper.tex
bibtex build/DER_LOCALIZERS_paper
lualatex -interaction=nonstopmode -halt-on-error -output-directory=build DER_LOCALIZERS_paper.tex
lualatex -interaction=nonstopmode -halt-on-error -output-directory=build DER_LOCALIZERS_paper.tex
cp build/DER_LOCALIZERS_paper.pdf DER_LOCALIZERS_paper.pdf
