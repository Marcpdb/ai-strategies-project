# How the evaluation works

Used when the student says "findings", or asks about the evaluation of a strategy. The student evaluates every AI dashboard **by hand**, with the evaluation methods from the theory class. The dashboard changes nothing by itself: it runs, documents and logs.

## The methods (from the theory class)

| Step | Method | Key question |
|---|---|---|
| 1 Document | date, time, run number, AI strategy, model(s), prompt(s), input dataset, settings, trace, final output and decision, tokens, time, issues | What exactly produced this result? |
| 2 Vary input | prompt: wording, order, … · input: decisive fact, missing or conflicting information, … | How stable is the outcome of the followed AI strategy? How certain is the outcome from the input? |
| 3 Vary system | repeated runs (TIA) · strategies and models (CSA) · agents (ISIA) | Does the outcome depend on what processes it? |

Step 1 happens for every run, automatically: the dashboard logs all of it (`reference/log-format.md`).

## 1. Run (in the dashboard)

- **Change** what the method needs, by hand: click a box in the flow to change its prompt or model; click **In** to change the input of the run (by default the data of the tabs). Changed boxes say "changed" in the flow; "Back to the original" undoes a change.
- **Title** the run in the small box next to Run, for example "Baseline", "Vary input: budget €20", "Vary system: Opus for every box". Runs with the same title belong together: run each one about 3 times.
- **Run.** The dashboard logs the run with its title and with what differs from the original (`changes_detected`). Under the advice, the student can write the issues they noticed; they go into the log too.

After each run the log is downloaded (CSV and JSON, every run so far; **Download log** does the same by hand). The student types "sync": the files go to `3-strategies/<strategy>/dashboard/logs/` as `runs.csv` and `runs.json`.

Advice for the student (say it when they ask what to run): first about 3 runs titled "Baseline" with nothing changed; then one change at a time, about 3 runs per title; the same input in every strategy dashboard when comparing strategies.

## 2. Findings (the student says "findings")

Read `3-strategies/<strategy>/dashboard/logs/runs.json` and group the runs without an error by `title`.

1. **Name the method of every title.** From the title and `changes_detected`, say for each title which step and method of the table above it is (for example "Vary input: budget €20" → 2 Vary input, decisive fact). Show this short list and let the student correct it before you write. A title whose runs have different changes (different `changes_detected` or `input`) holds more than one test: say so, and ask whether to split it.
2. **Find the baseline:** the title with nothing changed (`changes_detected` "none"). If there is none, say so and stop: every test is compared with the baseline.
3. **Write one `findings.md` per title**, in `3-strategies/<strategy>/evaluation/<title in lower case, joined with ->/findings.md` (for example `evaluation/vary-input-budget-20/findings.md`), in plain English, short:
   - **What was tested:** the title, the step and method (as confirmed), the key question of that step, what differed from the original (`changes_detected`), the dates, and the models that actually answered (`models_answered`).
   - **Runs, coded:** a table: run, outcome (`ai_outcome`), the student's issues (`issues`), and your coding of each run from its `ai_output`, `input` and `steps`:
     - **verdict:** correct, partly, wrong or unsure, judged against the input and the workflow in `3-strategies/<strategy>/export/strategy.md`, with one line why;
     - **flags uncertainty:** yes or no, with the sentence that shows it, quoted word for word;
     - **makes things up:** yes or no: a fact in the output that is not in the input, quoted word for word.
     Mark the coding as Claude's, and invite the student to check it and change what they disagree with.
   - **Compared with the baseline** (not in the baseline's own file): the baseline runs next to them. Say only what the log shows: how many runs gave the same outcome, where the outcome changed. With fewer than 3 runs, say that so few runs cannot show stability.
   - **Open:** runs with an error, and runs you could not judge (say why).
   - **The student's conclusion:** an empty section with the key question of the step. The student writes it; offer to help them phrase it, never write it for them.

What to look at per method:

- **Baseline, repeated runs (TIA):** how many runs gave the same outcome, and where the outputs differ.
- **Prompt and input changes:** did the outcome follow the change? With missing or conflicting information: did it flag uncertainty, or make something up?
- **Models (CSA):** which models were asked and which answered; how the outcomes differ.
- **Strategies (CSA):** compared across dashboards in "compare".
- **Agents (ISIA):** read the `steps`: what the changed box produced, what the boxes after it received, and whether its error reached the final output.

Existing `findings.md` files hold the student's checks and conclusions: never overwrite them. When new runs came in for a title that already has findings, add a section "New runs" under the existing text.

## 3. What comes next (always say this after findings)

The student evaluates every strategy they chose: every strategy with an `export/strategy.md`. After writing findings, look at the others and tell the student the next step in one or two lines:

- a strategy with an export but no dashboard yet: "build the <strategy> dashboard";
- a strategy with a dashboard but no baseline runs in its log: run the baseline there first;
- a strategy with runs but without findings: "findings for <strategy>";
- every strategy with findings: "compare" (`4-compare-and-conclude/`).

## Rules

- One change at a time; the student makes it, not Claude. Never change a student's dashboard to run an evaluation for them.
- Report every run, also the failed ones.
- No anthropomorphism: write "the debater boxes produced", not "the agents argued" or "the agent thought".
- Invented data only, no real personal data.
- Tokens are estimates (about 4 characters per token).
