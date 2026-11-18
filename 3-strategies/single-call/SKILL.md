---
name: single-call-dashboard
description: "Builds the AI dashboard for the Single call strategy: the student's manual dashboard plus their Single call export from the sandbox. Use when the student asks to build or change the Single call dashboard."
---

# Single call: build the AI dashboard

One agent does the whole task, with tools: retrieval (searching notes), a calculator and memory.

This folder turns the student's manual dashboard (`2-manual-dashboard/dashboard.html`) and their export (`export/strategy.md`) into an AI-assisted dashboard that uses this strategy for the final decision of their workflow.

## Before you build

- `export/strategy.md` must exist. If not, the student has not exported this strategy yet, or has not synced: say so.
- `2-manual-dashboard/dashboard.html` must exist. If not, follow "The manual dashboard" in the main `SKILL.md`.

## Build

Follow `reference/build-dashboard.md`, with the dashboard in `dashboard/` of this folder. For this strategy:

- The one LLM box sits on the tab where its advice is used (or none: its advice shows under the flow); its tools are drawn under it.
- Retrieval searches the notes in the export ("Notes for retrieval"). Ask the student which background from `2-manual-dashboard/` belongs in those notes, in their own words; do not copy whole documents.
- Memory stays in the dashboard's browser between runs. Say so: it can make repeated runs differ.

## Then: the evaluation

The student evaluates the dashboard by hand: they change the input (click In) or a box's prompt or model (click the box) themselves, give every run a title in the small box next to **Run** (for example "Baseline" or "Vary input: budget €20"), and run. Every run is logged; see `reference/evaluation.md`. After each run the log is downloaded; the student types "sync". When they say "findings", Claude groups the runs by title, names the evaluation method of each title with the student, and writes `evaluation/<title>/findings.md`, each compared with the baseline runs.

Single call has one LLM box, so the method Agents (ISIA) does not apply to it.
