# How to build an AI dashboard from the manual dashboard and an export

Used by the `SKILL.md` of every strategy folder. `<strategy>` below is that folder, for example `3-strategies/parallel/`.

## Inputs

- `<strategy>/export/strategy.md`: the export of the sandbox, filled in by the student. "My workflow" holds the student's answers; "Boxes" is the source of truth for the flow (`reference/strategies.md` shows how it becomes nodes and edges).
- `2-manual-dashboard/`: the student's first workflow dashboard and its data. `dashboard.html` is the dashboard itself; everything else there (data files, PDF, notes) is background. Never change anything in that folder.
- `3-strategies/test-cases.md`: the test cases, the same for every strategy.

## 1. Check what is still open

Anything that still says `_(fill in)_` in `strategy.md` must be answered first: workflow, decision, outcomes, why it fits, who decides, input, the tab of every box. Ask one short question at a time, use the student's own words, and write the answers into `strategy.md`. Never invent them.

If `3-strategies/test-cases.md` has fewer than 3 test cases, ask for them: concrete situations of the workflow, written as values for the dashboard data. One realistic case, one hard case, one with missing or conflicting information. No real personal data. Write them to `test-cases.md`; every strategy uses the same ones.

## 2. Map the strategy onto the dashboard, and confirm

Show the student one short mapping and wait for their yes:

- **In box:** which data of the dashboard goes into the strategy, and how it is written as text (`caseText()`). The same for every strategy.
- **Boxes per tab:** a small table from the "Tab of my dashboard" line of every box. A box without a matching tab goes on the tab where its output is used.
- **Out box:** the decision tab, mapped to the outcomes. The prompt of the last LLM box must end with `Advice: <outcome>`; if it does not, ask whether you may add that one line.

## 3. Build

Start from `reference/dashboard-template.html`: a finished dashboard for the invented dinner example, with the placeholders `/*__ENGINE__*/`, `/*__STRATEGY_JSON__*/`, `/*__STEP_OF__*/` and `/*__VARIATION__*/`. Replace its dinner content (title, tabs, data, `caseText()`, `TESTS`, how the outcome is read) with the student's dashboard. Keep everything else: the flow, the agent cards, the conversation, the run controls, the decision tab and the run log with its two downloads (their file names tell "sync" where the log belongs).

1. **Title:** "<dashboard name> · <strategy name>". Keep the student's tabs, data and content.
2. **Engine, copied verbatim:** the block from `/* ===== ENGINE START` to `/* ENGINE END */` out of `1-playground/playground.html`. Do not write your own strategy logic.
3. **Strategy, copied verbatim:** `STRATEGY` from the "Boxes" section, prompts exactly as written; the confirmed mapping in `STEP_OF`; the test cases in `TESTS`. Do not change prompts, models, effort or tools unless the student asks.
4. **Variation:** `{type:"baseline",what:""}` for the strategy's own dashboard.
5. Write the page to `<strategy>/dashboard/dashboard.html`.
6. **Publish** it with the Artifact tool: `capabilities` `{"sample": {}, "downloads": true}`, a short generic `icon`. Write the link to `<strategy>/dashboard/link.md`. To change it later, edit `dashboard.html` and publish again with the link as `url`, so the link stays.

## 4. Hand over

Check the page once for errors. Then tell the student in a few lines: the link, the mapping you used, what came from their file and what you added, and the next step: the evaluation, starting with `evaluation/1-baseline-stability`. Remind them to share the dashboard directly with the people who need to see it, not as a public link.

## Rules

- Same In text for the same test case in every strategy, so the comparison is fair.
- Tokens are estimates (about 4 characters per token); say so. Show the model that actually answered.
- Plain English, short.
