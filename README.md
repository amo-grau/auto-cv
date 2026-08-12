# auto_cv

My CV and motivation letter in LaTeX, and the machinery to tailor them to a
specific job posting without rewriting either from scratch.

The idea: `base/` holds one honest, complete version of each document. Every
application gets a copy that is trimmed and reordered for that posting — the same
facts, told in the order that particular employer cares about.

## Layout

Each document is a directory with a `main.tex` inside it.

```
base/
  cv/main.tex        the CV — one page, ATS-parsable, no images
  letter/            the motivation letter
    main.tex           layout (do not edit per application)
    info.tex           who I am + who I'm writing to
    body.tex           the prose
    sig.jpg            scanned signature (gitignored — see Privacy)
applications/         one directory per application — local only, never pushed
build.sh              compiles main.tex files to PDF
```

`base/` changes only when something changes in real life: a new role, a new
skill, a course finished. It is never bent to fit a particular posting.

## Setup

```bash
sudo apt install -y texlive-latex-extra texlive-fonts-recommended \
                    texlive-fonts-extra latexmk
```

`texlive-fonts-extra` supplies `fontawesome5`, used for the letter's contact icons.

## Building

```bash
./build.sh                          # everything under base/
./build.sh base/cv                  # one document
./build.sh applications/<name>      # one application
```

PDFs land in `<document dir>/build/main.pdf`. The script prints the page count of
each one, since both documents are meant to be a single page.

## Applying to a job

1. Create `applications/<company>-<role>/` and drop the posting in as `offer.md`.
2. `cp -r base/cv base/letter applications/<company>-<role>/`.
3. Tailor the copies: reorder and prune, never invent.
4. `./build.sh applications/<company>-<role>`, check the page counts, send.

Step 3 is what Claude does — see [CLAUDE.md](CLAUDE.md) for the rules it follows.

## Privacy

`applications/`, all `*.pdf` files and `sig.jpg` are gitignored. Which companies I
apply to, what their postings say, what I sent them, and my handwritten signature
all stay on this machine. `base/` names no target company, so it is safe to push.

Because the signature is not in the repo, a fresh clone compiles the letter with
blank space where it belongs. Copy `sig.jpg` into `base/letter/` to restore it.
