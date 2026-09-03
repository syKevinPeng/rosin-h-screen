# rosin-h-screen

The rating interface for the **H screen** of the rosin atom-mining loop.
A professional violinist (and the author, as a sanity band) rate each
measurement "atom" of violin performance on two questions, each on a
4-point scale with no midpoint:

- **H1 attended**: is this something violin teachers actually attend to in lessons?
- **H2 actionable**: if a tutor reported this value to a student, could the student act on it?

Static site, no server. The only automatic external request is the Inter
font from Google Fonts. Answers autosave in the rater's browser; at the end the
rater sends them through the round's Google Form (a pre-filled link they open
and submit themselves) or downloads them as a file; the durable record is the merged CSV
committed to the rosin repo (`docs/h-screen/round-<n>-scores.csv`). The
protocol is `docs/2026-09-03-h-screen-plan.md` in rosin; decisions D-M6 and
D-M8 in `docs/2026-09-03-mining-loop-decisions.md`.

## Repo rule

**No atom values, plots, corpus statistics, screen outcomes, utility numbers
or model numbers ever enter this repo.** The rater sees only a card title and
one plain-English paragraph per atom (the `prose` field; the structured
fields and cited phrases in rows.json are the record behind it), plus the two
questions (D-M8, outcome-independence). `tests/test_build.py` guards a short list of withheld
caveat words; the rule is broader than the test.

## Layout

```
rounds/round-<n>/rows.json        content: the single source of truth (plain English; `prose` is what the rater reads, the structured fields and cited phrases are the record)
rounds/round-<n>/index.html       built page (rows inlined, form_version stamped)
rounds/round-<n>/form.md          built printable form, fixed order (paper fallback)
rounds/round-<n>/blank-scores.csv built blank score sheet (spreadsheet fallback)
index.html                        redirect to the current round
template/page.html                page template (vanilla HTML/CSS/JS, no dependencies)
template/order.js                 per-rater card order (seeded shuffle), inlined into the page
scripts/build.py                  rows.json -> the three built files (+ root redirect with --current)
scripts/order.py                  Python port of order.js, used to verify exports
scripts/merge_scores.py           per-rater exports -> merged CSV + raw agreement counts
scripts/from_google_sheet.py      Google Form response sheet (CSV) -> per-rater export files
tests/                            pytest; the Node cross-check needs `node` on PATH
```

`form_version` is the first 12 hex digits of the SHA-256 of the canonical
`rows.json`. It is stamped on the page, the printable form, the blank sheet
and every export, so nothing can drift from the committed content. A content
change after first contact with a rater is a new round by protocol.

## Workflow for a round

1. Edit `rounds/round-<n>/rows.json` (rows come from the audited atoms; for
   mining rounds, from `AtomSpec`s). Never put values in it.
2. `python scripts/build.py rounds/round-<n> --current`, then
   `python -m pytest`.
3. Commit rows.json **and** the built files together. Copy `form.md` to rosin
   `docs/h-screen/` (round 0: `round-0-incumbents-form.md`) and pin this
   repo's commit as the rosin submodule. That commit is the freeze.
4. Send each rater their link:
   `https://sykevinpeng.github.io/rosin-h-screen/?rater=violinist` or
   `...?rater=author`. The two calibration cards come first; the rest are
   shuffled per rater (seed = form_version + rater), stable across reloads.
5. At the end the page opens the round's Google Form (`collect` block in
   rows.json) with a compact copy of the answer file pre-filled in its one
   paragraph field (per-card timestamps are left out to keep the link under
   Google's ~8 KB limit; if notes make it longer still, the page switches to
   copy-then-paste); the rater signs in and presses Submit (the Form allows
   editing the response later). Download / copy remain as the fallback and
   carry the full timestamps.
   Then: download the Form's response sheet as CSV and run
   `python scripts/from_google_sheet.py responses.csv --out exports/` to get
   one export file per rater (the last submission per rater wins).
6. `python scripts/merge_scores.py --rows rounds/round-<n>/rows.json --out round-<n>-scores.csv <exports>`
   refuses anything that does not match the frozen form (version, rater,
   order, completeness) and prints raw agreement counts only (no kappa/CVR by
   design, D-M6). Commit the CSV to rosin `docs/h-screen/`.

Paper fallback: print `form.md`, or open the page with `?mode=print`. The
spreadsheet fallback is `blank-scores.csv`; fill `rater`, `h1`, `h2`, `note`
and feed it to the merge script like any export (positions must follow the
blank sheet's fixed order only if the sheet was used as is; otherwise the
merge script will report the mismatch and the order can be reconciled by hand).

## Export columns

`round, form_version, rater, position, atom, is_anchor, seen_as_calibration,
h1, h2, note, shown_at, answered_at, started_at, finished_at`

`is_anchor=1` marks the two calibration cards. Under `anchor_policy:
"repeat"` the same two atoms appear again inside the shuffled block as data
rows with `seen_as_calibration=1`; they are reported flagged because the rater
saw them minutes earlier as labeled examples.

## Citations in rows.json

Every teacher phrase carries a tag: `verbatim` (words the project's pedagogy
syntheses mark as quoted from the source), `synthesis` (the synthesis author's
paraphrase of what a treatise covers, bibliography-level), `expert-opinion`
(the ViolinITS etude-classification spreadsheet), `experiment` (a study's own
variable name), or `uncited` (a paraphrase with no located source, shown to
the rater as such). `locator` points into the syntheses (`T:` treatises, `C:`
Chinese sources, `E:` experiments, `X:` spreadsheet cross-check, then a line
number); those files are not public.
