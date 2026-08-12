---
name: bootstrap
description: Build a CV and cover letter from scratch for a new owner of this repository — wipe the previous person's data everywhere it lives, interview the new owner section by section, fill profile/ and both LaTeX documents, and compile. Use when someone has cloned this repo to make it their own, or when starting the documents over from nothing.
---

# Building from scratch for a new owner

Someone cloned this repository and wants their own CV and cover letter out of it.
The templates stay; every trace of the previous owner goes.

This is destructive. Read the whole skill before touching anything.

## Step 0 — Confirm, and warn about history

Ask outright: *"This replaces every piece of the previous owner's information. Go
ahead?"* Do not start on an implied yes.

Then tell them once, because they cannot fix it later as easily:

> This clone still contains the previous owner's CV data in its git history, and
> the remote it points at is not yours. Before pushing anywhere, either start a
> fresh history (`rm -rf .git && git init`) or point `origin` at your own empty
> repository. Check `git remote -v`.

Do not run those commands for them. Say it and let them decide.

## Step 1 — Wipe

Every location holding personal data. Missing one means the new CV silently
carries a stranger's details.

| What | Where | Action |
| --- | --- | --- |
| Identity record | `profile/owner.md` | rewrite completely |
| Career content | `profile/experience.md`, `education.md`, `projects.md`, `skills.md`, `learning.md`, `activities.md` | empty of entries, keep the headings and format |
| Open questions | `profile/_gaps.md` | clear — they belong to the old owner |
| CV header | `base/cv/main.tex` — name, phone, email, LinkedIn, GitHub | replace; **each link appears twice**, as URL and as visible text |
| CV body | `base/cv/main.tex` — Experience, Education, Professional Development, Skills, and anything after `\end{document}` | replace with the new owner's content |
| Letter variables | `base/letter/info.tex` — `\myname`, `\mytitle`, `\myemail`, `\mylinkedin`, `\myphone`, `\mylocation` | replace |
| Letter prose | `base/letter/body.tex` | rewrite entirely |
| Signature | `base/letter/sig.jpg` | **delete it.** It is a real person's signature. The letter compiles without it thanks to `\IfFileExists`; tell them to drop in their own scan. |
| Old applications | `applications/` | delete if present — those are someone else's applications |
| Owner references | any `Oscar`/name left in `profile/` or `base/` | none should remain |

Two more, easy to overlook because they are instruction files rather than content:

| What | Where | Action |
| --- | --- | --- |
| Known issues | `CLAUDE.md` → "Known issues, not yet fixed" | delete the entries — they describe the previous owner's documents. Refill it as issues in the new owner's documents come up. |
| Clone URL and asides | `README.md` → "Using this for your own CV" | repoint the clone URL at the new owner's repository and drop the first-person references to the previous one. |

The rest of `CLAUDE.md`, `README.md` and the skills say "the owner" throughout and
need no editing.

Verify at the end with a grep for the previous owner's name, email, phone and
handles across all tracked files. Nothing may survive.

## Step 2 — Interview

Fill `profile/` from their answers, then render `base/` from `profile/`. Never
invent, never leave placeholder text, never carry a bullet over from the previous
owner "as an example".

Follow the mode 1 rules in `CLAUDE.md`. The essentials:

- One section at a time. Identity first, then experience, education, skills,
  learning, activities.
- **Treat the first answer as insufficient.** "I worked on a vision system" is not
  usable. Which models, which language, which hardware, how many, how fast,
  deployed or prototype, who used it, what changed because of it. Keep pushing
  until the bullet could not have been written by someone who did not do the work.
- Chase numbers. Throughput, latency, team size, users, percentage, duration.
- If they cannot answer, drop the claim. Do not soften it into vagueness.
- Confirm dates, employer names, titles and locations exactly as they should
  appear.
- Anything worth having but unanswered goes into `_gaps.md` as a question.

They will want to stop early. The interview is the whole value of this repository —
the templates are the easy part. Keep going until each section has real content.

## Step 3 — Render and compile

Write `base/cv/main.tex` and the letter from `profile/`, in the voice defined in
`CLAUDE.md`: formal, plain, specific, never the register of a generated letter.

```bash
./build.sh
pdftotext -layout base/cv/build/main.pdf -
```

Both documents must be exactly one page. Read the extracted text and confirm the
new owner's name, email and phone are all present and correct — that output is
roughly what an automated screening filter receives.

## Step 4 — Hand over

Tell them:

- Where their documents are and that both compile to one page.
- To add their own `sig.jpg` to `base/letter/` if they want a signature.
- What is still in `_gaps.md` and why answering it improves every future
  application at once.
- That `/apply <url>` runs a full application from a job posting link.
