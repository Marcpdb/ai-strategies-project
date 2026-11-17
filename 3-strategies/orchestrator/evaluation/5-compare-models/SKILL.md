---
name: orchestrator-compare-models
description: "Evaluation test 'Models' for the Orchestrator strategy. Use when the student sets up, syncs or writes findings for this test."
---

# Orchestrator · Models

**Question.** Compare (CSA, models): how do models differ on the same cases?

**What changes.** One change: the model. Either every LLM box, or one box (the one that decides). Effort, prompts and test cases stay the same.

Follow `reference/evaluation.md` (set up, sync, findings). The variation type in the log is `model`. For this test:

- Ask the student which box or boxes, and which model (Haiku, Sonnet or Opus). Write it in `plan.md`.
- Build the test dashboard with only the model changed. Same test cases, same number of runs as the baseline.
- `models_answered` shows which model really answered: a named model that is not available is replaced by one of the same tier. Report it.
- Findings: per test case, outcomes per model next to the baseline; also the time and estimated tokens per run.

The folder ends up with `plan.md`, `dashboard.html`, `link.md`, `logs/` and `findings.md`.
