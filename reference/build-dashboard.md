# How to build an AI dashboard from the manual dashboard and an export

Used by the `SKILL.md` of every strategy folder. `<strategy>` below is that folder, for example `3-strategies/parallel/`.

## Inputs

- `<strategy>/export/strategy.md`: the export of the sandbox, filled in by the student. "My workflow" holds the student's answers; "Boxes" is the source of truth for the flow (`reference/strategies.md` shows how it becomes nodes and edges).
- `2-manual-dashboard/`: the student's first workflow dashboard and its data. `dashboard.html` is the dashboard itself; everything else there (data files, PDF, notes) is background. Never change anything in that folder.

## 1. Check what is still open

Anything that still says `_(fill in)_` in `strategy.md` must be answered first: workflow, decision, outcomes, why it fits, who decides, input, the tab of every box. Ask one short question at a time, use the student's own words, and write the answers into `strategy.md`. Never invent them.

## 2. Map the strategy onto the dashboard, and confirm

Show the student one short mapping and wait for their yes:

- **In box:** which data of the dashboard goes into the strategy, and how it is written as text (`caseText()`). The same for every strategy, with the dashboard's own data as the default, so the strategies can be compared.
- **Boxes per tab:** a small table from the "Tab of my dashboard" line of every box. A box without a matching tab goes on the tab where its output is used.
- **Out box:** the advice, shown under the flow, mapped to the outcomes. The prompt of the last LLM box must end with `Advice: <outcome>`; if it does not, ask whether you may add that one line.

## 3. Build

Start from `reference/dashboard-template.html`: a finished dashboard for the invented dinner example, with the placeholders `/*__ENGINE__*/`, `/*__STRATEGY_JSON__*/` and `/*__STEP_OF__*/`. Replace only its dinner content: the title and header, the data, `STEPS` (the student's own tabs; there is no separate decision tab), `OUTCOMES` (the possible outcomes and the words that recognise them in the line `Advice: ...`), `caseText()`, the defaults in `ST`, and the dashboard's own tabs between `function tabHtml` and `END of the dashboard's own tabs`. Keep everything else: the flow, the agent cards, the conversation, Run, the evaluation dropdown, the advice under the flow, and Download log.

1. **Title:** "<dashboard name> · <strategy name>". Keep the student's tabs, data and content.
2. **Engine, copied verbatim:** the block from `/* ===== ENGINE START` to `/* ENGINE END */` out of `1-playground/playground.html`. Do not write your own strategy logic.
3. **Strategy, copied verbatim:** `STRATEGY` from the "Boxes" section, prompts exactly as written; `STRATEGY.strategy` is the strategy's name (Single call, Chain, Routing, Parallel, Orchestrator, Critic, Debate), because the log files are named after it. The confirmed mapping goes in `STEP_OF`.
4. **Evaluation:** nothing to add. The test dropdown, their extra prompts and the 3 runs per test are in the template; the Agents test only appears when the strategy has more than one LLM box.
5. Write the page to `<strategy>/dashboard/dashboard.html`.
6. **Publish** it with the Artifact tool: `capabilities` `{"sample": {}, "downloads": true}`, a short generic `icon`. Write the link to `<strategy>/dashboard/link.md`. To change it later, edit `dashboard.html` and publish again with the link as `url`, so the link stays.

## 4. Hand over

Check the page once for errors. Then tell the student in a few lines: the link, the mapping you used, what came from their file and what you added, and the next step: the evaluation, with the Evaluation test dropdown next to Run (`reference/evaluation.md`). Remind them to share the dashboard directly with the people who need to see it, not as a public link.

## Rules

- The same In text in every strategy, so the comparison is fair.
- Tokens are estimates (about 4 characters per token); say so. Show the model that actually answered.
- Plain English, short.
