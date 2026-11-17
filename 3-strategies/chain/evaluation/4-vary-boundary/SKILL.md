---
name: chain-vary-boundary
description: "Evaluation test 'Missing or conflicting information' for the Chain strategy. Use when the student sets up, syncs or writes findings for this test."
---

# Chain · Missing or conflicting information

**Question.** Vary (boundary testing): with missing or conflicting information, does it flag uncertainty, or make things up?

**What changes.** One change: one test case with information left out, or with two pieces of information that contradict each other. The prompts stay as they are.

Follow `reference/evaluation.md` (set up, sync, findings). The variation type in the log is `boundary`. For this test:

- Ask the student which information to remove or make conflicting, in one test case. Write it in `plan.md`.
- Build the test dashboard with that one extra test case, named "<case> (missing: ...)" or "<case> (conflict: ...)". Run it as often as the baseline.
- The two readings matter most here: "flags uncertainty" and "adds facts" (see `reference/evaluation.md`). Findings: count both per run, and quote the sentence of the output that shows it, word for word.

The folder ends up with `plan.md`, `dashboard.html`, `link.md`, `logs/` and `findings.md`.
