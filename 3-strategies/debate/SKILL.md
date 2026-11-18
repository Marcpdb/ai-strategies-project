---
name: debate-dashboard
description: "Builds the AI dashboard for the Debate strategy: the student's manual dashboard plus their Debate export from the sandbox. Use when the student asks to build or change the Debate dashboard."
---

# Debate: build the AI dashboard

Several debaters answer each other in rounds; a judge reads the whole discussion and decides. A debater can speak for one step of the workflow, or for one possible outcome.

This folder turns the student's manual dashboard (`2-manual-dashboard/dashboard.html`) and their export (`export/strategy.md`) into an AI-assisted dashboard that uses this strategy for the final decision of their workflow.

## Before you build

- `export/strategy.md` must exist. If not, the student has not exported this strategy yet, or has not synced: say so.
- `2-manual-dashboard/dashboard.html` must exist. If not, follow "The manual dashboard" in the main `SKILL.md`.

## Build

Follow `reference/build-dashboard.md`, with the dashboard in `dashboard/` of this folder. For this strategy:

- The playground has two Debate examples; both export as Debate (the line "Based on:" says which). In **Debate (steps)** each debater speaks for one step of the workflow: put it on the tab of that step. In **Debate (dishes)** each debater defends one possible outcome (one dish): those debaters work on the decision itself, so put them on the tab of the decision. The judge goes on the tab where its advice is used (or none: its advice shows under the flow).
- With more than four debaters the dashboard draws a larger circle by itself.
- Keep the number of rounds from the export. Show the discussion per round.

## Then: the evaluation

The student evaluates the dashboard by hand: they change the input (click In) or a box's prompt or model (click the box) themselves, give every run a title in the small box next to **Run** (for example "Baseline" or "Vary input: budget €20"), and run. Every run is logged; see `reference/evaluation.md`. After each run the log is downloaded; the student types "sync". When they say "findings", Claude groups the runs by title, names the evaluation method of each title with the student, and writes `evaluation/<title>/findings.md`, each compared with the baseline runs.
