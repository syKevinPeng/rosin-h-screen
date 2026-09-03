#!/usr/bin/env python3
"""Merge per-rater H-screen exports into the round's committed score file.

    python scripts/merge_scores.py --rows rounds/round-0/rows.json \
        --out /path/to/round-0-scores.csv EXPORT [EXPORT ...]

EXPORT is a CSV or JSON file downloaded from the page (one per rater).
Checks, all fatal: form_version matches rows.json; rater is registered; every
card is present exactly once with h1 and h2 in 1..4; the positions are exactly
the order the frozen page shows that rater (recomputed with scripts/order.py).

Writes the merged CSV (calibration rows first, then by atom, then rater) and
prints RAW AGREEMENT COUNTS only. No kappa, no CVR, by design: D-M6 runs the
H screen in preliminary mode and those statistics are not computed even for
information.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import CSV_COLS, form_version  # noqa: E402
from order import build_order  # noqa: E402

INT_COLS = ("round", "position", "is_anchor", "seen_as_calibration", "h1", "h2")


class MergeError(Exception):
    pass


def load_export(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() == ".json":
        obj = json.loads(text)
        recs = obj["records"] if isinstance(obj, dict) else obj
    else:
        recs = list(csv.DictReader(io.StringIO(text, newline="")))
    out = []
    for r in recs:
        row = {c: r.get(c, "") for c in CSV_COLS}
        for c in INT_COLS:
            v = row[c]
            row[c] = None if v in ("", None) else int(v)
        out.append(row)
    return out


def check_export(recs: list[dict], data: dict, version: str, src: str) -> list[str]:
    errs = []
    if not recs:
        return [f"{src}: no records"]
    raters = {r["rater"] for r in recs}
    if len(raters) != 1:
        return [f"{src}: mixed raters {sorted(raters)}"]
    rater = recs[0]["rater"]
    if rater not in data["raters"]:
        errs.append(f"{src}: unknown rater {rater!r}")
    rounds = {r["round"] for r in recs}
    if rounds != {data["round"]}:
        errs.append(f"{src}: round {sorted(rounds)} != rows.json round {data['round']}")
    versions = {r["form_version"] for r in recs}
    if versions != {version}:
        errs.append(f"{src}: form_version {sorted(versions)} != rows.json {version}")
        return errs
    expected = build_order([r["id"] for r in data["rows"]], data["anchors"],
                           data["anchor_policy"], version, rater)
    got = sorted(recs, key=lambda r: (r["position"] is None, r["position"] or 0))
    if len(got) != len(expected):
        errs.append(f"{src}: {len(got)} records, expected {len(expected)} cards")
    for i, (g, e) in enumerate(zip(got, expected), 1):
        if g["position"] != i or g["atom"] != e["id"] or g["is_anchor"] != e["is_anchor"]:
            errs.append(f"{src}: position {i}: got ({g['atom']}, is_anchor={g['is_anchor']}, "
                        f"position={g['position']}), expected ({e['id']}, is_anchor={e['is_anchor']})")
            break
    for g in got:
        for q in ("h1", "h2"):
            if g[q] not in (1, 2, 3, 4):
                errs.append(f"{src}: {g['atom']}#{g['is_anchor']}: {q}={g[q]!r} not in 1..4")
        want_flag = 1 if (g["is_anchor"] == 0 and g["atom"] in data["anchors"]) else 0
        if g["seen_as_calibration"] != want_flag:
            errs.append(f"{src}: {g['atom']}#{g['is_anchor']}: seen_as_calibration should be {want_flag}")
    return errs


def merge(exports: list[Path], rows_path: Path) -> tuple[list[dict], str]:
    data = json.loads(rows_path.read_text(encoding="utf-8"))
    version = form_version(data)
    all_recs, errs, seen = [], [], set()
    for p in exports:
        recs = load_export(p)
        e = check_export(recs, data, version, p.name)
        if not e:
            rater = recs[0]["rater"]
            if rater in seen:
                e = [f"{p.name}: rater {rater!r} appears in more than one export"]
            seen.add(rater)
        errs += e
        all_recs += recs
    if errs:
        raise MergeError("\n".join(errs))
    all_recs.sort(key=lambda r: (-r["is_anchor"], r["atom"], r["rater"]))
    return all_recs, report(all_recs, data)


def report(recs: list[dict], data: dict) -> str:
    raters = sorted({r["rater"] for r in recs})
    by_atom: dict[str, dict[str, dict]] = defaultdict(dict)
    for r in recs:
        if r["is_anchor"] == 0:
            by_atom[r["atom"]][r["rater"]] = r
    L = [f"round {data['round']} · raters {raters} · data rows {len(by_atom)} · "
         f"calibration rows {sum(1 for r in recs if r['is_anchor'])}",
         "Raw agreement counts only; no kappa / CVR by design (D-M6, preliminary mode)."]
    for rater in raters:
        rows = [r for r in recs if r["rater"] == rater and r["is_anchor"] == 0]
        L.append(f"  {rater}: H1 yes-direction (3 or 4) {sum(r['h1'] >= 3 for r in rows)}/{len(rows)} · "
                 f"H2 yes-direction {sum(r['h2'] >= 3 for r in rows)}/{len(rows)}")
    multi = {a: rs for a, rs in by_atom.items() if len(rs) >= 2}
    if multi:
        for q in ("h1", "h2"):
            exact = sum(len({r[q] for r in rs.values()}) == 1 for rs in multi.values())
            direction = sum(len({r[q] >= 3 for r in rs.values()}) == 1 for rs in multi.values())
            L.append(f"  {q.upper()}: all raters exact-agree {exact}/{len(multi)} · "
                     f"same direction {direction}/{len(multi)}")
        disagree = sorted(a for a, rs in multi.items()
                          if any(len({r[q] >= 3 for r in rs.values()}) > 1 for q in ("h1", "h2")))
        if disagree:
            L.append("  direction disagreements: " + ", ".join(disagree))
    flagged = sorted({r["atom"] for r in recs if r["seen_as_calibration"] == 1})
    if flagged:
        L.append("  flagged seen_as_calibration (rated minutes after being shown as a labeled example): "
                 + ", ".join(flagged))
    return "\n".join(L)


def write_csv(recs: list[dict], out: Path) -> None:
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLS, lineterminator="\n")
        w.writeheader()
        for r in recs:
            w.writerow({c: ("" if r[c] is None else r[c]) for c in CSV_COLS})


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("exports", nargs="+", type=Path)
    ap.add_argument("--rows", required=True, type=Path, help="the round's rows.json (frozen content)")
    ap.add_argument("--out", required=True, type=Path, help="merged CSV to write (commit it to rosin docs/h-screen/)")
    a = ap.parse_args(argv)
    try:
        recs, rep = merge(a.exports, a.rows)
    except MergeError as e:
        print("REFUSED:\n" + str(e), file=sys.stderr)
        return 1
    write_csv(recs, a.out)
    print(rep)
    print(f"wrote {a.out} ({len(recs)} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
