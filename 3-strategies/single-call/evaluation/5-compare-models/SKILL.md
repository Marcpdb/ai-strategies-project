---
name: single-call-compare-models
description: "Evaluation test 'Models' for the Single call strategy. Use when the student asks about this test or writes findings for it."
---

# Single call · Models

**Question.** Compare (CSA, models): how do models differ on the same case?

**How it runs.** The **Models** button next to Run in the Single call dashboard (`../../dashboard/`), 3 runs. Nothing to set up by hand. `variation_type` in the log: `model`.

**What changes.** Every LLM box gets the next model up: Haiku → Sonnet, Sonnet → Opus, Opus → Sonnet. Effort, prompts and input stay the same. No extra call.

Follow `reference/evaluation.md`. Findings are written only when every test of the Single call dashboard has its 3 runs; then this folder gets `findings.md`, from `../../dashboard/logs/runs.json`. In particular:

- `models_answered` shows which model really answered: a named model that is not available is replaced by one of the same tier. Report it.
- The outcomes per model next to the baseline; also the time and estimated tokens per run, compared with the baseline.
- Say what the boxes produced, never what they "thought".
