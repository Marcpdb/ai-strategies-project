---
name: routing-vary-wording
description: "Evaluation test 'Prompt wording' for the Routing strategy. Use when the student asks about this test or writes findings for it."
---

# Routing · Prompt wording

**Question.** Vary (systematic prompt variation): does changing the order or wording of the prompts change the outcome?

**How it runs.** Choose **Wording** in the Evaluation test dropdown of the Routing dashboard (`../../dashboard/`) and click Run test: 3 runs. Nothing to set up by hand. `variation_type` in the log: `wording`.

**What changes.** One extra call rewords every prompt of the strategy, with the same meaning, the same placeholders and the same `Advice:` line. The reworded prompts are the same in all 3 runs. The student can edit the extra prompt before the first run.

Follow `reference/evaluation.md`. Findings are written only when every test of the Routing dashboard has its 3 runs; then this folder gets `findings.md`, from `../../dashboard/logs/runs.json`. In particular:

- Show one old and one new prompt side by side (from `extra_output`), so the reader sees what the change was.
- The outcomes of the 3 runs next to the 3 baseline runs: did the outcome change?
- Say what the boxes produced, never what they "thought".
