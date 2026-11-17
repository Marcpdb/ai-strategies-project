# Run log format (the same in every dashboard)

One row per run, written by every dashboard (`source` = dashboard), so students can put the CSV files of their three dashboards together in one sheet. The two downloads are named `runs-<strategy>-<test>.csv` and `.json`; "sync" moves them to the right `logs/` folder. The JSON download has the same fields plus `steps`: every step of the run with what went in, what came out, the model asked for, the model that answered, and the time. (The sandbox keeps its last 30 runs with the same fields and steps, and downloads them as JSON.)

The columns follow the four steps of the AI evaluation.

## 1. Document (what exactly produced this result?)

| Column | Meaning |
|---|---|
| run_id | D001, D002, … per dashboard |
| date_time | ISO date and time of the run |
| source | sandbox or dashboard |
| strategy | the strategy name from the file |
| strategy_version | a short code of the whole setup (boxes, prompts, models, lines). It changes when anything in the strategy changes |
| test_case | which test case (or "In box" / "own input") |
| input | the exact text of the In box |
| models_asked | the models named in the boxes |
| models_answered | the models that actually answered (a named model that is not available is replaced by one of the same tier) |
| calls, tokens_est, seconds | number of calls to Claude, estimated tokens (about 4 characters per token), time |
| error | empty, or why the run stopped |

## 2. Vary (does the outcome change?)

| Column | Meaning |
|---|---|
| variation_type | filled in by the student in their sheet: baseline, repeat, wording (wording or order), fact (a decisive fact: counterfactual), boundary (missing or conflicting information), model, strategy, other |
| what_changed | typed before the run in "What did you change?", e.g. "Ben: Haiku → Sonnet" |

## 3. Compare (are results consistent, and how do they differ?)

| Column | Meaning |
|---|---|
| repeat_no | how many runs with the same strategy_version and the same input there are, this one included. Repeats are the basis for stability (TIA) |
| ai_output | the full answer that reached Out |
| ai_outcome | the outcome read from the line `Advice: <outcome>` |

Comparing strategies or models (CSA): put the CSV files of all dashboards together and compare `ai_outcome` per `test_case`. Agent interaction (ISIA): read the `steps` in the JSON file: what each agent received from the others and what it said.

## 4. Conclude (code every run)

| Column | Meaning |
|---|---|
| user_choice | accepted or overridden (dashboards) |
| override_to, override_reason | the outcome the student chose instead, and why |
| verdict | the student's coding: correct, partly, wrong, unsure |
| uncertainty_flagged | yes or no: does the answer say what it does not know? |
| fabricated | yes or no: does it make up facts that are not in the input? |
| coder_note | a short note |
