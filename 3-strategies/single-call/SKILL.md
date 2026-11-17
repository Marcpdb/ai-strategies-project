---
name: single-call-dashboard
description: "Builds the AI dashboard for the Single call strategy: the student's manual dashboard plus their Single call export from the sandbox. Use when the student asks to build or change the Single call dashboard."
---

# Single call: build the AI dashboard

One LLM call does the whole task, with tools: retrieval (searching notes), a calculator and memory.

This folder turns the student's manual dashboard (`2-manual-dashboard/dashboard.html`) and their export (`export/strategy.md`) into an AI-assisted dashboard that uses this strategy for the final decision of their workflow.

## Before you build

- `export/strategy.md` must exist. If not, the student has not exported this strategy yet, or has not synced: say so.
- `2-manual-dashboard/dashboard.html` must exist. If not, follow "The manual dashboard" in the main `SKILL.md`.

## Build

Follow `reference/build-dashboard.md`, with the dashboard in `dashboard/` of this folder. For this strategy:

- The one LLM box usually sits on the decision tab; its tools are drawn under it.
- Retrieval searches the notes in the export ("Notes for retrieval"). Ask the student which background from `2-manual-dashboard/` belongs in those notes, in their own words; do not copy whole documents.
- Memory stays in the dashboard's browser between runs. Say so: it can make repeated runs differ.

## Then: the evaluation

The dashboard has one button per test next to Run (5 tests, 3 runs each). Each button makes its own change automatically and logs it; see `reference/evaluation.md`. The student runs every test, codes every run on the last tab, downloads both log files and types "sync". When all 5 tests are done, "findings" writes `findings.md` in each folder of `evaluation/`:

| Folder | Button | Step |
|---|---|---|
| `1-baseline-stability` | Baseline | Document and Compare (TIA) |
| `2-vary-wording` | Wording | Vary (systematic prompt variation) |
| `3-vary-fact` | Fact | Vary (counterfactual prompting) |
| `4-vary-boundary` | Boundary | Vary (boundary testing) |
| `5-compare-models` | Models | Compare (CSA, models) |
