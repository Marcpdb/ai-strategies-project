---
name: compare-and-conclude
description: "Compares the student's 3 strategies on every evaluation test (CSA) and helps them conclude under which conditions a strategy holds up and where it breaks. Use when the student asks to compare strategies or to conclude."
---

# Compare the strategies, and conclude

Two parts. Both work only from the logs and findings in `3-strategies/`; run "sync" first (main `SKILL.md`).

## 1. Compare the strategies (CSA): "compare"

How do the three strategies differ, test by test?

- Check first with "status" (main `SKILL.md`) which tests every strategy has done. Compare what is there; list every missing test under "Missing".
- Take every run: the baseline (`3-strategies/<strategy>/dashboard/logs/runs.json`) and every test (`3-strategies/<strategy>/evaluation/<test>/logs/runs.json`). Put them together in `all-runs.csv` here, one row per run with the columns of `reference/log-format.md` (without `steps`); the `strategy` and `variation_type` columns tell them apart.
- Check that the strategies used the same test cases with the same input, and in each test the same change (the `plan.md` files, and `what_changed`). Where they differ, say so: those cells cannot be compared one to one.
- Write `comparison.md`:
  - **Overview:** one table, the strategies as rows and the tests as columns. One short cell each, from the logs and the `findings.md` of that test, for example "3 of 3 the same outcome", "outcome changed in 2 of 3 cases", "flagged the missing height in 3 of 3 runs", "wrong fact reached the outcome in 1 of 3". `n/a` where a test does not apply, `missing` where it was not done.
  - **Per test:** one section per test with the change (from `plan.md`), and a table per test case: strategies as rows, the outcome of every run, compared with that strategy's baseline (same or changed).
  - **Cost:** per strategy, calls, estimated tokens and seconds per run (averages), and the models that actually answered.
  - **Missing:** tests not done, fewer runs than planned, runs with an error.
  Say only what the logs and findings show.

## 2. Conclude: "conclude"

Under which conditions does a strategy hold up, and where does it break?

- Read every `findings.md` and `comparison.md`. Make `conclusion.md` with, per strategy, one short line per test with what the findings show (with the folder it comes from), and the student's own conclusion from each `findings.md`.
- Leave the two final sections for the student: "Where each strategy holds up, and where it breaks", and "Which strategy I would use for my workflow, and why". Ask them questions that help: which test changed the outcome most, which strategy flagged uncertainty, where errors spread, what the extra calls of a strategy bought. Do not write the conclusion for them.
- Tips: vary one thing at a time; report all runs, not the best ones; no anthropomorphism ("the agents debated" does not mean they reasoned).
