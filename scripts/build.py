#!/usr/bin/env python3
"""Build one round of the H-screen form from its rows.json.

    python scripts/build.py rounds/round-0 [--current] [--check]

Outputs (deterministic: no timestamps, so a rebuild of frozen content is
byte-identical and `--check` can guard the freeze):

  <round>/index.html        the rating page: rows inlined, form_version stamped
  <round>/form.md           printable form, fixed order (paper fallback)
  <round>/blank-scores.csv  one line per card, answers empty (spreadsheet fallback)
  index.html (repo root)    redirect to this round, only with --current

form_version = first 12 hex of sha256(canonical rows.json). Any content change
changes it; the page, the printable form, the blank sheet and every export
carry it, so nothing can drift from the committed rows.json.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "template" / "page.html"
ORDER_JS = ROOT / "template" / "order.js"
TAGS = {"verbatim", "synthesis", "expert-opinion", "experiment", "uncited"}
ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")
PLACEHOLDER_RE = re.compile(r"__[A-Z][A-Z_]*__")
CSV_COLS = [
    "round", "form_version", "rater", "position", "atom", "is_anchor",
    "seen_as_calibration", "h1", "h2", "note", "shown_at", "answered_at",
    "started_at", "finished_at",
]


# ---------------------------------------------------------------- version --
def canonical(data: dict) -> bytes:
    return json.dumps(data, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":")).encode("utf-8")


def form_version(data: dict) -> str:
    return hashlib.sha256(canonical(data)).hexdigest()[:12]


# --------------------------------------------------------------- validate --
CJK_RE = re.compile(r"[\u3000-\u303f\u3400-\u4dbf\u4e00-\u9fff\uff00-\uffef]")


def _s(x, path: str, errs: list[str]) -> None:
    if not (isinstance(x, str) and x.strip()):
        errs.append(f"{path}: non-empty string required")
    elif CJK_RE.search(x):
        errs.append(f"{path}: contains CJK text; the instrument is English-only (Siyuan, 2026-09-03)")


def _s_tree(x, path: str, errs: list[str]) -> None:
    if isinstance(x, dict):
        for k, v in x.items():
            _s_tree(v, f"{path}.{k}", errs)
    else:
        _s(x, path, errs)


def validate(data: dict) -> list[str]:
    """Return a list of problems (empty = valid)."""
    errs: list[str] = []
    if not isinstance(data.get("round"), int):
        errs.append("round: int required")
    for k in ("title", "round_label", "intro"):
        _s(data.get(k), k, errs)
    q = data.get("questions") or {}
    for k in ("h1", "h2", "h2_gloss"):
        _s(q.get(k), f"questions.{k}", errs)
    if isinstance(q.get("h1"), str) and "{x}" not in q["h1"]:
        errs.append("questions.h1: must contain {x} (the card's subject)")
    if isinstance(data.get("intro"), str) and "{n}" not in data["intro"]:
        errs.append("intro: must contain {n} (the card count)")
    sc = data.get("scale")
    if not (isinstance(sc, list) and [o.get("value") for o in sc] == [1, 2, 3, 4]):
        errs.append("scale: exactly the values 1,2,3,4 in order")
    else:
        for o in sc:
            _s(o.get("label"), f"scale[{o.get('value')}].label", errs)
    ui = data.get("ui")
    if not isinstance(ui, dict):
        errs.append("ui: object required")
    else:
        _s_tree(ui, "ui", errs)
        for k in ("tag_labels", "rater_names"):
            if k not in ui:
                errs.append(f"ui.{k}: missing")
        for tag in TAGS:
            if tag not in (ui.get("tag_labels") or {}):
                errs.append(f"ui.tag_labels.{tag}: missing")
    rows = data.get("rows")
    if not (isinstance(rows, list) and rows):
        errs.append("rows: non-empty list required")
        return errs
    ids = [r.get("id") for r in rows]
    for i, r in enumerate(rows):
        p = f"rows[{i}]({r.get('id')})"
        if not (isinstance(r.get("id"), str) and ID_RE.match(r["id"])):
            errs.append(f"{p}: bad id (snake_case required)")
        for k in ("group", "status"):
            if not (isinstance(r.get(k), str) and r[k]):
                errs.append(f"{p}.{k}: non-empty string required")
        for k in ("name", "definition", "unit", "range", "prose", "short"):
            _s(r.get(k), f"{p}.{k}", errs)
        fig = r.get("figure")
        if fig is not None and not (isinstance(fig, dict) and fig.get("kind") == "wrist" and fig.get("dir") in (1, 2, 3)):
            errs.append(f"{p}.figure: only {{kind: wrist, dir: 1|2|3}} is supported")
        ph = r.get("phrases")
        if not (isinstance(ph, list) and ph):
            errs.append(f"{p}.phrases: non-empty list required")
            continue
        for j, x in enumerate(ph):
            pp = f"{p}.phrases[{j}]"
            _s(x.get("text"), f"{pp}.text", errs)
            if x.get("source"):
                _s(x.get("source"), f"{pp}.source", errs)
            if x.get("tag") not in TAGS:
                errs.append(f"{pp}.tag: must be one of {sorted(TAGS)}")
            src = x.get("source", "")
            if x.get("tag") == "uncited" and src:
                errs.append(f"{pp}: an uncited phrase must have an empty source")
            if x.get("tag") in TAGS - {"uncited"} and not src:
                errs.append(f"{pp}: a cited phrase needs its attribution in source")
            if not isinstance(x.get("locator", ""), str):
                errs.append(f"{pp}.locator: string required")
            _s(x.get("short_source"), f"{pp}.short_source", errs)
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        errs.append(f"duplicate row ids: {dup}")
    anchors = data.get("anchors")
    if not (isinstance(anchors, list) and anchors and len(set(anchors)) == len(anchors)):
        errs.append("anchors: non-empty list of unique ids required")
    else:
        for a in anchors:
            if a not in ids:
                errs.append(f"anchor {a!r} is not a row")
    if data.get("anchor_policy") not in ("repeat", "once"):
        errs.append("anchor_policy: 'repeat' or 'once'")
    col = data.get("collect")
    if col is not None:
        if col.get("kind") != "google_form":
            errs.append("collect.kind: only 'google_form' is supported")
        if not (isinstance(col.get("viewform"), str) and col["viewform"].startswith("https://docs.google.com/forms/")):
            errs.append("collect.viewform: a docs.google.com/forms URL is required")
        if not re.fullmatch(r"entry\.\d+", col.get("entry", "")):
            errs.append("collect.entry: must look like entry.123456")
    raters = data.get("raters")
    if not (isinstance(raters, list) and raters
            and all(isinstance(r, str) and ID_RE.match(r) for r in raters)
            and len(set(raters)) == len(raters)):
        errs.append("raters: non-empty list of unique snake_case ids required")
    elif isinstance(ui, dict):
        for r in raters:
            if r not in (ui.get("rater_names") or {}):
                errs.append(f"ui.rater_names.{r}: missing")
    return errs


# ------------------------------------------------------------------ cards --
def cards(data: dict) -> list[dict]:
    """Fixed (unshuffled) card list: anchors first, then rows in code order.

    Under anchor_policy "repeat" the anchor atoms appear again in the data
    block with seen_as_calibration=1. This is the paper/spreadsheet order;
    the page shuffles the data block per rater (template/order.js).
    """
    anchors = data["anchors"]
    out = [{"atom": a, "is_anchor": 1, "seen_as_calibration": 0} for a in anchors]
    for r in data["rows"]:
        if data["anchor_policy"] == "once" and r["id"] in anchors:
            continue
        out.append({"atom": r["id"], "is_anchor": 0,
                    "seen_as_calibration": 1 if r["id"] in anchors else 0})
    return out


# ---------------------------------------------------------------- renders --
def render_html(data: dict, version: str) -> str:
    tpl = TEMPLATE.read_text(encoding="utf-8")
    js = ORDER_JS.read_text(encoding="utf-8")
    inlined = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    out = (tpl.replace("__ROWS_JSON__", inlined)
              .replace("__ORDER_JS__", js)
              .replace("__FORM_VERSION__", version)
              .replace("__TITLE__", data["title"].replace("&", "&amp;").replace("<", "&lt;"))
              .replace("__ROUND__", str(data["round"])))
    left = PLACEHOLDER_RE.findall(out)
    if left:
        raise RuntimeError(f"unfilled template placeholders: {sorted(set(left))}")
    return out


def _bl(o: str) -> str:
    return o


def _fill(s: str, **vars) -> str:
    return re.sub(r"\{(\w+)\}", lambda m: str(vars.get(m.group(1), m.group(0))), s)


def render_form_md(data: dict, version: str) -> str:
    ui, q = data["ui"], data["questions"]
    rows = {r["id"]: r for r in data["rows"]}
    cs = cards(data)
    n = len(cs)
    boxes = " · ".join(f"☐ {o['value']} {o['label']}" for o in data["scale"])
    L = [f"# {_bl(data['title'])} · {_bl(data['round_label'])}", "",
         f"**{_bl(ui['version'])}:** `{version}` · **{_bl(ui['rater'])}:** "
         + " · ".join(f"☐ {_bl(ui['rater_names'][r])}" for r in data["raters"]), "",
         _bl(ui["print_title"]), "",
         _fill(data["intro"], n=n), "",
         f"## {_bl(ui['questions_heading'])}", "",
         f"**{_bl(ui['q1_label'])}.** {_fill(q['h1'], x='this')}", "", f"**{_bl(ui['q2_label'])}.** {_fill(q['h2'], x='this')}  ", f"*{_bl(q['h2_gloss'])}*", "",
         f"## {_bl(ui['scale_heading'])}", ""]
    L += [f"- **{o['value']}** {o['label']}" for o in data["scale"]]
    L += ["", "---", ""]
    for i, c in enumerate(cs, 1):
        r = rows[c["atom"]]
        L.append(f"### {i}. {_bl(r['name'])}")
        L.append(f"<sub>{r['id']}</sub>" + (f"  \n**{_bl(ui['calibration'])}**" if c["is_anchor"] else ""))
        L.append("")
        L.append(r["prose"])
        L.append("")
        L.append(f"**{_bl(ui['q1_label'])}.** {_fill(q['h1'], x=r['short'])}  \n{boxes}")
        L.append("")
        L.append(f"**{_bl(ui['q2_label'])}.** {_fill(q['h2'], x=r['short'])}  \n{boxes}")
        L.append("")
        L.append(f"**{_bl(ui['note_prompt'])}**  \n" + "\\_" * 40)
        L.append("")
    return "\n".join(L) + "\n"


def render_blank_csv(data: dict, version: str) -> str:
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=CSV_COLS, lineterminator="\n")
    w.writeheader()
    for pos, c in enumerate(cards(data), 1):
        w.writerow({"round": data["round"], "form_version": version, "rater": "",
                    "position": pos, "atom": c["atom"], "is_anchor": c["is_anchor"],
                    "seen_as_calibration": c["seen_as_calibration"]})
    return buf.getvalue()


def render_redirect(rel: str) -> str:
    return ("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"robots\" content=\"noindex\"><title>Survey</title>"
            f"<noscript><meta http-equiv=\"refresh\" content=\"0; url={rel}\"></noscript>"
            f"<script>location.replace({json.dumps(rel)} + location.search + location.hash);</script>"
            f"</head><body><p>Redirecting to <a href=\"{rel}\">{rel}</a>…</p></body></html>\n")


# ------------------------------------------------------------------- main --
def _rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def build_outputs(round_dir: Path, current: bool) -> tuple[str, dict[Path, str]]:
    data = json.loads((round_dir / "rows.json").read_text(encoding="utf-8"))
    errs = validate(data)
    if errs:
        raise SystemExit("rows.json is invalid:\n  " + "\n  ".join(errs))
    version = form_version(data)
    outputs = {
        round_dir / "index.html": render_html(data, version),
        round_dir / "form.md": render_form_md(data, version),
        round_dir / "blank-scores.csv": render_blank_csv(data, version),
    }
    if current:
        rel = round_dir.resolve().relative_to(ROOT).as_posix() + "/"
        outputs[ROOT / "index.html"] = render_redirect(rel)
    return version, outputs


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("round_dir", help="e.g. rounds/round-0 (must contain rows.json)")
    ap.add_argument("--current", action="store_true", help="also write the repo-root index.html redirect to this round")
    ap.add_argument("--check", action="store_true", help="do not write; exit 1 if any output is stale")
    a = ap.parse_args(argv)
    rd = Path(a.round_dir).resolve()
    version, outputs = build_outputs(rd, a.current)
    stale = []
    for path, text in outputs.items():
        if a.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(path)
        else:
            path.write_text(text, encoding="utf-8")
    if a.check:
        if stale:
            print("STALE (rebuild and commit):", *[_rel(p) for p in stale], sep="\n  ")
            return 1
        print(f"up to date · form_version {version}")
        return 0
    print(f"built round {rd.name} · form_version {version} · {len(outputs)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
