---
name: routing-baseline-stability
description: "Evaluation test 'Baseline and stability' for the Routing strategy. Use when the student sets up, syncs or writes findings for this test."
---

# Routing · Baseline and stability

**Question.** Document and Compare (TIA): what exactly produced this result, and do repeated runs give the same outcome?

**What changes.** Nothing is changed: this is the baseline every other test is compared with. It uses the strategy's own dashboard (`../../dashboard/`), so there is no separate dashboard here.

Follow `reference/evaluation.md` (set up, sync, findings). The variation type in the log is `baseline`. For this test:

- Check that the test cases in `3-strategies/test-cases.md` include a neutral case, and that the strategy's dashboard is built.
- The plan: every test case, at least 3 runs each (the 3× button), with "What did you change?" left empty. Write that in `plan.md`, with the date, the strategy version and the models of every box (from the export).
- After sync, the runs are in `../../dashboard/logs/`: that is where the baseline lives.
- Findings: per test case, how many runs gave the same outcome (`ai_outcome`), and where they differ. That is the stability (TIA).

The folder ends up with `plan.md` and `findings.md`.
