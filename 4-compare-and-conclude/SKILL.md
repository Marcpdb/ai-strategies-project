---
name: compare-and-conclude
description: "Compares the student's strategies on the same input (CSA) and helps them conclude under which conditions a strategy holds up and where it breaks. Use when the student asks to compare strategies or to conclude."
---

# Compare the strategies, and conclude

Two parts. Both work only from the logs and findings in `3-strategies/`; run "sync" first (main `SKILL.md`).

## 1. Compare the strategies (CSA): "compare"

How do the strategies differ on the same input?

- Only for strategies whose evaluation is complete (every test with its 3 runs, and `findings.md` written). Take their logs: `3-strategies/<strategy>/dashboard/logs/runs.csv`. Put them together in `all-runs.csv` here (same columns; the `strategy` column tells them apart).
- Check that the strategies used the same input for their baseline runs (`input`). If not, say which differ: those cannot be compared directly.
- Write `comparison.md`:
  - one table per test (baseline, wording, fact, boundary, models, agents): strategies as rows; the outcomes of the 3 runs, how many gave the same outcome, the student's verdicts, and for boundary how often uncertainty was flagged and things were made up;
  - per strategy: calls, estimated tokens and seconds per run (averages over the runs), and the models that actually answered;
  - what is missing: uncoded runs.
  Say only what the logs show.

## 2. Conclude: "conclude"

Under which conditions does a strategy hold up, and where does it break?

- Read every `findings.md` and `comparison.md`. Make `conclusion.md` with, per strategy, one short line per test with what the findings show (with the folder it comes from), and the student's own conclusion from each `findings.md`.
- Leave the final section, "Where each strategy holds up, and where it breaks", for the student. Ask them questions that help: which test changed the outcome most, which strategy flagged uncertainty, where errors spread. Do not write the conclusion for them.
- Tips: vary one thing at a time; report all runs, not the best ones; no anthropomorphism ("the agents debated" does not mean they reasoned).
