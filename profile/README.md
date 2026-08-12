# Profile — the inventory

Everything the owner has done that could ever belong on a CV, with no page limit and
no editing for length. This is the **content source of truth**.

`base/cv/main.tex` is not the inventory. It is one rendering of it: a general
purpose one-pager. A tailored CV is a *different* selection from the same
inventory, chosen to match a specific posting.

```
profile/            everything, uncut          <- add here first, always
  ↓ select
base/cv/            default one-pager
  ↓ select + reorder
applications/…/cv/  one-pager for one posting
```

The point: nothing is ever lost because it did not fit. An entry cut from the CV
stays here and can come back for the next posting that rewards it.

## Format

One `##` heading per entry. Every entry carries:

- **When** — absolute dates, `MM.YYYY` or a year range.
- **Where** — employer/institution and location, when applicable.
- **Tags** — lowercase keywords used to match an entry against a posting. Be
  generous: tags cost nothing and are what makes selection work.
- Bullets in **full detail** — longer and more specific than any CV would fit.
  Trimming happens at render time, not here.

Write bullets so a shorter version can be derived by deletion. Put the outcome
and the number in the first clause.

## Rules

- Only what the owner has confirmed. Same truthfulness bar as everywhere else in this
  repo — an unverified detail belongs in `_gaps.md`, not in an entry.
- Never delete an entry because it is currently irrelevant. Irrelevant today is
  the right fit two postings from now.
- Never name a target company here. This directory is public.
- When something new happens, it lands here first, and only then propagates to
  `base/cv/`.

## Selection priorities

Standing guidance from the owner, 12.08.2026. Overridden by a posting that clearly
asks otherwise, but this is the default order.

**Lead with:**

1. **PickAnything** — ownership, adoption across two continents, real numbers.
   The strongest item available.
2. **The vision-based AI platform** — the thing other applications build on.
3. **Code review, merge authority and teaching** — senior scope without the title.

**Always keep, even when short of space:**

- **The Franka Emika C++ API.** Old and small, but it is the middle link in an
  unbroken C++ record spanning 2022 to now across three roles. Cutting it breaks
  the chain, which is exactly what a C++-heavy reader is checking.
- **The Alistair Cockburn hexagonal architecture training.** Trained by the person
  who created the pattern, applies it at work, teaches it to colleagues. Rare and
  verifiable.

**Deliberately downplayed:**

- **HALCON.** Real experience, but he does not want a HALCON-centric role. Never
  lead with it; never target roles built around it. See `learning.md`.

**Never write:**

- **The absence of a senior title.** Decided 12.08.2026. Phrases like "without
  holding a senior title" or "despite not being senior" do not go on a CV or in a
  letter. Describe the scope — ownership, code review, merge authority, teaching —
  and let it speak for itself. Do not reintroduce this on a later pass.

**Rarely select:**

- Smart welding and palletizing — only for welding, logistics or C#/.NET roles.
- The TRANE internship — a 2020 non-software internship, outclassed by everything
  else on the page.
- The eleven-book list — name two or three, or fold it into one line.

## `_gaps.md`

Open questions — entries missing the number, scope or outcome that would make
them strong. Working through that file is the cheapest way to improve every
future CV at once.
