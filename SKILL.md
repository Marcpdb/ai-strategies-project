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
  test-cases.md          the test cases, the same for every strategy
  <strategy>/            single-call, chain, routing, parallel, orchestrator, critic, debate
    SKILL.md             builds the AI dashboard of this strategy
    export/strategy.md   the export from the sandbox
    dashboard/           the AI dashboard: dashboard.html, link.md, logs/
    evaluation/<test>/   one folder per test, each with its own SKILL.md
4-compare-and-conclude/  comparing strategies, and the conclusion
reference/               shared instructions, the dashboard template, runs_to_csv.py
```

Never change or delete what the student made: `2-manual-dashboard/`, filled-in `strategy.md` files, `logs/`, `plan.md`, `findings.md`.

## "start"

1. **The playground.** If `1-playground/link.md` has a link, give it. Otherwise publish `1-playground/playground.html` as the student's own artifact with the Artifact tool:
   - `capabilities`: `{"sample": {}, "downloads": true, "db": {"rules": [{"path": "exports", "read": "admin", "write": "owner"}]}, "user": {}}`;
   - `icon`: `flow`; description: "My AI Strategy Playground."

   Write the link to `1-playground/link.md`.
2. **Check** as under "status", and say what is missing.
3. Tell the student the next step in one or two lines: learn the seven strategies in the Playground tab; in the Sandbox load, change and run the ones they choose for the final decision of their workflow; export each one, fill in every _(fill in)_ in the file that opens, save, and type "sync".

## The manual dashboard

The student puts everything from the earlier exercise in `2-manual-dashboard/`: a link, an HTML file, data files, a PDF. What is needed to build on is the dashboard's HTML, as `2-manual-dashboard/dashboard.html`:

- a link (in the chat or in a file there): read the artifact with the Artifact tool and save its full HTML as `dashboard.html`; write the link to `link.md`. If it cannot be read, the student must be its owner: say so.
- an HTML file: use it as `dashboard.html` (copy it; keep the original file).
- only data or a PDF: ask for the link of the dashboard they built. Do not rebuild a dashboard from a PDF.

Read the other files only as background (what the data mean), and never change them.

## "sync"

Do all parts, then say in a few lines what is new and where it went.

1. **Exports.** Read the `exports` collection of the playground (ArtifactData `list`, the link in `1-playground/link.md`). Each document has `file`, `strategy`, `base`, `saved` and `markdown`. The strategy folder follows from `base`: augmented → `single-call`, chain → `chain`, routing → `routing`, parallel → `parallel`, orchestrator → `orchestrator`, evaluator → `critic`, debate → `debate`. If `base` is empty (the sandbox started empty), ask the student which folder it belongs to. Write `markdown` to `3-strategies/<folder>/export/strategy.md`:
   - no file yet, or the file is still exactly what the last sync wrote (see `export/.sync.json`): write it;
   - the student changed the file since: do not overwrite it. Write `export/strategy.new.md` and say which lines differ.

   Keep `export/.sync.json` up to date: the `saved` time and the exact text the last sync wrote. Two exports for one folder: ask which one to use.
2. **Logs.** For every `link.md` under `3-strategies/` (the strategy dashboards and the test dashboards), read the `runs` collection of that dashboard (ArtifactData `list`, all pages; the `out_dir` option keeps large runs out of the chat). Write `logs/runs.json` next to that `link.md`'s folder as `{"strategy": ..., "test": ..., "dashboard": <link>, "synced": <ISO time>, "runs": [...]}`, sorted by `date_time`, then run `python3 reference/runs_to_csv.py <that runs.json>`. For a strategy dashboard the logs go to `dashboard/logs/`; for a test, to `evaluation/<test>/logs/`.
3. **Next step.** For each strategy with a new export: tell the student that the strategy's `SKILL.md` builds its dashboard next ("build the parallel dashboard").

## "status"

A short list:

- playground link: yes or no;
- `2-manual-dashboard/dashboard.html`: yes or no;
- `3-strategies/test-cases.md`: how many test cases;
- per strategy that has an export: export filled in (any _(fill in)_ left?), dashboard link, runs at the last sync, which evaluation folders have a `plan.md` and a `findings.md`;
- the next step.

Strategies without an export are not listed: the student chose others.

## Rules

- Plain English, short. Never invent results, test cases or answers.
- The human decides last: the student accepts or overrides every advice and codes every run. Do not code runs.
- No anthropomorphism ("the agents debated" does not mean they reasoned).
- Dashboards are shared directly with the people who need to see them, not as a public link.
