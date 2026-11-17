"""Turn a dashboard's runs.json into runs.csv, with the log columns.

Usage: python3 reference/runs_to_csv.py 3-strategies/parallel/dashboard/logs/runs.json
Writes runs.csv next to it.
"""
import csv, json, sys
from pathlib import Path

COLS = ["run_id", "date_time", "source", "strategy", "strategy_version", "test_case", "input",
        "variation_type", "what_changed", "repeat_no", "models_asked", "models_answered",
        "ai_output", "ai_outcome", "user_choice", "override_to", "override_reason", "verdict",
        "uncertainty_flagged", "fabricated", "coder_note", "calls", "tokens_est", "seconds", "error"]

src = Path(sys.argv[1])
data = json.loads(src.read_text(encoding="utf-8"))
runs = data["runs"] if isinstance(data, dict) else data
runs = sorted(runs, key=lambda r: r.get("date_time", ""))
out = src.with_suffix(".csv")
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(COLS)
    for r in runs:
        w.writerow(["" if r.get(c) is None else r.get(c) for c in COLS])
print(f"{len(runs)} runs -> {out}")
