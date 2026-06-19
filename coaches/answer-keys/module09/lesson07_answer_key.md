---
module: 9
unit: 2
lesson: 7
type: answer_key
title: "Answer Key — When Perception Lies"
audience: coaches
---

# Answer Key 2.3 — Case Study: When Perception Lies

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Occlusion, noise, and duplicates are facts of operation; the seam's job is robustness, not a perception fix.

**Q2 — B.** Reflect current observability and fall back; cross-frame persistence is a Recover-stage concern.

**Q3 — B.** Dedupe merges the duplicate, so the world-state count is unchanged.

**Q4 — B.** Noise can swap the order of near-equidistant fruit harmlessly; it doesn't flip feasibility except at the reach boundary.

**Q5 — True.** Deterministic-per-frame selection has bounded sensitivity to small perturbations, except at exact feasibility boundaries.

---

**Q6 — model answer.** Dedupe merges the two F1 reports (0.03 m < τ) into one. World state = {F1, F4}, both ripe and reachable. Rank by distance from origin: F4 (≈ 0.92) nearer than F1 (≈ 1.0). Commit F4. The occluded F2 is absent this frame and the F1 duplicate never double-counts — all three faults absorbed, one clean target.
*Grading: require the merge, the occluded-fruit absence, and F4 committed by distance.*
