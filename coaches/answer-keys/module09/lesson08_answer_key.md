---
module: 9
unit: 2
lesson: 8
type: answer_key
title: "Answer Key — Unit 2 Recap: Perceive → Understand"
audience: coaches
---

# Answer Key 2.4 — Unit 2 Recap: Perceive → Understand

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Clean → decide → stay robust → hand forward.

**Q2 — B.** One committed target; 5 detections − 1 merged duplicate = 4 world-state entries; the occluded fruit isn't among them this frame.

**Q3 — B.** A committed target with a pose, plus a ranked fallback list, goes to Plan.

**Q4 — A.** A committed target of None when nothing is pickable is a normal, handled outcome.

**Q5 — True.** Clean must precede decide, or duplicates and noise leak into the selection.

---

**Q6 — model answer.** *Clean:* convert raw detections into a trusted world state by de-duplicating within tolerance, annotating reachability and distance, and normalizing to the world frame. *Decide:* apply the explicit policy — filter to ripe-and-reachable, rank by distance, commit to one — yielding a target with a pose and a ranked fallback list. *Stay robust:* treat detections as evidence not ground truth, so occlusion triggers fall-back, duplicates merge, and noise produces only small bounded changes; then hand the committed target to Plan.
*Grading: one accurate sentence per move; full credit for all three.*
