# rosin-h-screen

Rating interface for the **H screen** of the rosin atom-mining loop: a
professional violinist (and the author, as a sanity band) rate each measurement
"atom" on two questions, *attended* (do teachers attend to this?) and
*actionable* (could a student act on the value?), on a 4-point scale.

Static site, no server. Ratings are exported as a file and committed to the
rosin repo as the durable record. See `docs/` in rosin for the protocol.

Round 0 = the frozen incumbent atoms. Later rounds reuse the same instrument
with rows generated from `AtomSpec`s.
