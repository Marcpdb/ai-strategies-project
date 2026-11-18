# Run log format (the same in every dashboard)

One row per run. Every dashboard writes it, so the CSV files of all strategies can be put together in one sheet. The dashboard downloads them automatically after each run (and with **Download log**). The two downloads are named `runs-<strategy>.csv` and `.json` and hold every run of that dashboard. "sync" moves them to `3-strategies/<strategy>/dashboard/logs/` as `runs.csv` and `runs.json`.

The JSON download has every column below per run, plus `settings` (every box: type, model, effort, tools, prompt, rounds), `steps` (the full trace: every box, what went in, the full prompt, what came out, the model asked and the model that answered, the time) and `transcript` (the debate). At the top: `original_input` and `original_boxes` (the strategy as built, before any change).

## What is stored for every run

| Column | Meaning |
|---|---|
| run_id | the run number: D001, D002, … per dashboard |
| date, time | the date and the local time of the run (`date_time` in the JSON: ISO, UTC) |
| source | dashboard |
| strategy | the AI strategy |
| strategy_version | a short code of the strategy as built (boxes, prompts, models, lines) |
| run_version | the same code for what actually ran: it differs from strategy_version when the student changed a prompt or a model |
| models_asked | the models named in the boxes |
| models_answered | the models that actually answered (a named model that is not available is replaced by one of the same tier) |
| prompts | the prompt of every box, as it ran: `[Box]` then its prompt |
| settings_text | per box: type, model, effort, tools, rounds or maximum words |
| input | the input dataset: the exact text of the In box |
| ai_output | the full final output that reached Out |
| ai_outcome | the decision, read from the line `Advice: <outcome>` |
| tokens_est, seconds, calls | estimated tokens (about 4 characters per token), time, number of calls to Claude |
| trace | every step in order: `[Box · round · model]` then what it produced (the full trace with inputs and prompts is in `steps` in the JSON) |
| error | empty, or why the run stopped |
| issues | what the student noticed about this run, written under its advice |

## The evaluation of the run

| Column | Meaning |
|---|---|
| title | the title the student gave the run, next to Run (for example "Baseline", "Vary input: budget €20"). Runs with the same title belong together |
| changes_detected | what the dashboard found different from the original: the input, the prompt or model of a box ("none" when nothing) |
| repeat_no | 1, 2, 3, …: the how-manieth run with the same title, the same boxes (run_version) and the same input. Repeats are the basis for stability (TIA) |

## Using the log

- Stability (TIA): runs with the same `title`, `run_version` and `input`; compare `ai_outcome`.
- Strategies or models (CSA): put the CSV files of all dashboards together and compare `ai_outcome` per `title`, on the same `input`.
- Agent interaction (ISIA): read `steps` in the JSON: what each box received from the others and what it produced.
- Coding (verdict, flags uncertainty, makes things up) is not in the log: the findings step writes it in `findings.md`, and the student checks it there.
