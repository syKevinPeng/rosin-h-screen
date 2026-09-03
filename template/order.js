// Deterministic per-rater card order. Shared verbatim between the page
// (inlined by scripts/build.py) and the Node test, and ported line-for-line
// to scripts/order.py so the committed CSV can be checked against it.
//
// order = anchors (fixed order, is_anchor=1) + shuffle(data rows, seed)
// seed  = fnv1a(form_version + "|" + rater)   -> 32-bit
// shuffle = Fisher-Yates driven by mulberry32(seed)
// anchor_policy "repeat": anchor atoms appear AGAIN inside the shuffled data
// block (is_anchor=0, seen_as_calibration=1); "once": they do not.
(function (root) {
  function fnv1a(str) {
    var h = 0x811c9dc5;
    for (var i = 0; i < str.length; i++) {
      h ^= str.charCodeAt(i);
      h = Math.imul(h, 0x01000193) >>> 0;
    }
    return h >>> 0;
  }
  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function shuffle(arr, seed) {
    var a = arr.slice(), rnd = mulberry32(seed);
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(rnd() * (i + 1));
      var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
    }
    return a;
  }
  function buildOrder(ids, anchors, policy, formVersion, rater) {
    var dataIds = ids.filter(function (id) {
      return policy === "repeat" || anchors.indexOf(id) < 0;
    });
    var seed = fnv1a(formVersion + "|" + rater);
    var out = anchors.map(function (id) { return { id: id, is_anchor: 1 }; });
    shuffle(dataIds, seed).forEach(function (id) {
      out.push({ id: id, is_anchor: 0 });
    });
    return out;
  }
  var api = { fnv1a: fnv1a, mulberry32: mulberry32, shuffle: shuffle, buildOrder: buildOrder };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.HOrder = api;
})(typeof window !== "undefined" ? window : this);
