# AI strategies and AI evaluation

Open this folder in the Code tab of the Claude desktop app and type the words in bold.

1. **start**: you get your own AI Strategy Playground.
2. Put everything from your first exercise in `2-manual-dashboard/`: the link of your dashboard, its data. Or paste the link in the chat.
3. In the playground, learn the seven strategies. In the Sandbox, change and run the ones you choose for the final decision of your workflow. Click Export: fill in every _(fill in)_ in the file that opens, then click Download.
4. **sync**: each strategy file goes to the folder of its strategy in `3-strategies/`.
5. **build the <strategy> dashboard**, for example *build the chain dashboard*. You get an AI version of your dashboard with that strategy.
6. Evaluate each strategy in its `evaluation/` folder, starting with `1-baseline-stability`: **set up**, run the tests in the dashboard, download both log files (CSV and JSON) from the decision tab, **sync**, **findings**.
7. Compare the strategies and conclude in `4-compare-and-conclude/`.

Type **status** at any time to see where you are and what comes next.

## Downloads and sync

The playground and your dashboards are web pages. They cannot save into this folder, so you download files from them, and they land in your Downloads folder. **sync** moves them from Downloads to the right place in this folder. The file names tell it where:

| You download | From | sync moves it to |
|---|---|---|
| `strategy-<name>.md` | Export in the sandbox | `3-strategies/<strategy>/export/strategy.md` |
| `runs-<strategy>-baseline.csv` and `.json` | your strategy's dashboard | `3-strategies/<strategy>/dashboard/logs/` |
| `runs-<strategy>-<test>.csv` and `.json` | a test dashboard | `3-strategies/<strategy>/evaluation/<test>/logs/` |

A log download always holds every run so far, so download again after new runs or after coding them, and sync again.

## Folders

| Folder | What is in it |
|---|---|
| `1-playground/` | the AI Strategy Playground |
| `2-manual-dashboard/` | your first dashboard and its data |
| `3-strategies/` | one folder per strategy: its skill, your strategy file, the AI dashboard, the evaluation |
| `4-compare-and-conclude/` | the comparison of your strategies, and your conclusion |
| `reference/` | shared instructions and the dashboard template |
