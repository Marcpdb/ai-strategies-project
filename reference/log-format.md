# Run log format (the same in every dashboard)

One row per run. Every dashboard writes it, so the CSV files of all strategies can be put together in one sheet. The dashboard downloads them automatically after each test (and with **Download log**). The two downloads are named `runs-<strategy>.csv` and `.json` and hold every run of that dashboard: free runs and every evaluation test. "sync" moves them to `3-strategies/<strategy>/dashboard/logs/` as `runs.csv` and `runs.json`.

The JSON download has the same fields per run plus `steps` (every step: what went in, the full prompt, what came out, the model asked for, the model that answered, the time), and at the top: `tests` (the tests of this dashboard), `runs_per_test` (3), `evaluation_input` (the input fixed at the first test run) and `variations` (per test, the change that was made).

The columns follow the four steps of the AI evaluation.

## 1. Document (what exactly produced this result?)

| Column | Meaning |
|---|---|
| run_id | D001, D002, … per dashboard |
| date_time | ISO date and time of the run |
| source | dashboard |
| strategy | the strategy name |
| strategy_version | a short code of the strategy as built (boxes, prompts, models, lines) |
| run_version | the same code for what actually ran: it differs from strategy_version when a test changed prompts or models |
| input | the exact text of the In box |
| models_asked | the models named in the boxes |
| models_answered | the models that actually answered (a named model that is not available is replaced by one of the same tier) |
| calls, tokens_est, seconds | number of calls to Claude, estimated tokens (about 4 characters per token), time |
| error | empty, or why the run stopped |

## 2. Vary (does the outcome change?)

| Column | Meaning |
|---|---|
| variation_type | set by the dashboard: `run` (a free run, not part of the evaluation), `baseline`, `wording`, `fact`, `boundary`, `model`, `agents` |
| what_changed | the change, written by the dashboard, e.g. "budget €500 → €400" |
| extra_prompt | the extra prompt that made the change (empty for baseline and model) |
| extra_output | what that extra call returned |

## 3. Compare (are results consistent, and how do they differ?)

| Column | Meaning |
|---|---|
| repeat_no | 1, 2 or 3: which run of this test it is. Repeats are the basis for stability (TIA) |
| ai_output | the full answer that reached Out |
| ai_outcome | the outcome read from the line `Advice: <outcome>` |

Comparing strategies or models (CSA): put the CSV files of all dashboards together and compare `ai_outcome` per `variation_type`. Agent interaction (ISIA): read the `steps` in the JSON file: what each box received from the others and what it produced.

## 4. Conclude (coding)

The log has no coding columns. Each run is coded in `findings.md` by the findings step: verdict (correct, partly, wrong, unsure), flags uncertainty (yes/no), makes things up (yes/no), each with a quote from the output. The student checks that coding and can change it there.
