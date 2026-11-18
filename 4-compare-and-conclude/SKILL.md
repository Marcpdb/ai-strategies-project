---
name: compare-and-conclude
description: "Compares the student's strategies on the same input (CSA) and helps them conclude under which conditions a strategy holds up and where it breaks. Use when the student asks to compare strategies or to conclude."
---

# Compare the strategies, and conclude

Two parts. Both work only from the logs and findings in `3-strategies/`; run "sync" first (main `SKILL.md`).

**Only when every chosen strategy is done.** The chosen strategies are those with an `export/strategy.md`. Each needs a dashboard, baseline runs in `dashboard/logs/runs.json`, and a `findings.md` for every run title in its log. If one is not done, do not compare or conclude: say which strategy is missing what, and what the student does next ("build the chain dashboard", the baseline still to run, "findings for chain").

## 1. Compare the strategies (CSA): "compare"

How do the strategies differ on the same input?

- Take the logs of every chosen strategy: `3-strategies/<strategy>/dashboard/logs/runs.csv`. Put them together in `all-runs.csv` here (same columns; the `strategy` column tells them apart).
- Check that the strategies used the same input for their baseline runs (`input`). If not, say which differ: those cannot be compared directly.
- Write `comparison.md`:
  - one table per evaluation method that more than one strategy used (baseline first, then the methods named in the findings, such as a decisive fact, missing information, models): strategies as rows; the run title, what was changed, the outcomes of the runs, how many gave the same outcome, the verdicts from each `findings.md` (as checked by the student), and for missing or conflicting information how often uncertainty was flagged and things were made up. Only compare runs of different strategies that changed the same thing on the same input; say where they differ;
  - methods only one strategy used: list them, with that strategy;
  - per strategy: calls, estimated tokens and seconds per run (averages over the runs), and the models that actually answered;
  - what is missing: runs with an error.
  Say only what the logs show.

## 2. Conclude: "conclude"

Under which conditions does a strategy hold up, and where does it break?

- Read every `findings.md` and `comparison.md`. Make `conclusion.md` with, per strategy, one short line per run title with what the findings show (with the folder it comes from), and the student's own conclusion from each `findings.md`.
- Leave the final section, "Where each strategy holds up, and where it breaks", for the student. Ask them questions that help: which change moved the outcome most, which strategy flagged uncertainty, where errors spread. Do not write the conclusion for them.
- Tips: vary one thing at a time; report all runs, not the best ones; no anthropomorphism ("the agents debated" does not mean they reasoned).
