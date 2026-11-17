---
name: single-call-vary-fact
description: "Evaluation test 'Decisive fact' for the Single call strategy. Use when the student asks about this test or writes findings for it."
---

# Single call · Decisive fact

**Question.** Vary (counterfactual prompting): does changing one decisive fact in the input change the outcome?

**How it runs.** Choose **Fact** in the Evaluation test dropdown of the Single call dashboard (`../../dashboard/`) and click Run test: 3 runs. Nothing to set up by hand. `variation_type` in the log: `fact`.

**What changes.** One extra call changes one fact in the input that should change the advice (a budget, a size, a date, a requirement). The prompts stay as they are. The same changed input is used in all 3 runs.

Follow `reference/evaluation.md`. Findings are written only when every test of the Single call dashboard has its 3 runs; then this folder gets `findings.md`, from `../../dashboard/logs/runs.json`. In particular:

- The changed fact, from what to what (`what_changed`).
- The outcomes of the 3 runs next to the 3 baseline runs: did the outcome change, and does the output mention the changed fact? Ask the student whether this is the change they would expect.
- Say what the boxes produced, never what they "thought".
