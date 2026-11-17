---
name: debate-baseline-stability
description: "Evaluation test 'Baseline and stability' for the Debate strategy. Use when the student asks about this test or writes findings for it."
---

# Debate · Baseline and stability

**Question.** Document and Compare (TIA): what exactly produced this result, and do repeated runs give the same outcome?

**How it runs.** The **Baseline** button next to Run in the Debate dashboard (`../../dashboard/`), 3 runs. Nothing to set up by hand. `variation_type` in the log: `baseline`.

**What changes.** Nothing. The Baseline button runs the strategy as built, 3 times, on the input fixed at the first test run. Every other test is compared with it.

Follow `reference/evaluation.md`. Findings are written only when every test of the Debate dashboard has its 3 runs; then this folder gets `findings.md`, from `../../dashboard/logs/runs.json`. In particular:

- Document: the strategy version, the models of every box (asked and answered), the input, and per run the calls, estimated tokens and seconds.
- Stability: how many of the 3 runs gave the same outcome (`ai_outcome`), and where the outputs differ.
- Say what the boxes produced, never what they "thought".
