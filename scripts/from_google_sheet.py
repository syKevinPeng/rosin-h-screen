#!/usr/bin/env python3
"""Turn the Google Form's response sheet into per-rater export files.

    python scripts/from_google_sheet.py responses.csv --out exports/

`responses.csv` is the sheet linked to the Google Form, downloaded as CSV
(File > Download > CSV). Each response row holds the whole answer file in the
"Survey Response" column; this script writes it out verbatim as
<out>/<rater>-<form_version>.csv, ready for scripts/merge_scores.py. When a
rater submitted more than once (the Form allows editing), the LAST row wins
and the others are reported.
"""
from __future__ import annotations

import argparse
import csv
import io
import sys
from pathlib import Path

PAYLOAD_COL = "Survey Response"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sheet_csv", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--column", default=PAYLOAD_COL, help="column holding the answer file")
    a = ap.parse_args(argv)
    rows = list(csv.DictReader(a.sheet_csv.read_text(encoding="utf-8-sig").splitlines()))
    if not rows:
        print("no responses", file=sys.stderr)
        return 1
    if a.column not in rows[0]:
        print(f"column {a.column!r} not found; columns: {list(rows[0])}", file=sys.stderr)
        return 1
    a.out.mkdir(parents=True, exist_ok=True)
    latest: dict[str, tuple[int, str]] = {}
    for i, row in enumerate(rows, 1):
        payload = (row.get(a.column) or "").strip()
        if not payload.startswith("round,form_version,rater"):
            print(f"row {i}: not an answer file (skipped)", file=sys.stderr)
            continue
        recs = list(csv.DictReader(io.StringIO(payload)))
        if not recs:
            print(f"row {i}: empty answer file (skipped)", file=sys.stderr)
            continue
        key = f"{recs[0]['rater']}-{recs[0]['form_version']}"
        if key in latest:
            print(f"row {i}: {key} submitted again; keeping the later row", file=sys.stderr)
        latest[key] = (i, payload if payload.endswith("\n") else payload + "\n")
    for key, (i, payload) in latest.items():
        p = a.out / f"{key}.csv"
        p.write_text(payload, encoding="utf-8")
        print(f"wrote {p} (sheet row {i})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
