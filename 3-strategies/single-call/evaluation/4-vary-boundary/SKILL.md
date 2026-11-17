---
name: single-call-vary-boundary
description: "Evaluation test 'Missing or conflicting information' for the Single call strategy. Use when the student asks about this test or writes findings for it."
---

# Single call · Missing or conflicting information

**Question.** Vary (boundary testing): with missing or conflicting information, does it flag uncertainty, or make things up?

**How it runs.** Choose **Boundary** in the Evaluation test dropdown of the Single call dashboard (`../../dashboard/`) and click Run test: 3 runs. Nothing to set up by hand. `variation_type` in the log: `boundary`.

**What changes.** One extra call removes one piece of information the advice depends on, or adds one sentence that contradicts another fact. The prompts stay as they are. The same input is used in all 3 runs.

Follow `reference/evaluation.md`. Findings are written only when every test of the Single call dashboard has its 3 runs; then this folder gets `findings.md`, from `../../dashboard/logs/runs.json`. In particular:

- What was removed or contradicted (`what_changed`).
- The coding matters most here: count "flags uncertainty" and "makes things up" over the 3 runs, and quote the sentence of the output that shows it, word for word.
- Say what the boxes produced, never what they "thought".
