import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build  # noqa: E402
import order  # noqa: E402

D = json.loads((ROOT / "rounds" / "round-0" / "rows.json").read_text(encoding="utf-8"))
V = build.form_version(D)
IDS = [r["id"] for r in D["rows"]]


def js_order(ids, anchors, policy, version, rater):
    js = ("const o=require(%s);process.stdout.write(JSON.stringify(o.buildOrder(%s,%s,%s,%s,%s)));"
          % (json.dumps(str(ROOT / "template" / "order.js")), json.dumps(ids), json.dumps(anchors),
             json.dumps(policy), json.dumps(version), json.dumps(rater)))
    out = subprocess.run(["node", "-e", js], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def test_fnv1a_reference_values():
    assert order.fnv1a("") == 0x811C9DC5
    assert order.fnv1a("a") == 0xE40C292C
    assert order.fnv1a("foobar") == 0xBF9CF968


def test_anchors_first_then_a_permutation_of_all_rows():
    for rater in D["raters"]:
        o = order.build_order(IDS, D["anchors"], "repeat", V, rater)
        assert [x["id"] for x in o[:2]] == D["anchors"]
        assert all(x["is_anchor"] == 1 for x in o[:2])
        data = [x["id"] for x in o[2:]]
        assert sorted(data) == sorted(IDS) and all(x["is_anchor"] == 0 for x in o[2:])
    o = order.build_order(IDS, D["anchors"], "once", V, "author")
    assert not any(x["id"] in D["anchors"] for x in o[2:])


def test_raters_and_versions_get_different_orders_but_each_is_stable():
    a = order.build_order(IDS, D["anchors"], "repeat", V, "violinist")
    b = order.build_order(IDS, D["anchors"], "repeat", V, "author")
    c = order.build_order(IDS, D["anchors"], "repeat", V, "violinist")
    d = order.build_order(IDS, D["anchors"], "repeat", "000000000000", "violinist")
    assert a == c
    assert a != b and a != d


@pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")
@pytest.mark.parametrize("rater", ["violinist", "author", "third_rater"])
@pytest.mark.parametrize("policy", ["repeat", "once"])
def test_js_and_python_orders_are_identical(rater, policy):
    assert js_order(IDS, D["anchors"], policy, V, rater) == order.build_order(IDS, D["anchors"], policy, V, rater)


@pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")
def test_mulberry32_streams_agree_with_js():
    js = "const o=require(%s);const r=o.mulberry32(%d);process.stdout.write(JSON.stringify([r(),r(),r(),r(),r()]));"
    for seed in (1, 0x811C9DC5, 2**31 - 1, 2**32 - 1):
        out = json.loads(subprocess.run(["node", "-e", js % (json.dumps(str(ROOT / "template" / "order.js")), seed)],
                                        capture_output=True, text=True, check=True).stdout)
        rnd = order.mulberry32(seed)
        assert out == [rnd() for _ in range(5)]
