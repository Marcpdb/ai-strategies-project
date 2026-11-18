# How to build an AI dashboard from the manual dashboard and an export

Used by the `SKILL.md` of every strategy folder. `<strategy>` below is that folder, for example `3-strategies/parallel/`.

The AI dashboard is the student's **own** manual dashboard, with the same look and layout, and with the AI strategy added to it. It is not a new dashboard in another style.

## Inputs

- `2-manual-dashboard/dashboard.html`: the student's own workflow dashboard (from the Claude artifact link they gave; see "The manual dashboard" in the main `SKILL.md`). Its look, layout, tabs and data are the base. Everything else in `2-manual-dashboard/` is background. Never change anything in that folder.
- `<strategy>/export/strategy.md`: the export of the sandbox, filled in by the student. "My workflow" holds the student's answers; "Boxes" is the source of truth for the flow (`reference/strategies.md` shows how it becomes nodes and edges).
- `reference/dashboard-template.html`: the reference implementation, a finished AI dashboard for the dinner example (Dishes, Guests, Budget & time, Choose). It supplies the pieces to add, already working together.

## 1. Check what is still open

- Anything that still says `_(fill in)_` in `strategy.md` must be answered first: workflow, decision, outcomes, why it fits, who decides, input, the tab of every box. Ask one short question at a time, use the student's own words, and write the answers into `strategy.md`. Never invent them.
- **The data.** The In box gets the data of the dashboard. If `dashboard.html` has no data in it (empty tables, placeholders, data only described), or the data it needs is in other files the student has not given: ask the student for it (a file, or pasted in the chat). If they prefer, add input fields or an editable table to the AI dashboard, so they enter the data there; it is saved in the browser and goes into the In box and the log. Never invent data.

## 2. Map the strategy onto the dashboard, and confirm

Show the student one short mapping and wait for their yes:

- **In box:** which data of the dashboard goes into the strategy, and how it is written as text (`caseText()`). **Only the data**, as in the dinner example (the dishes, the guests, the budget and time): what to do with it belongs in the prompts of the boxes. The same In for every strategy, so the strategies can be compared.
- **Boxes per tab:** a small table from the "Tab of my dashboard" line of every box. A box without a matching tab goes on the tab where its output is used.
- **Out box:** the advice, shown under the flow, mapped to the outcomes. The prompt of the last LLM box must end with `Advice: <outcome>`; if it does not, ask whether you may add that one line.

## 3. Build: the student's dashboard, plus the AI pieces

Start from a copy of `2-manual-dashboard/dashboard.html`. Keep its title, header, colours, fonts, tabs, layout and content. Add to it, taken from `reference/dashboard-template.html` (copy the code; do not rewrite it):

1. **The engine**, copied verbatim: the block from `/* ===== ENGINE START` to `/* ENGINE END */` out of `1-playground/playground.html`. Do not write your own strategy logic.
2. **The strategy**, copied verbatim: `STRATEGY` from the "Boxes" section, prompts exactly as written; `STRATEGY.strategy` is the strategy's name (Single call, Chain, Routing, Parallel, Orchestrator, Critic, Debate), because the log files are named after it. The confirmed mapping goes in `STEP_OF`; `STEPS` lists the dashboard's own tabs (id, number, label) in order.
3. **The AI flow card**, under the tabs: the flow (In to Out, live, with the model of each box in small under its name), and top right: Run shown, Download log, the run **title** box and **Run**. Under the flow: the advice of the run shown, with the field for the student's issues.
4. **In each tab:** the agent card of every box on that tab, on top of the tab's own content (what it says, what it received, and "Prompt and model" to change them). Clicking **In** shows the input of the run, which the student can change.
5. **The conversation panel** ("What the agents say"), next to or under the tab, as the dashboard's layout allows.
6. **Run and log:** `caseText()` from the dashboard's own data, `OUTCOMES` (the outcomes and the words that recognise them in the line `Advice: ...`), the run with its title, the log in the format of `reference/log-format.md`, and the downloads (only when the student clicks Download log, never after every run).

Make the added pieces look like the student's dashboard: map the template's colour tokens (`--page`, `--card`, `--ink`, `--muted`, `--line`, the green, io and code colours) and fonts to the ones of the student's dashboard, and keep their spacing and corners. Keep the flow's meaning of colours (LLM boxes, In/Out, code), in the student's palette. Keep light and dark mode working if their dashboard has them.

Then:

7. **Title:** "<dashboard name> · <strategy name>".
8. **Check** that every tab of the manual dashboard still works and shows the same content, and that the flow, Run, the title box and Download log work.
9. Write the page to `<strategy>/dashboard/dashboard.html`.
10. **Publish** it with the Artifact tool: `capabilities` `{"sample": {}, "downloads": true}`, a short generic `icon`. Write the link to `<strategy>/dashboard/link.md`. To change it later, edit `dashboard.html` and publish again with the link as `url`, so the link stays.

If the manual dashboard cannot carry the pieces (for example it is one long image, or its code cannot be read), say so, and build from `reference/dashboard-template.html` instead, with the student's tabs, data, colours and fonts.

## 4. Hand over

Tell the student in a few lines: the link, the mapping you used, what came from their dashboard and file and what you added, and the next step: the evaluation (`reference/evaluation.md`). In short: change what you want to test yourself (click In, or click a box), give the run a title next to Run (start with "Baseline", about 3 times), and run. Remind them to share the dashboard directly with the people who need to see it, not as a public link.

## Rules

- The same In text in every strategy, so the comparison is fair.
- Tokens are estimates (about 4 characters per token); say so. Show the model that actually answered.
- Plain English, short.
