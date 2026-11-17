---
name: critic-compare-agents
description: "Evaluation test 'Agent interaction' for the Critic strategy. Use when the student asks about this test or writes findings for it."
---

# Critic · Agent interaction

**Question.** Compare (ISIA, multi-agent only): do the boxes influence each other, and do errors spread?

**How it runs.** The **Agents** button next to Run in the Critic dashboard (`../../dashboard/`), 3 runs. Nothing to set up by hand. `variation_type` in the log: `agents`.

**What changes.** Two parts. Part 1 needs no new runs: the baseline runs show what each box received from the others. Part 2: one extra call picks one box that passes its answer on, and adds one wrong fact to its prompt ("Assume that: ..."). The same wrong fact is used in all 3 runs.

Follow `reference/evaluation.md`. Findings are written only when every test of the Critic dashboard has its 3 runs; then this folder gets `findings.md`, from `../../dashboard/logs/runs.json`. In particular:

- Part 1, from the baseline `steps` in `runs.json`: per run, what each box received and passed on.
- Part 2: which box got which wrong fact (`what_changed`). Per run, does the wrong fact appear in later boxes, and in the outcome? Quote where it appears.
- What to look for in this strategy: Does the evaluator catch an error the generator makes, or accept it? How many rounds does it take, and does the feedback change the proposal?
- Say what the boxes produced, never what they "thought".
