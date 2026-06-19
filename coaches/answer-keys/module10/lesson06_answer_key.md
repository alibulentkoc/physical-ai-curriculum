---
module: 10
unit: 2
lesson: 6
type: answer_key
title: "Answer Key — Synchronizing Twin ↔ Real"
audience: coaches
---

# Answer Key 2.2 — Synchronizing Twin ↔ Real

**Q1 — B.** Copies the reported state into the twin, driving the gap to zero.
**Q2 — B.** Drifts as the real robot acts (divergence grows).
**Q3 — B.** ~0 (synced).
**Q4 — B.** A design choice trading freshness against cost.
**Q5 — True.** Sync is the heartbeat that makes a static replica a live twin.

**Q6 — model answer.** Right after the first sync, the gap is zero. The robot then moves (new q, a newly picked fruit) while the twin holds the old frame, so divergence shows a nonzero joint gap, a nonzero tool gap, and one fruit mismatch — the twin drifted because it didn't refresh. Syncing against the new report rewrites the twin to match, returning the gap to zero. Divergence grows whenever the system advances past the last sync; sync resets it.
*Grading: require drift (nonzero gap/mismatch) + sync resets to zero.*
