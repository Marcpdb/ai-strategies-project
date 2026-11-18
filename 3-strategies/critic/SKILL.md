---
name: critic-dashboard
description: "Builds the AI dashboard for the Critic strategy: the student's manual dashboard plus their Critic export from the sandbox. Use when the student asks to build or change the Critic dashboard."
---

# Critic: build the AI dashboard

A generator makes a proposal; an evaluator checks it against criteria and sends feedback, until it is accepted or the maximum number of rounds is reached.

This folder turns the student's manual dashboard (`2-manual-dashboard/dashboard.html`) and their export (`export/strategy.md`) into an AI-assisted dashboard that uses this strategy for the final decision of their workflow.

## Before you build

- `export/strategy.md` must exist. If not, the student has not exported this strategy yet, or has not synced: say so.
- `2-manual-dashboard/dashboard.html` must exist. If not, follow "The manual dashboard" in the main `SKILL.md`.

## Build

Follow `reference/build-dashboard.md`, with the dashboard in `dashboard/` of this folder. For this strategy:

- The evaluator's criteria must come from the student's workflow: check that its prompt names them. If it still has the dinner rules, ask for the student's own criteria.
- Every round (proposal, verdict, feedback) shows in the conversation panel.

## Then: the evaluation

The student evaluates the dashboard by hand: they change the input (click In) or a box's prompt or model (click the box) themselves, give every run a title in the small box next to **Run** (for example "Baseline" or "Vary input: budget €20"), and run. Every run is logged; see `reference/evaluation.md`. After each run the log is downloaded; the student types "sync". When they say "findings", Claude groups the runs by title, names the evaluation method of each title with the student, and writes `evaluation/<title>/findings.md`, each compared with the baseline runs.
