# How the evaluation works

Used by the `SKILL.md` in every `3-strategies/<strategy>/evaluation/<test>/` folder. The evaluation is run from the strategy's own dashboard: next to **Run** there is one button per test. Each test makes **one** change automatically (with an extra prompt the student can read and edit before the first run), runs **3 times** on the same input, and logs everything. Nothing is set up by hand, and there are no separate test dashboards.

| Folder | Button | Step | Question | What the button changes |
|---|---|---|---|---|
| 1-baseline-stability | Baseline | Document, Compare (TIA) | What exactly produced this result? Do repeated runs give the same outcome? | Nothing |
| 2-vary-wording | Wording | Vary (systematic prompt variation) | Does changing the order or wording of the prompts change the outcome? | One extra call rewords every prompt, same meaning |
| 3-vary-fact | Fact | Vary (counterfactual prompting) | Does changing one decisive fact change the outcome? | One extra call changes one decisive fact in the input |
| 4-vary-boundary | Boundary | Vary (boundary testing) | With missing or conflicting information, does it flag uncertainty, or make things up? | One extra call removes one piece of information, or adds a contradiction |
| 5-compare-models | Models | Compare (CSA, models) | How do models differ on the same case? | Every box one model up: Haiku → Sonnet, Sonnet → Opus, Opus → Sonnet |
| 6-compare-agents | Agents | Compare (ISIA, multi-agent only) | Do the boxes influence each other, and do errors spread? | One extra call picks one box that passes its answer on, and gives it one wrong fact |

The input is fixed at the first test run: every test uses the same data of the dashboard (the fact and boundary tests change that same input). Single call has no Agents test.

Comparing the strategies with each other (CSA) and the conclusion are in `4-compare-and-conclude/`.

## 1. Run (in the dashboard)

The student clicks each test button, reads the extra prompt (and may change it before the first run of that test), and clicks Run. Each test runs 3 times. On the last tab they code every run: verdict, flags uncertainty, makes things up, and a note. When every test has 3 runs, the dashboard says so. They download both log files (CSV and JSON) and type "sync": the files go to `../../dashboard/logs/` as `runs.csv` and `runs.json`.

## 2. Findings (the student says "findings")

**Only when every test is done.** Read `../../dashboard/logs/runs.json`. Its `tests` lists the tests of this dashboard. Every one of them needs at least 3 runs without an error. If not, say which tests still miss runs, and stop: no findings until all tests of this dashboard are done.

Then write `findings.md` in every test folder of this strategy, in plain English, short:

- **What was tested:** the question, the change as logged (`what_changed`, and for an extra call `extra_prompt` and `extra_output`), the dates, the input, and the models that actually answered (`models_answered`).
- **Runs:** a table: run, outcome (`ai_outcome`), the student's coding (verdict, uncertainty flagged, fabricated).
- **Compared with the baseline:** the baseline runs next to them (not in folder 1). Say only what the log shows: how many runs gave the same outcome, where the outcome changed.
- **Open:** runs that are not coded yet, runs with an error. Ask the student to code them; never code runs yourself.
- **The student's conclusion:** an empty section with the folder's question. The student writes it; offer to help them phrase it, never write it for them.

Each test folder's `SKILL.md` says what its findings look at in particular.

## Rules

- One change per test; everything else stays the same as the baseline. The dashboard does this: do not change prompts or models by hand during the evaluation.
- Report every run, also the failed ones.
- No anthropomorphism: write "the debater boxes produced", not "the agents argued" or "the agent thought".
- Invented data only, no real personal data.
- Tokens are estimates (about 4 characters per token).
