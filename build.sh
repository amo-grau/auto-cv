#!/usr/bin/env bash
# Compile every main.tex under a path into <its dir>/build/main.pdf
#
#   ./build.sh                          # compiles base/cv and base/letter
#   ./build.sh base/cv                  # just the CV
#   ./build.sh applications/<name>      # both documents of one application
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="${1:-base}"

if ! command -v latexmk >/dev/null 2>&1; then
  echo "latexmk not found. Install the toolchain with:" >&2
  echo "  sudo apt install -y texlive-latex-extra texlive-fonts-recommended \\" >&2
  echo "                      texlive-fonts-extra latexmk" >&2
  exit 1
fi

[ -e "$ROOT/$TARGET" ] || [ -e "$TARGET" ] || { echo "No such path: $TARGET" >&2; exit 1; }

mapfile -t docs < <(find "$ROOT/$TARGET" -name main.tex -not -path '*/build/*' | sort)
[ ${#docs[@]} -gt 0 ] || { echo "No main.tex found under $TARGET" >&2; exit 1; }

status=0
for tex in "${docs[@]}"; do
  dir="$(dirname "$tex")"
  echo ">> ${dir#"$ROOT"/}"
  # Run inside the document's own directory so \input{} and \includegraphics
  # resolve against it rather than against the repo root.
  if ( cd "$dir" && latexmk -pdf -interaction=nonstopmode -halt-on-error \
                            -outdir=build main.tex >/dev/null ); then
    pages="$(pdfinfo "$dir/build/main.pdf" 2>/dev/null | awk '/^Pages:/{print $2}')"
    echo "   ok  -> ${dir#"$ROOT"/}/build/main.pdf (${pages:-?} page(s))"
  else
    echo "   FAILED - see ${dir#"$ROOT"/}/build/main.log" >&2
    status=1
  fi
done
exit $status
