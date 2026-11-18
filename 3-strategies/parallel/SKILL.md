---
name: parallel-dashboard
description: "Builds the AI dashboard for the Parallel strategy: the student's manual dashboard plus their Parallel export from the sandbox. Use when the student asks to build or change the Parallel dashboard."
---

# Parallel: build the AI dashboard

Several calls run at the same time, each with its own view; an aggregator combines their answers.

This folder turns the student's manual dashboard (`2-manual-dashboard/dashboard.html`) and their export (`export/strategy.md`) into an AI-assisted dashboard that uses this strategy for the final decision of their workflow.

## Before you build

- `export/strategy.md` must exist. If not, the student has not exported this strategy yet, or has not synced: say so.
- `2-manual-dashboard/dashboard.html` must exist. If not, follow "The manual dashboard" in the main `SKILL.md`.

## Build

Follow `reference/build-dashboard.md`, with the dashboard in `dashboard/` of this folder. For this strategy:

- Each parallel box usually belongs on the tab of its own view; the aggregator on the tab where its advice is used (or none: its advice shows under the flow).
- The parallel boxes do not see each other's answers; only the aggregator does.

## Then: the evaluation

The student evaluates the dashboard by hand: they change the input (click In) or a box's prompt or model (click the box) themselves, give every run a title in the small box next to **Run** (for example "Baseline" or "Vary input: budget €20"), and run. Every run is logged; see `reference/evaluation.md`. After each run the log is downloaded; the student types "sync". When they say "findings", Claude groups the runs by title, names the evaluation method of each title with the student, and writes `evaluation/<title>/findings.md`, each compared with the baseline runs.
