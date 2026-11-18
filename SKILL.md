---
name: ai-strategies-project
description: "The main skill of the AI strategies project folder. Use when a student starts the project, asks for the playground, syncs, gives their manual dashboard, or asks what to do next."
---

# AI strategies project: the main skill

The student adds AI strategies to the final decision of their own workflow dashboard (their "manual dashboard", from an earlier exercise) and evaluates them. This skill knows the whole project. It checks that everything is there, gives the playground, and hands every export to the folder of its strategy. The work inside a strategy folder is done by that folder's `SKILL.md`.

## The folder

```text
1-playground/            the AI Strategy Playground
2-manual-dashboard/      everything from the earlier exercise: the dashboard, its data
3-strategies/
  <strategy>/            single-call, chain, routing, parallel, orchestrator, critic, debate
    SKILL.md             builds the AI dashboard of this strategy
    export/strategy.md   the export from the sandbox
    dashboard/           the AI dashboard: dashboard.html, link.md, logs/ (every run)
    evaluation/<title>/  one folder per run title the student used, with findings.md
4-compare-and-conclude/  comparing strategies, and the conclusion
reference/               shared instructions, the dashboard template and the workflow image
```

Never change or delete what the student made: `2-manual-dashboard/`, filled-in `strategy.md` files, `logs/`, `findings.md`.

## "start"

1. **The playground.** If `1-playground/link.md` has a link, give it. Otherwise publish `1-playground/playground.html` as the student's own artifact with the Artifact tool:
   - `capabilities`: `{"sample": {}, "downloads": true}`;
   - `icon`: `flow`; description: "My AI Strategy Playground."

   Write the link to `1-playground/link.md`.
2. **Check** as under "status", and say what is missing.
3. Tell the student the next step in one or two lines: look at the example dashboard in the Dinner planner tab (the workflow Dishes, Guests, Budget & time, Choose; `reference/workflow.png` shows it), then learn the strategies in the Playground tab, which all make the decision of that dashboard; in the Sandbox load, change and run the ones they choose for the final decision of their workflow; export each one, fill in every _(fill in)_ in the file that opens, click Download, and type "sync".

## The manual dashboard

The student gives the link of the dashboard they built in the earlier exercise: a Claude artifact link (claude.ai/…/artifact/…), in the chat or in `2-manual-dashboard/link.md`. They may also put data files, notes or a PDF in `2-manual-dashboard/`. Every AI dashboard is built on this dashboard: its look, layout, tabs and data.

- **The link:** read the artifact with the Artifact tool (`action: "read"`) and save its full HTML as `2-manual-dashboard/dashboard.html`; write the link to `link.md`. When the student owns the artifact, the read gives the full HTML. If it gives only a summary (the artifact belongs to another account), say so: the student opens Claude Code with the account that made it, or downloads the HTML from the artifact page and puts it in `2-manual-dashboard/`.
- **An HTML file:** use it as `dashboard.html` (copy it; keep the original file).
- **Only data or a PDF:** ask for the link of the dashboard they built. Do not rebuild a dashboard from a PDF.
- **The data.** Check that the dashboard holds the data of the workflow (not empty tables or placeholders). If it does not, and the data is not in the other files either: ask the student for it now (a file, or pasted in the chat), or tell them they can enter it in the AI dashboard, which then gets input fields for it (`reference/build-dashboard.md`).

Read the other files only as background (what the data mean), and never change them.

## "sync"

The playground and the dashboards are web pages: they cannot write into this folder. The student downloads files from them (the browser puts them in the Downloads folder), and "sync" moves them here. Look in `~/Downloads` for the files below, take the newest of each name (the browser adds " (1)", " (2)" to repeated downloads), move it, and remove the older copies of that name from Downloads. Then say in a few lines what moved where, and what is still missing.

1. **Strategy files** `strategy-<name>.md` (from Export in the sandbox). The folder follows from the line "Based on: <strategy>." in the file: Single call → `single-call`, Chain → `chain`, Routing → `routing`, Parallel → `parallel`, Orchestrator → `orchestrator`, Critic → `critic`, Debate (steps) or Debate (dishes) → `debate`. No such line (the sandbox started empty): ask the student which strategy it is. Move it to `3-strategies/<folder>/export/strategy.md`. If that file exists and is different, do not overwrite it: ask the student which one to keep, and show which lines differ. Two new files for one strategy: ask which one.
2. **Run logs** `runs-<strategy>.csv` and `.json` (from **Download log** at the top right of a dashboard). They hold every run of that dashboard, each with the title the student gave it. Move them to `3-strategies/<strategy>/dashboard/logs/` as `runs.csv` and `runs.json`. A newer download replaces the older one: the dashboard always downloads every run so far.
3. **Missing:** a dashboard with a link but no log yet, or a log whose newest run is older than the student's last session. Remind them to click Download log in that dashboard.
4. **Next step.** For each strategy with a new strategy file: the strategy's `SKILL.md` builds its dashboard next ("build the parallel dashboard"). For each strategy whose log has new runs: "findings" when the student has run what they want to evaluate (at least about 3 runs titled Baseline). When every strategy with an export has its findings: "compare". Until then, name the strategy that comes next, as in "What comes next" in `reference/evaluation.md`.

## "status"

A short list:

- playground link: yes or no;
- `2-manual-dashboard/dashboard.html`: yes or no;
- per strategy that has an export: export filled in (any _(fill in)_ left?), dashboard link, the run titles in the log at the last sync with the number of runs of each, which evaluation folders have a `findings.md`;
- the next step: the next strategy to build, run or write findings for, and "compare" only when every strategy with an export has its findings.

Strategies without an export are not listed: the student chose others.

## Rules

- Plain English, short. Never invent results or answers.
- The evaluation is done by the student, by hand: they change the input or a box themselves and title every run. The findings step groups the runs by title, codes every run (verdict, flags uncertainty, makes things up) with quotes as evidence, marked as Claude's coding; the student checks it and writes the conclusions.
- No anthropomorphism ("the agents debated" does not mean they reasoned).
- Dashboards are shared directly with the people who need to see them, not as a public link.
