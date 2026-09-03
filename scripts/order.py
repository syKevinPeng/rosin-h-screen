"""Python port of template/order.js (bit-for-bit): the per-rater card order.

Used by merge_scores.py to verify that an export's `position` column is the
order the frozen page would have shown that rater, and by the tests to pin
the JS and Python implementations against each other.
"""
from __future__ import annotations

M32 = 0xFFFFFFFF


def fnv1a(s: str) -> int:
    h = 0x811C9DC5
    for ch in s:
        # JS charCodeAt is UTF-16; all inputs here are ASCII, asserted.
        code = ord(ch)
        assert code < 0x10000, "order seed inputs must be BMP/ASCII"
        h ^= code
        h = (h * 0x01000193) & M32
    return h


def _imul(a: int, b: int) -> int:
    """JS Math.imul: 32-bit signed multiply."""
    r = (a * b) & M32
    return r - (1 << 32) if r & 0x80000000 else r


def _to_i32(x: int) -> int:
    x &= M32
    return x - (1 << 32) if x & 0x80000000 else x


def mulberry32(seed: int):
    a = _to_i32(seed)

    def rnd() -> float:
        nonlocal a
        a = _to_i32(a + 0x6D2B79F5)
        t = _imul(a ^ ((a & M32) >> 15), 1 | a)
        t = _to_i32((t + _imul(t ^ ((t & M32) >> 7), 61 | t)) ^ t)
        return ((t ^ ((t & M32) >> 14)) & M32) / 4294967296

    return rnd


def shuffle(items: list, seed: int) -> list:
    a = list(items)
    rnd = mulberry32(seed)
    for i in range(len(a) - 1, 0, -1):
        j = int(rnd() * (i + 1))
        a[i], a[j] = a[j], a[i]
    return a


def build_order(ids: list[str], anchors: list[str], policy: str,
                form_version: str, rater: str) -> list[dict]:
    data_ids = [i for i in ids if policy == "repeat" or i not in anchors]
    seed = fnv1a(f"{form_version}|{rater}")
    out = [{"id": a, "is_anchor": 1} for a in anchors]
    out += [{"id": i, "is_anchor": 0} for i in shuffle(data_ids, seed)]
    return out
