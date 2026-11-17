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

Each folder in `evaluation/` is one test, with its own `SKILL.md`. Start with `1-baseline-stability`: every other test is compared with it.

| Folder | Step |
|---|---|
| `1-baseline-stability` | Document and Compare (TIA) |
| `2-vary-wording` | Vary (systematic prompt variation) |
| `3-vary-fact` | Vary (counterfactual prompting) |
| `4-vary-boundary` | Vary (boundary testing) |
| `5-compare-models` | Compare (CSA, models) |
| `6-compare-agents` | Compare (ISIA, multi-agent only) |
