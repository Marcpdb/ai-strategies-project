---
name: compare-and-conclude
description: "Compares the student's strategies on the same test cases (CSA) and helps them conclude under which conditions a strategy holds up and where it breaks. Use when the student asks to compare strategies or to conclude."
---

# Compare the strategies, and conclude

Two parts. Both work only from the logs and findings in `3-strategies/`; run "sync" first (main `SKILL.md`).

## 1. Compare the strategies (CSA): "compare"

How do the strategies differ on the same cases?

- Take the baseline runs of every strategy that has them: `3-strategies/<strategy>/dashboard/logs/runs.json`. Put them together in `all-baseline-runs.csv` here, one row per run with the columns of `reference/log-format.md` (without `steps`; the `strategy` column tells them apart).
- Check that the strategies used the same test cases with the same input (`test_case`, `input`). If not, say which differ: those cannot be compared.
- Write `comparison.md`:
  - one table per test case: strategies as rows; the outcomes of the runs, and how many runs gave the same outcome;
  - per strategy: calls, estimated tokens and seconds per run (averages over the runs), and the models that actually answered;
  - what is missing: strategies with fewer runs than planned, runs with an error.
  Say only what the logs show.

## 2. Conclude: "conclude"

Under which conditions does a strategy hold up, and where does it break?

- Read every `findings.md` and `comparison.md`. Make `conclusion.md` with, per strategy, one short line per test with what the findings show (with the folder it comes from), and the student's own conclusion from each `findings.md`.
- Leave the final section, "Where each strategy holds up, and where it breaks", for the student. Ask them questions that help: which test changed the outcome most, which strategy flagged uncertainty, where errors spread. Do not write the conclusion for them.
- Tips: vary one thing at a time; report all runs, not the best ones; no anthropomorphism ("the agents debated" does not mean they reasoned).
