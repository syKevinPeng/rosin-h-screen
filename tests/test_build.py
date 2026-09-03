import copy
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build  # noqa: E402

ROUND0 = ROOT / "rounds" / "round-0"


def load():
    return json.loads((ROUND0 / "rows.json").read_text(encoding="utf-8"))


def test_round0_validates():
    assert build.validate(load()) == []


def test_version_is_a_stable_content_hash():
    v1, v2 = build.form_version(load()), build.form_version(load())
    assert v1 == v2 and re.fullmatch(r"[0-9a-f]{12}", v1)


def test_version_changes_when_any_content_changes():
    d = load()
    base = build.form_version(d)
    d["rows"][3]["definition"] += "."
    assert build.form_version(d) != base


@pytest.mark.parametrize("mutate, needle", [
    (lambda d: d["rows"][0].update(definition=""), "non-empty string required"),
    (lambda d: d["rows"][0].update(definition="弓速"), "contains CJK text"),
    (lambda d: d["ui"].update(start="开始"), "contains CJK text"),
    (lambda d: d["rows"][0]["phrases"][0].update(tag="made-up"), "tag: must be one of"),
    (lambda d: d["rows"][1]["phrases"][0].update(tag="uncited", source="X"), "uncited phrase must have an empty source"),
    (lambda d: d["rows"][1]["phrases"][0].update(tag="synthesis", source=""), "cited phrase needs its attribution"),
    (lambda d: d["anchors"].append("no_such_atom"), "is not a row"),
    (lambda d: d["rows"].append(copy.deepcopy(d["rows"][0])), "duplicate row ids"),
    (lambda d: d.update(anchor_policy="sometimes"), "anchor_policy"),
    (lambda d: d["scale"].pop(), "scale: exactly"),
    (lambda d: d["ui"]["tag_labels"].pop("uncited"), "ui.tag_labels.uncited"),
    (lambda d: d["raters"].append("guest"), "ui.rater_names.guest"),
])
def test_validate_catches(mutate, needle):
    d = load()
    mutate(d)
    errs = build.validate(d)
    assert any(needle in e for e in errs), errs


def test_html_inlines_every_row_and_fills_every_placeholder():
    d = load()
    v = build.form_version(d)
    html = build.render_html(d, v)
    for r in d["rows"]:
        assert f'"id":"{r["id"]}"' in html
    assert not build.PLACEHOLDER_RE.search(html)
    assert html.count(v) >= 1          # the JS constant; the page renders it into the footer
    assert "HOrder" in html and "buildOrder" in html


def test_html_json_block_round_trips():
    d = load()
    html = build.render_html(d, build.form_version(d))
    m = re.search(r'<script id="rows-json" type="application/json">(.*?)</script>', html, re.S)
    assert m
    assert json.loads(m.group(1).replace("<\\/", "</")) == d


def test_cards_anchors_first_then_code_order_with_repeat_flag():
    d = load()
    cs = build.cards(d)
    assert [c["atom"] for c in cs[:len(d["anchors"])]] == d["anchors"]
    assert all(c["is_anchor"] == 1 for c in cs[:len(d["anchors"])])
    rest = cs[len(d["anchors"]):]
    assert [c["atom"] for c in rest] == [r["id"] for r in d["rows"]]
    assert {c["atom"] for c in rest if c["seen_as_calibration"]} == set(d["anchors"])
    d["anchor_policy"] = "once"
    rest = build.cards(d)[len(d["anchors"]):]
    assert not any(c["atom"] in d["anchors"] for c in rest)


def test_form_md_has_every_card_and_marks_calibration():
    d = load()
    md = build.render_form_md(d, build.form_version(d))
    heads = re.findall(r"^### (\d+)\. ", md, re.M)
    assert [int(h) for h in heads] == list(range(1, len(build.cards(d)) + 1))
    for r in d["rows"]:
        assert f"`{r['id']}`" in md
    cal = d["ui"]["calibration"]
    assert md.count(cal) == len(d["anchors"]) + 0  # calibration cards only
    assert build.form_version(d) in md


def test_blank_csv_shape():
    d = load()
    v = build.form_version(d)
    lines = build.render_blank_csv(d, v).splitlines()
    assert lines[0] == ",".join(build.CSV_COLS)
    assert len(lines) - 1 == len(build.cards(d))
    assert all(v in ln for ln in lines[1:])


def test_rows_are_english_only():
    """Siyuan, 2026-09-03: no Chinese text on the instrument; translated English instead."""
    text = json.dumps(load(), ensure_ascii=False)
    assert not build.CJK_RE.search(text)


def test_public_rows_carry_no_withheld_caveats():
    text = json.dumps(load(), ensure_ascii=False)
    for banned in ("P07", "noise floor", "confound", "SUSTAINED", "defect"):
        assert banned not in text, banned


def test_cli_build_is_deterministic_and_check_guards(tmp_path):
    rd = tmp_path / "round-x"
    rd.mkdir()
    shutil.copy(ROUND0 / "rows.json", rd / "rows.json")
    py = sys.executable
    script = str(ROOT / "scripts" / "build.py")
    subprocess.run([py, script, str(rd)], check=True, capture_output=True)
    first = {p.name: p.read_bytes() for p in rd.iterdir()}
    subprocess.run([py, script, str(rd)], check=True, capture_output=True)
    second = {p.name: p.read_bytes() for p in rd.iterdir()}
    assert first == second
    assert {"rows.json", "index.html", "form.md", "blank-scores.csv"} <= set(first)
    assert subprocess.run([py, script, str(rd), "--check"], capture_output=True).returncode == 0
    (rd / "form.md").write_text("tampered", encoding="utf-8")
    r = subprocess.run([py, script, str(rd), "--check"], capture_output=True, text=True)
    assert r.returncode == 1 and "STALE" in r.stdout


def test_committed_round0_outputs_are_current():
    """The freeze guard: what is committed must be what rows.json builds."""
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build.py"), str(ROUND0), "--current", "--check"],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
