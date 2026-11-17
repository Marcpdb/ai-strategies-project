---
name: parallel-vary-fact
description: "Evaluation test 'Decisive fact' for the Parallel strategy. Use when the student sets up, syncs or writes findings for this test."
---

# Parallel · Decisive fact

**Question.** Vary (counterfactual prompting): does changing one decisive fact in the input change the outcome?

**What changes.** One change: one fact in one test case that should decide the outcome (a budget, a size, a date, a requirement). The prompts stay as they are.

Follow `reference/evaluation.md` (set up, sync, findings). The variation type in the log is `fact`. For this test:

- Ask the student which test case and which fact, and what outcome they expect when it changes. Write the expectation in `plan.md` before any run.
- Build the test dashboard with one extra test case: the original case with that one fact changed, named "<case> (changed: <fact>)". Run it as often as the baseline.
- Findings: did the outcome change the way the student expected? Compare with the baseline runs of the original case.

The folder ends up with `plan.md`, `dashboard.html`, `link.md`, `logs/` and `findings.md`.
