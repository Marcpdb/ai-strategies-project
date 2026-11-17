---
name: routing-dashboard
description: "Builds the AI dashboard for the Routing strategy: the student's manual dashboard plus their Routing export from the sandbox. Use when the student asks to build or change the Routing dashboard."
---

# Routing: build the AI dashboard

A router first decides what kind of case this is, then sends it to the one specialist that fits. The other specialists are skipped.

This folder turns the student's manual dashboard (`2-manual-dashboard/dashboard.html`) and their export (`export/strategy.md`) into an AI-assisted dashboard that uses this strategy for the final decision of their workflow.

## Before you build

- `export/strategy.md` must exist. If not, the student has not exported this strategy yet, or has not synced: say so.
- `2-manual-dashboard/dashboard.html` must exist. If not, follow "The manual dashboard" in the main `SKILL.md`.

## Build

Follow `reference/build-dashboard.md`, with the dashboard in `dashboard/` of this folder. For this strategy:

- The router usually sits on the first tab where the case is described; each specialist on the tab of its point of view.
- Show on the decision tab which route was chosen, and why (the router's note).

## Then: the evaluation

The dashboard has one button per test next to Run (6 tests, 3 runs each). Each button makes its own change automatically and logs it; see `reference/evaluation.md`. The student runs every test, codes every run on the last tab, downloads both log files and types "sync". When all 6 tests are done, "findings" writes `findings.md` in each folder of `evaluation/`:

| Folder | Button | Step |
|---|---|---|
| `1-baseline-stability` | Baseline | Document and Compare (TIA) |
| `2-vary-wording` | Wording | Vary (systematic prompt variation) |
| `3-vary-fact` | Fact | Vary (counterfactual prompting) |
| `4-vary-boundary` | Boundary | Vary (boundary testing) |
| `5-compare-models` | Models | Compare (CSA, models) |
| `6-compare-agents` | Agents | Compare (ISIA, multi-agent only) |
