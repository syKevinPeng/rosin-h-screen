import csv
import io
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build  # noqa: E402
import merge_scores as ms  # noqa: E402
import order  # noqa: E402

ROWS = ROOT / "rounds" / "round-0" / "rows.json"
D = json.loads(ROWS.read_text(encoding="utf-8"))
V = build.form_version(D)


def payload(rater, note=""):
    o = order.build_order([r["id"] for r in D["rows"]], D["anchors"], D["anchor_policy"], V, rater)
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=build.CSV_COLS, lineterminator="\r\n")
    w.writeheader()
    for pos, x in enumerate(o, 1):
        w.writerow({"round": 0, "form_version": V, "rater": rater, "position": pos, "atom": x["id"], "is_anchor": x["is_anchor"],
                    "seen_as_calibration": 1 if (x["is_anchor"] == 0 and x["id"] in D["anchors"]) else 0,
                    "h1": 4, "h2": 3, "note": note if pos == 3 else "", "shown_at": "", "answered_at": "",
                    "started_at": "2026-09-04T10:00:00Z" if pos == 1 else "", "finished_at": "2026-09-04T10:30:00Z" if pos == 1 else ""})
    return buf.getvalue()


def write_sheet(path, rows):
    with path.open("w", newline="", encoding="utf-8-sig") as f:   # BOM, like Google's export
        w = csv.writer(f)
        w.writerow(["Timestamp", "Email Address", "Survey Response"])
        w.writerows(rows)


def test_sheet_to_exports_handles_multiline_bom_repeats_and_junk(tmp_path):
    sheet = tmp_path / "responses.csv"
    write_sheet(sheet, [
        ["2026/09/04 10:31:00", "a@example.com", payload("author", "first try")],
        ["2026/09/04 10:40:00", "x@example.com", "hello, this is not an answer file"],
        ["2026/09/04 11:00:00", "v@example.com", payload("violinist", "a note,\nwith \"quotes\" and a newline")],
        ["2026/09/04 11:20:00", "a@example.com", payload("author", "edited later")],
    ])
    out = tmp_path / "exports"
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "from_google_sheet.py"), str(sheet), "--out", str(out)],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert "row 2: not an answer file" in r.stderr and "submitted again" in r.stderr
    files = sorted(p.name for p in out.iterdir())
    assert files == [f"author-{V}.csv", f"author-{V}.meta.json", f"violinist-{V}.csv", f"violinist-{V}.meta.json"]
    meta = json.loads((out / f"author-{V}.meta.json").read_text())
    assert meta["sheet_row"] == 4 and meta["email"] == "a@example.com" and meta["n_records"] == len(build.cards(D))
    merged, rep = ms.merge([out / f"author-{V}.csv", out / f"violinist-{V}.csv"], ROWS)
    assert len(merged) == 2 * len(build.cards(D))
    notes = {r["note"] for r in merged if r["note"]}
    assert notes == {"edited later", "a note,\nwith \"quotes\" and a newline"}
