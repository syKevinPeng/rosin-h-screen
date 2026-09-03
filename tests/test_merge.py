import csv
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build  # noqa: E402
import merge_scores as ms  # noqa: E402
import order  # noqa: E402

ROWS = ROOT / "rounds" / "round-0" / "rows.json"
D = json.loads(ROWS.read_text(encoding="utf-8"))
V = build.form_version(D)


def records(rater, score):
    """score(atom, is_anchor) -> (h1, h2)."""
    o = order.build_order([r["id"] for r in D["rows"]], D["anchors"], D["anchor_policy"], V, rater)
    out = []
    for pos, x in enumerate(o, 1):
        h1, h2 = score(x["id"], x["is_anchor"])
        out.append({"round": 0, "form_version": V, "rater": rater, "position": pos, "atom": x["id"],
                    "is_anchor": x["is_anchor"],
                    "seen_as_calibration": 1 if (x["is_anchor"] == 0 and x["id"] in D["anchors"]) else 0,
                    "h1": h1, "h2": h2, "note": "a, \"quoted\" note" if pos == 3 else "",
                    "shown_at": "2026-09-04T10:00:00Z", "answered_at": "2026-09-04T10:01:00Z",
                    "started_at": "2026-09-04T09:59:00Z", "finished_at": "2026-09-04T10:30:00Z"})
    return out


def write(tmp, name, recs, fmt):
    p = tmp / f"{name}.{fmt}"
    if fmt == "json":
        p.write_text(json.dumps({"round": 0, "form_version": V, "rater": recs[0]["rater"], "records": recs}),
                     encoding="utf-8")
    else:
        with p.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=build.CSV_COLS, lineterminator="\r\n")
            w.writeheader()
            w.writerows(recs)
    return p


@pytest.mark.parametrize("fmt_a, fmt_b", [("csv", "json"), ("json", "csv"), ("csv", "csv")])
def test_merge_two_raters_counts_and_flags(tmp_path, fmt_a, fmt_b):
    a = write(tmp_path, "v", records("violinist", lambda atom, anc: (4, 4)), fmt_a)
    b = write(tmp_path, "a", records("author", lambda atom, anc: (2 if atom == "bow_accel" else 4, 3)), fmt_b)
    recs, rep = ms.merge([a, b], ROWS)
    n_cards = len(build.cards(D))
    assert len(recs) == 2 * n_cards
    assert all(r["is_anchor"] == 1 for r in recs[:4]) and all(r["is_anchor"] == 0 for r in recs[4:])
    assert recs[4:][0]["atom"] <= recs[4:][1]["atom"]
    n_data = len(D["rows"])
    assert f"H1: all raters exact-agree {n_data - 1}/{n_data} · same direction {n_data - 1}/{n_data}" in rep
    assert f"H2: all raters exact-agree 0/{n_data} · same direction {n_data}/{n_data}" in rep
    assert "direction disagreements: bow_accel" in rep
    assert "flagged seen_as_calibration" in rep and "bow_speed" in rep and "right_wrist_aa_z_dev_deg" in rep
    assert "no kappa" in rep
    out = tmp_path / "scores.csv"
    ms.write_csv(recs, out)
    back = list(csv.DictReader(out.read_text(encoding="utf-8").splitlines()))
    assert len(back) == 2 * n_cards and back[0].keys() == set(build.CSV_COLS)
    assert any(r["note"] == 'a, "quoted" note' for r in back)


def test_multiline_note_survives_csv_roundtrip(tmp_path):
    recs = records("violinist", lambda *_: (4, 4))
    recs[5]["note"] = "line one\nline two, with a comma and \"quotes\""
    p = write(tmp_path, "v", recs, "csv")
    merged, _ = ms.merge([p], ROWS)
    got = [r for r in merged if r["atom"] == recs[5]["atom"] and r["is_anchor"] == recs[5]["is_anchor"]][0]
    assert got["note"] == recs[5]["note"]


def test_refuses_round_mismatch(tmp_path):
    recs = records("violinist", lambda *_: (3, 3))
    for r in recs:
        r["round"] = 1
    p = write(tmp_path, "v", recs, "csv")
    with pytest.raises(ms.MergeError, match="round"):
        ms.merge([p], ROWS)


def test_refuses_version_mismatch(tmp_path):
    recs = records("violinist", lambda *_: (3, 3))
    for r in recs:
        r["form_version"] = "deadbeef0000"
    p = write(tmp_path, "v", recs, "csv")
    with pytest.raises(ms.MergeError, match="form_version"):
        ms.merge([p], ROWS)


def test_refuses_wrong_order(tmp_path):
    recs = records("violinist", lambda *_: (3, 3))
    recs[5]["atom"], recs[6]["atom"] = recs[6]["atom"], recs[5]["atom"]
    p = write(tmp_path, "v", recs, "json")
    with pytest.raises(ms.MergeError, match="position 6"):
        ms.merge([p], ROWS)


def test_refuses_incomplete_and_out_of_range(tmp_path):
    recs = records("author", lambda *_: (3, 3))
    recs[0]["h2"] = ""
    recs[1]["h1"] = 5
    p = write(tmp_path, "a", recs, "csv")
    with pytest.raises(ms.MergeError) as e:
        ms.merge([p], ROWS)
    assert "h2=None" in str(e.value) and "h1=5" in str(e.value)


def test_refuses_unknown_rater_and_duplicate_rater(tmp_path):
    bad = records("author", lambda *_: (3, 3))
    for r in bad:
        r["rater"] = "stranger"
    p = write(tmp_path, "s", bad, "csv")
    with pytest.raises(ms.MergeError, match="unknown rater"):
        ms.merge([p], ROWS)
    a = write(tmp_path, "a1", records("author", lambda *_: (3, 3)), "csv")
    b = write(tmp_path, "a2", records("author", lambda *_: (3, 3)), "json")
    with pytest.raises(ms.MergeError, match="more than one export"):
        ms.merge([a, b], ROWS)


def test_cli_end_to_end(tmp_path):
    a = write(tmp_path, "v", records("violinist", lambda *_: (4, 3)), "csv")
    b = write(tmp_path, "a", records("author", lambda *_: (3, 3)), "json")
    out = tmp_path / "round-0-scores.csv"
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "merge_scores.py"), "--rows", str(ROWS),
                        "--out", str(out), str(a), str(b)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert out.exists() and "wrote" in r.stdout
    r2 = subprocess.run([sys.executable, str(ROOT / "scripts" / "merge_scores.py"), "--rows", str(ROWS),
                         "--out", str(out), str(a), str(a)], capture_output=True, text=True)
    assert r2.returncode == 1 and "REFUSED" in r2.stderr
