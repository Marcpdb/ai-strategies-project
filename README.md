# AI strategies and AI evaluation

Open this folder in the Code tab of the Claude desktop app and type the words in bold.

1. **start**: you get your own AI Strategy Playground.
2. Put everything from your first exercise in `2-manual-dashboard/`: the link of your dashboard, its data. Or paste the link in the chat.
3. In the playground, learn the seven strategies. In the Sandbox, change and run the ones you choose for the final decision of your workflow. Click Export: fill in every _(fill in)_ in the file that opens, then click Download.
4. **sync**: each strategy file goes to the folder of its strategy in `3-strategies/`.
5. **build the <strategy> dashboard**, for example *build the chain dashboard*. You get an AI version of your dashboard with that strategy.
6. Evaluate each strategy in its `evaluation/` folder, starting with `1-baseline-stability`: **set up**, run the tests in the dashboard, **sync**, **findings**. You only run; the findings skill reads the runs for you.
7. Compare the strategies and conclude in `4-compare-and-conclude/`.

Type **status** at any time to see where you are and what comes next.

## Keep your work private

This folder fills up with your own work: your dashboard and its data, your strategy files, your run logs and findings. Keep it on your computer, or in a **private** repository. Never push it to a public GitHub repository, and never make a public copy (fork) of it. The same goes for your dashboards and your playground: they are private pages; share them only directly with the people who need to see them, never as a public link.

## Downloads and sync

The playground and your dashboards are web pages. They cannot save into this folder. **sync** brings what they made to the right place:

| What | From | sync puts it in |
|---|---|---|
| `strategy-<name>.md` (you download it) | Export in the sandbox | `3-strategies/<strategy>/export/strategy.md` |
| your runs (saved by the dashboard itself) | your strategy's dashboard | `3-strategies/<strategy>/dashboard/logs/runs.json` |
| your runs (saved by the dashboard itself) | a test dashboard | `3-strategies/<strategy>/evaluation/<test>/logs/runs.json` |

You never download runs: every run is saved in the dashboard, and sync fetches all of them. ("Download runs" is only a backup; sync picks that file up from Downloads too.)

## Folders

| Folder | What is in it |
|---|---|
| `1-playground/` | the AI Strategy Playground |
| `2-manual-dashboard/` | your first dashboard and its data |
| `3-strategies/` | one folder per strategy: its skill, your strategy file, the AI dashboard, the evaluation |
| `4-compare-and-conclude/` | the comparison of your strategies, and your conclusion |
| `reference/` | shared instructions and the dashboard template |
