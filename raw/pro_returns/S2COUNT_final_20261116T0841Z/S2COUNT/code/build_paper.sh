#!/usr/bin/env bash
set -euo pipefail
# Standard build; this environment additionally needs its absent format/database
# regenerated in a writable directory. No system files are changed.
task_root=$(cd "$(dirname "$0")/.." && pwd)
task_tex_runtime=${S2COUNT_TEX_RUNTIME:-"$task_root/../tex_runtime"}
mkdir -p "$task_root/logs" "$task_tex_runtime/var" "$task_tex_runtime/config" "$task_tex_runtime/cache"
mkdir -p "$task_tex_runtime/fonts/map/pdftex"
# The image contains the Type 1 fonts but no generated font map.  Build a
# private map; LuaLaTeX can use these fonts without the optional luaotfload.
if [ ! -f "$task_tex_runtime/fonts/map/pdftex/pdftex.map" ]; then
  cat /usr/share/texmf/fonts/map/dvips/lm/lm.map \
      /usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/*.map \
      > "$task_tex_runtime/fonts/map/pdftex/pdftex.map"
fi
export TEXMF="{$task_tex_runtime,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
export TEXMFVAR="$task_tex_runtime/var"
export TEXMFCONFIG="$task_tex_runtime/config"
export TEXMFCACHE="$task_tex_runtime/cache"
if [ ! -f "$task_tex_runtime/lualatex.fmt" ]; then
  (cd "$task_tex_runtime" && luahbtex --ini --interaction=nonstopmode --jobname=lualatex \
    /usr/share/texlive/texmf-dist/tex/latex/tex-ini-files/lualatex.ini > format_build.stdout)
fi
cd "$task_root"
export TEXFORMATS="$task_tex_runtime:"
lualatex -interaction=nonstopmode -halt-on-error S2COUNT_paper.tex > logs/build_pass1.stdout
bibtex S2COUNT_paper > logs/bibtex.stdout
lualatex -interaction=nonstopmode -halt-on-error S2COUNT_paper.tex > logs/build_pass2.stdout
lualatex -interaction=nonstopmode -halt-on-error S2COUNT_paper.tex > logs/build_pass3.stdout
cp S2COUNT_paper.log logs/build_final.log
