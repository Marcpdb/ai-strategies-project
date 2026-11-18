# AI strategies and AI evaluation

Open this folder in the Code tab of the Claude desktop app and type the words in bold.

1. **start**: you get your own AI Strategy Playground.
2. Paste the link of your first dashboard (a Claude artifact) in the chat, or put it in `2-manual-dashboard/link.md`, with its data. Your AI dashboards keep its look and layout.
3. In the playground, learn the strategies: all of them decide on the same dinner workflow, Dishes → Guests → Budget & time → Choose (`reference/workflow.png`). Choose **5 strategies** for the final decision of your workflow (the two Debate examples count as one). In the Sandbox, load each one as a template (only its boxes and arrows), write your own input and prompts for your workflow, and run it. Click Export: fill in every _(fill in)_ in the file that opens, then click Download.
4. **sync**: each strategy file goes to the folder of its strategy in `3-strategies/`.
5. **build the <strategy> dashboard**, for example *build the chain dashboard*. You get an AI version of your dashboard with that strategy.
6. Evaluate each AI dashboard by hand, with the methods from class (document, vary input, vary system). Change what you want to test yourself: click **In** to change the input, click a box to change its prompt or model. Give the run a title in the box next to **Run** (start with *Baseline*, about 3 times), and run. Everything is logged; click **Download log** when you are done running, then type **sync**, and when you have run what you want to evaluate, **findings**: Claude groups your runs by title, codes every run and writes one `findings.md` per title, which you check.
7. Compare the strategies and conclude in `4-compare-and-conclude/`.

Type **status** at any time to see where you are and what comes next.

## Downloads and sync

The playground and your dashboards are web pages. They cannot save into this folder, so you download files from them, and they land in your Downloads folder. **sync** copies them from Downloads to the right place in this folder (the files stay in Downloads as a backup). The file names tell it where:

| You download | From | sync copies it to |
|---|---|---|
| `strategy-<name>.md` | Export in the sandbox | `3-strategies/<strategy>/export/strategy.md` |
| `runs-<strategy>-<date>-<time>.csv` and `.json` | **Download log** in your strategy's dashboard | `3-strategies/<strategy>/dashboard/logs/` (the newest as `runs.csv` / `runs.json`, every download in `logs/downloads/`) |

A log download always holds every run so far, and every download gets its own name (date and time), so nothing is overwritten. Download when you are done running, then sync.

## Folders

| Folder | What is in it |
|---|---|
| `1-playground/` | the AI Strategy Playground |
| `2-manual-dashboard/` | your first dashboard and its data |
| `3-strategies/` | one folder per strategy: its skill, your strategy file, the AI dashboard, the findings per run title |
| `4-compare-and-conclude/` | the comparison of your strategies, and your conclusion |
| `reference/` | shared instructions, the dashboard template, and the workflow image (`workflow.png`) |
