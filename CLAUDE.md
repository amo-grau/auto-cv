# auto_cv

LaTeX sources for Oscar Amo Grau's CV and motivation letter, plus per-application
tailored versions.

This repository is the source of truth for both documents. They are edited here,
not anywhere else.

## Layout

Every document is a directory containing a `main.tex`.

```
profile/                the inventory — everything, uncut, no page limit
  experience.md  education.md  projects.md  skills.md
  learning.md    activities.md
  _gaps.md              open questions about existing entries
base/                   default one-page rendering of the inventory
  cv/main.tex
  letter/               main.tex + info.tex (variables) + body.tex (prose) + sig.jpg
applications/
  <company>-<role>/     one directory per job application
    offer.md            the job posting, pasted verbatim
    notes.md            what was changed and why
    cv/
    letter/
build.sh                latexmk wrapper
```

`applications/` is gitignored in full — it is local-only and never pushed.

## The inventory is the content source of truth

`profile/` holds everything Oscar has done, at full length, with no page limit.
`base/cv/` is not the master list — it is one *selection* from `profile/`, sized to
one page. A tailored CV is a different selection from the same inventory.

```
profile/            everything, uncut          <- new facts land here first
  ↓ select
base/cv/            default one-pager
  ↓ select + reorder
applications/…/cv/  one-pager for one posting
```

This is what makes the one-page limit safe: content cut from a CV is not lost, it
is simply not selected this time, and it can return for the next posting that
rewards it. **Never delete an entry from `profile/` for being irrelevant today.**

Every entry carries `Tags:` — lowercase keywords. Matching a posting against those
tags is the first step of selection, not a substitute for judgement.

The letter splits cleanly: `info.tex` holds the per-application variables
(`\company`, `\position`, `\team`, `\city`, `\recipient`) and `body.tex` holds the
prose. Tailoring a letter is mostly editing those two files.

---

# The five modes

Work in this repo falls into five modes. Identify which one the request is before
acting; if genuinely ambiguous, ask.

## 1. Bootstrap — build the documents from scratch

Trigger: the base documents are empty, being rebuilt, or a whole section has no
content yet.

Fill `profile/` first by **interviewing Oscar**, then render `base/` from it. Do
not write placeholder content and do not guess. Rules for the interview:

- Ask about one section at a time; do not dump twenty questions at once.
- **Insist on specifics.** A first answer is almost always too vague to use. If he
  says "worked on a vision system", push for: which models, which language, which
  hardware, how many, how fast, deployed or prototype, who used it, what changed
  because of it. Keep pushing until the bullet could not have been written by
  someone who did not do the work.
- Chase numbers. Throughput, latency, team size, number of deployments, percentage
  improvement, duration. A bullet with a number beats three without.
- If he cannot answer, drop the claim rather than softening it into vagueness.
- Confirm dates, employer names, job titles and locations exactly as they should
  appear.

Write nothing into the documents that did not come from his answers.

## 2. Template and ATS optimization

Trigger: a request to improve how the documents are structured or how well they
survive automated screening.

Most companies run applications through automated screening — keyword matchers,
CV parsers, and increasingly LLM-based filters. The document must survive being
reduced to plain text. Concretely:

- **The check that decides everything:** `pdftotext -layout <pdf> -`. What that
  prints is roughly what the filter reads. Run it after any structural change and
  actually read the output. If a heading, date or contact detail is missing,
  garbled, or out of order there, the filter sees the same damage.
- Keep `\pdfgentounicode=1` in the CV so glyphs map back to real characters.
- Use **standard section headings** — Experience, Education, Skills, Projects.
  Parsers match on these literally; inventive headings get dropped.
- Dates must be unambiguous and consistent across the document.
- No text inside images, no multi-column layout, no text boxes, no critical
  information in headers or footers — parsers routinely discard all of these.
- Avoid hyphenation across line breaks in prose: a keyword split as `de-veloping`
  no longer matches `developing`. The CV is `\raggedright` so it is safe; the
  letter is justified and does hyphenate.
- Icon fonts (`fontawesome5`) do not extract as text. Anything encoded only as an
  icon — an email or phone next to an envelope glyph — must also be present as
  plain text.
- Spell out an acronym once alongside its expansion where a filter might match
  either form.
- Structural changes belong in `base/`. Never restructure a single application's
  copy and leave `base/` behind.

## 3. Specialized job applications

Trigger: Oscar sends a job posting.

1. Create `applications/<company>-<role>/` and save the posting verbatim to
   `offer.md`.
2. `cp -r base/cv base/letter applications/<company>-<role>/`.
3. **Re-select from `profile/`, do not merely trim `base/`.** Read the posting,
   match it against the inventory's tags and entries, and decide what earns a
   place on this particular page. An entry absent from `base/cv/` may well belong
   on this one — `activities.md` and the deeper bullets in `experience.md` exist
   precisely for that.
4. Tailor the wording (rules below).
5. `./build.sh applications/<company>-<role>`, check the page counts, and read the
   `pdftotext` output.
6. Record in `notes.md` what changed and why — including what was pulled in from
   `profile/` and what was dropped.

Tailoring rules:

- **Never invent or inflate.** No experience, tool, employer, date, or metric that
  isn't already in `base/` or confirmed by Oscar. Tailoring means selecting,
  reordering, and rephrasing what is true — nothing else.
- Mirror the posting's own vocabulary where it honestly describes existing work
  (posting says "computer vision", the bullet says "vision-based AI models" —
  align them).
- Reorder and prune bullets so the most relevant come first; drop the least
  relevant rather than adding new ones.
- Reorder the Skills lists to lead with what the posting asks for. Do not add a
  skill just because the posting names it.
- **The CV must stay on one page.** `build.sh` prints the page count of every PDF.
- The letter is one page. Always set `\company` and `\position`; set `\team` and
  `\recipient` only when the posting actually names them.
- If the posting demands something Oscar genuinely lacks, say so plainly rather
  than papering over it.

`base/` is never edited to fit a posting.

## 4. Info updates

Trigger: something changes in real life — a new role or promotion, a shipped
project, a finished course, a book read, a new tool used seriously.

- **It goes into `profile/` first, always.** The inventory has no page limit, so
  record it at full length with tags — even if it will not make the CV today.
- Ask the same specific questions as mode 1 before writing the entry. A new line
  earns its place with detail, not with its existence.
- Convert relative dates ("last month") to absolute ones before writing them down.
- Then decide separately whether it displaces something in `base/cv/`. It often
  should not, and that is fine — it is safely recorded either way.
- **The CV is one page, so every addition to it forces a removal.** Say what you
  propose to cut and why; do not silently spill onto a second page. What is cut
  remains in `profile/`.
- If the new fact answers something in `profile/_gaps.md`, delete that question.
- The letter changes far less often. Update it only when the new fact changes the
  story it tells — a new job, a change of field. A finished course does not.
- Rebuild afterwards and confirm both documents still fit on one page.

## 5. Feedback on existing content

Trigger: asked for feedback, or a weakness is noticed while doing something else.
Offer it unprompted when it matters, but keep it short and do not derail the task
at hand.

Look for and say plainly:

- Content that no longer earns its space: old, minor, or irrelevant to the roles
  being targeted now.
- Bullets that describe responsibilities instead of outcomes, or that carry no
  concrete detail.
- Missing numbers where a number would obviously exist.
- Long undifferentiated lists — a wall of items reads as filler and dilutes the
  strong entries.
- Anything ambiguous, unexplained, or dated in a way a reader outside the field
  would not follow.
- Gaps and inconsistencies: unexplained date gaps, tense drift, inconsistent
  formatting between entries.

Be direct and concrete: name the line, say why it is weak, propose the
replacement. Do not soften feedback into uselessness — but do not rewrite content
in `base/` or `profile/` on the strength of an opinion alone. Propose, then let
Oscar decide.

`profile/_gaps.md` is the standing form of this mode: every unanswered question
there is feedback already given. Keep it current, raise items from it when they
become relevant, and prefer asking one well-aimed question over listing ten.

---

## Rules that hold in every mode

- **Truthfulness is absolute.** Never add a skill, tool, employer, date, metric or
  claim that Oscar has not confirmed. This applies to bootstrap, tailoring and
  updates alike, and to `profile/` as much as to the rendered documents.
- New facts enter through `profile/`, never straight onto a CV.
- The CV is one page. The letter is one page.
- After any change, rebuild and read the extracted text — not just the page count.
- Nothing company-specific ever enters `base/`.

## Compiling

```bash
# once
sudo apt install -y texlive-latex-extra texlive-fonts-recommended \
                    texlive-fonts-extra latexmk
./build.sh                              # everything in base/
./build.sh applications/<company>-<role>
pdftotext -layout base/cv/build/main.pdf -   # read what a filter reads
```

`texlive-fonts-extra` is needed for the letter's `fontawesome5` icons.

## What must never be published

`applications/` is gitignored in full, and so is every PDF and `sig.jpg` (the
handwritten signature). Job postings, the companies applied to, the documents
actually sent, and the signature are private and stay out of git history. Never
commit them, never move company-specific content into `base/`, and never name a
target company in `base/` — `\company`, `\city`, `\team` and `\position` are
deliberately blank there.

The remote is public. `git push` uses the `github.com-personal` SSH alias.

The letter wraps its `\includegraphics{sig.jpg}` in `\IfFileExists` so a clone
without the signature still compiles. Keep that guard.
