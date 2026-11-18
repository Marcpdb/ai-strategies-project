# How a strategy file becomes a flow

The engine in `1-playground/playground.html` (between `ENGINE START` and `ENGINE END`) runs a flow of `nodes` and `edges`. Copy that block; do not reimplement it. You build the nodes and edges from the "Boxes" section of the strategy file. `dashboard-template.html` lays the flow out by itself, so nodes need no positions.

## From "Boxes" to nodes and edges

Every `### <name>` is one node (in the playground a box also has a workflow step, shown under its name; it is not exported: the "Tab of my dashboard" line takes its place):

- `id`: the name in lower case, letters and digits only, joined with `-` (Budget & time → `budget-time`, Chloé → `chloe`).
- `label`: the name. `type`: from "Type" (the first word).
- `cfg.model` from "Model", `cfg.effort` (empty for default), `cfg.tools` (retrieval, calculator, memory), `cfg.maxRounds` (evaluator, "maximum rounds"), `cfg.rounds` (debater), `cfg.maxWords` (gate, "at most N words"), `cfg.prompt`: the text block, exactly as written.

"Sends to" gives the edges, one per name, in that order: `{from, to}`. `(line: X)` adds `label: "X"`. `(line: X, goes back)` adds `loop: true` (the evaluator's way back). A name that has no `###` of its own (Out, Exit) becomes a node of type `out`. For every tool of an LLM add one node of type `aux` (`aux`: retrieval, tools for calculator, memory; label Retrieval, Tools, Memory) and an edge from the LLM to it. The notes under "Notes for retrieval" go into `STRATEGY.knowledge`.

`STRATEGY = {strategy, knowledge, nodes, edges}`. The template computes `version` with `ENGINE.version`.

## Box types

| Type | What it does |
|---|---|
| in | Sends the case (in a dashboard: `caseText()` built from the dashboard data) |
| out | Receives the result. If there are several, only the ones that are reached count |
| llm | An agent: one call to Claude with its model, effort, tools and prompt |
| worker | An agent that does one sub-task from the orchestrator (`{{subtask}}`) |
| router | An agent that sends the case to one of the boxes it connects to; the others are skipped. Only in the Routing example and its template: the Sandbox has no Router button |
| gate | A check in code, not an agent: passes when the text has at most `maxWords` words; when it fails, the flow follows the line labelled "Fail" |
| orchestrator | An agent that plans sub-tasks, one per worker it connects to; extra workers are skipped |
| evaluator | An agent that accepts or rejects what flows in. On reject, the box its loop line points to runs again with `{{feedback}}`, up to `maxRounds` |
| debater | All debaters speak in every round, at the same time, with `{{debate}}` = everything said so far; `rounds` sets the number of rounds. They answer each other. A debater can stand for one step of the workflow (Debate (steps)) or for one possible outcome (Debate (dishes)) |
| aux | Retrieval, Tools or Memory, drawn under an agent. They light up when that agent uses the tool |

Names: a single box is called **Agent**; the last agent before Out is always **Judge (…)**, with its role between brackets: Judge (choose), Judge (aggregator), Judge (synthesizer), Judge (evaluator), Judge (jury). In a template, debaters are called Actor 1, Actor 2, …

## Placeholders in prompts

`{{input}}` what flows into the box (several inputs are joined, each under "## From <box>") · `{{question}}` the In text · `{{subtask}}` · `{{feedback}}` · `{{debate}}`. A prompt without any placeholder gets the input added at the end.

## What every run returns

The output, every step (box, type, round, model asked, model answered, effort, tools, what went in, the full prompt, what came out, start and end time, a note such as the chosen route or the verdict), the debate transcript, the number of calls, estimated tokens and seconds.
