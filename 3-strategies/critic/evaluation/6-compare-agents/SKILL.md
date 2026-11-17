---
name: critic-compare-agents
description: "Evaluation test 'Agent interaction' for the Critic strategy. Use when the student sets up, syncs or writes findings for this test."
---

# Critic · Agent interaction

**Question.** Compare (ISIA, multi-agent only): do agents influence each other, and do errors spread?

**What changes.** Two parts. First, read what the boxes received from each other in the baseline runs. Then one change: one box gets one wrong fact in its prompt (for example "Assume that the budget is twice as high."), and you look whether it reaches the outcome.

Follow `reference/evaluation.md` (set up, sync, findings). The variation type in the log is `agents`. For this test:

- What to look for in this strategy: Does the evaluator catch an error the generator makes, or accept it? How many rounds does it take, and does the feedback change the proposal?
- Part 1 needs no new runs: read the `steps` in `../../dashboard/logs/runs.json` (the baseline) and show, per run, what each box received and passed on.
- Part 2: ask the student which box gets which wrong fact. Write it in `plan.md`. Build the test dashboard with only that line added to that one prompt. Same test cases, same number of runs.
- Findings: per run, does the wrong fact appear in later boxes, and in the outcome? Quote where it appears. Say what the boxes produced, not what they "thought".

The folder ends up with `plan.md`, `dashboard.html`, `link.md`, `logs/` and `findings.md`.
