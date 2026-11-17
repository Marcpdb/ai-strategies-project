---
name: orchestrator-dashboard
description: "Builds the AI dashboard for the Orchestrator strategy: the student's manual dashboard plus their Orchestrator export from the sandbox. Use when the student asks to build or change the Orchestrator dashboard."
---

# Orchestrator: build the AI dashboard

An orchestrator decides during the run which sub-tasks are needed and hands them to workers; a synthesizer combines the results.

This folder turns the student's manual dashboard (`2-manual-dashboard/dashboard.html`) and their export (`export/strategy.md`) into an AI-assisted dashboard that uses this strategy for the final decision of their workflow.

## Before you build

- `export/strategy.md` must exist. If not, the student has not exported this strategy yet, or has not synced: say so.
- `2-manual-dashboard/dashboard.html` must exist. If not, follow "The manual dashboard" in the main `SKILL.md`.

## Build

Follow `reference/build-dashboard.md`, with the dashboard in `dashboard/` of this folder. For this strategy:

- The sub-tasks are only known during a run, so workers cannot be tied to fixed tabs: put them on the tab where their results are used, and show each worker's sub-task title.
- The synthesizer goes on the decision tab.

## Then: the evaluation

Each folder in `evaluation/` is one test, with its own `SKILL.md`. Start with `1-baseline-stability`: every other test is compared with it.

| Folder | Step |
|---|---|
| `1-baseline-stability` | Document and Compare (TIA) |
| `2-vary-wording` | Vary (systematic prompt variation) |
| `3-vary-fact` | Vary (counterfactual prompting) |
| `4-vary-boundary` | Vary (boundary testing) |
| `5-compare-models` | Compare (CSA, models) |
| `6-compare-agents` | Compare (ISIA, multi-agent only) |
