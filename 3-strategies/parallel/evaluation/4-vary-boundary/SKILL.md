---
name: parallel-vary-boundary
description: "Evaluation test 'Missing or conflicting information' for the Parallel strategy. Use when the student asks about this test or writes findings for it."
---

# Parallel · Missing or conflicting information

**Question.** Vary (boundary testing): with missing or conflicting information, does it flag uncertainty, or make things up?

**How it runs.** The **Boundary** button next to Run in the Parallel dashboard (`../../dashboard/`), 3 runs. Nothing to set up by hand. `variation_type` in the log: `boundary`.

**What changes.** One extra call removes one piece of information the advice depends on, or adds one sentence that contradicts another fact. The prompts stay as they are. The same input is used in all 3 runs.

Follow `reference/evaluation.md`. Findings are written only when every test of the Parallel dashboard has its 3 runs; then this folder gets `findings.md`, from `../../dashboard/logs/runs.json`. In particular:

- What was removed or contradicted (`what_changed`).
- The student's coding matters most here: count "flags uncertainty" and "makes things up" over the 3 runs, and quote the sentence of the output that shows it, word for word.
- Say what the boxes produced, never what they "thought".
