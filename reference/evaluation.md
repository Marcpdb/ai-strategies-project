# How every evaluation folder works

Used by the `SKILL.md` in every `3-strategies/<strategy>/evaluation/<test>/` folder. The four steps of the AI evaluation (Document, Vary, Compare, Conclude) are spread over these folders:

| Folder | Step | Question |
|---|---|---|
| 1-baseline-stability | Document, Compare (TIA) | What exactly produced this result? Do repeated runs give the same outcome? |
| 2-vary-wording | Vary (systematic prompt variation) | Does changing the order or wording of a prompt change the outcome? |
| 3-vary-fact | Vary (counterfactual prompting) | Does changing one decisive fact change the outcome? |
| 4-vary-boundary | Vary (boundary testing) | With missing or conflicting information, does it flag uncertainty, or make things up? |
| 5-compare-models | Compare (CSA, models) | How do models differ on the same cases? |
| 6-compare-agents | Compare (ISIA, multi-agent only) | Do agents influence each other, and do errors spread? |

Comparing the strategies with each other (CSA) and the conclusion are in `4-compare-and-conclude/`.

## The same three moves in every folder

### 1. Set up (the student says "set up")

- Read `../../export/strategy.md`, `../../dashboard/link.md` and `3-strategies/test-cases.md`. If the strategy's dashboard does not exist yet, stop: it is built first (`SKILL.md` of the strategy folder).
- Agree with the student on **one** change, as the folder's `SKILL.md` describes. Change nothing else.
- Write `plan.md` in the folder, before any run:
  - what is changed, from what to what, and why;
  - the test cases used;
  - the number of runs per test case, set now (at least 3), and that every run is reported.
- If the test needs its own dashboard (every folder except 1 and part of 6): copy `../../dashboard/dashboard.html` to `dashboard.html` in this folder, make exactly the one change, set `VARIATION` to `{type:"<type>",what:"<the change in a few words>"}`, publish it as a separate artifact titled "<dashboard name> · <strategy> · <test>", with the same `capabilities` as the strategy's dashboard (so its runs are saved too), and write the link to `link.md` in this folder.
- Tell the student which link to open, which test cases to run and how many times (use the 3× button). Every run is saved in the dashboard by itself; when they are done, they type "sync". They do not judge runs in the dashboard: that happens in the findings.

### 2. Sync (the student says "sync")

Every run is saved in the test dashboard's own database; "sync" (main `SKILL.md`) reads them into `logs/runs.json` here. For folder 1 the runs come from the strategy's own dashboard and go to `../../dashboard/logs/`.

### 3. Findings (the student says "findings")

Write `findings.md` from the logs, in plain English, short:

- **What was tested:** copied from `plan.md`, with the dates and the models that actually answered.
- **Runs:** a table per test case: run, outcome (`ai_outcome`), and two readings of the output (`ai_output`, and the `steps` where it matters):
  - **flags uncertainty:** yes or no: does the output say what it does not know, or what is missing? Quote the sentence word for word.
  - **adds facts:** yes or no: does the output state facts, numbers or rules that are not in the input (`input`)? Quote them word for word, and say that they are not in the input.
  These readings are yours, not the student's: label the columns "read by Claude", and keep the quotes so the student can check every one.
- **Compared with the baseline:** the same table from `../../dashboard/logs/` (the baseline runs) next to it. Say only what the logs show: how many runs gave the same outcome, where the outcome changed.
- **Open:** runs with an error, fewer runs than planned. Ask the student to run them.
- **The student's conclusion:** an empty section with the folder's question. The student writes it; offer to help them phrase it, never write it for them.

## Rules

- One change at a time; everything else stays the same as the baseline.
- The strategy's own dashboard is only for the baseline. Every change gets its own test dashboard, so the logs never mix.
- Report every run, also the failed ones.
- No anthropomorphism: write "the debater boxes produced", not "the agents argued" or "the agent thought".
- Invented cases only, no real personal data.
- Tokens are estimates (about 4 characters per token).
