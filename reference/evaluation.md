# How the evaluation works

Used by the `SKILL.md` in every `3-strategies/<strategy>/evaluation/<test>/` folder. The evaluation is run from the strategy's own dashboard: next to **Run** (top right) there is a small dropdown with the tests and a **Run test** button. Each test makes **one** change automatically (with an extra prompt the student can read and edit before the first run), runs **3 times** on the same input, and logs everything. Nothing is set up by hand, and there are no separate test dashboards.

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

The student picks each test in the dropdown, may open the line under it to read or change the extra prompt (before the first run of that test), and clicks **Run test**. Each test runs 3 times. The advice of the run shown is under the flow. When every test has 3 runs, the dashboard says so. They click **Download log** (CSV and JSON) and type "sync": the files go to `../../dashboard/logs/` as `runs.csv` and `runs.json`. Nothing is coded in the dashboard: the findings do that.

## 2. Findings (the student says "findings")

**Only when every test is done.** Read `../../dashboard/logs/runs.json`. Its `tests` lists the tests of this dashboard. Every one of them needs at least 3 runs without an error. If not, say which tests still miss runs, and stop: no findings until all tests of this dashboard are done.

Then write `findings.md` in every test folder of this strategy, in plain English, short:

- **What was tested:** the question, the change as logged (`what_changed`, and for an extra call `extra_prompt` and `extra_output`), the dates, the input, and the models that actually answered (`models_answered`).
- **Runs, coded:** a table: run, outcome (`ai_outcome`), and your coding of each run from its `ai_output`, `input` and `steps`:
  - **verdict:** correct, partly, wrong or unsure, judged against the input and the workflow in `../../export/strategy.md`, with one line why;
  - **flags uncertainty:** yes or no, with the sentence that shows it, quoted word for word;
  - **makes things up:** yes or no: a fact in the output that is not in the input, quoted word for word.
  Mark the coding as Claude's, and invite the student to check it and change what they disagree with.
- **Compared with the baseline:** the baseline runs next to them (not in folder 1). Say only what the log shows: how many runs gave the same outcome, where the outcome changed.
- **Open:** runs with an error, and runs you could not judge (say why).
- **The student's conclusion:** an empty section with the folder's question. The student writes it; offer to help them phrase it, never write it for them.

Each test folder's `SKILL.md` says what its findings look at in particular.

## 3. What comes next (always say this after findings)

The student evaluates every strategy they chose: every strategy with an `export/strategy.md`. After writing the findings of one strategy, look at the others and tell the student the next step in one or two lines:

- a strategy with an export but no dashboard yet: "build the <strategy> dashboard";
- a strategy with a dashboard whose tests are not all done: which tests still need runs, in that dashboard;
- a strategy whose tests are done but without findings: "findings for <strategy>";
- every strategy done, with findings: "compare" (`4-compare-and-conclude/`).

Never suggest comparing or concluding while a chosen strategy is not done.

## Rules

- One change per test; everything else stays the same as the baseline. The dashboard does this: do not change prompts or models by hand during the evaluation.
- Report every run, also the failed ones.
- No anthropomorphism: write "the debater boxes produced", not "the agents argued" or "the agent thought".
- Invented data only, no real personal data.
- Tokens are estimates (about 4 characters per token).
