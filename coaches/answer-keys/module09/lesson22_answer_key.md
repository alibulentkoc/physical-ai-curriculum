---
module: 9
unit: 6
lesson: 22
type: answer_key
title: "Answer Key — Detecting Failure: Health Signals and Guards"
audience: coaches
---

# Answer Key 6.2 — Detecting Failure: Health Signals and Guards

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** A guard is a predicate on an existing output that fires the matching event.

**Q2 — B.** Hard-failure guards halt the path at their stage and record the stage reached.

**Q3 — B.** Warning guards annotate a completed run without halting.

**Q4 — B.** run_pipeline is the per-seam guards run in sequence — no new theory.

**Q5 — True.** A guard detects and localises; it does not diagnose root physics.

---

**Q6 — model answer.** Occlude all → Understand guard fires NO_TARGET, halts at Understand (nothing to convert/plan/execute). Out-of-reach bypassing the filter → IK-seam guard fires UNREACHABLE, halts at the IK seam. Obstacle over goal → Understand/IK pass, Plan guard fires PLAN_INVALID, halts at Plan. Strong disturbance → hard guards pass, run executes, Track guard fires TRACKING_FAILURE (+ EXCESS_EFFORT warning). Each halts at the first seam whose guard it trips.
*Grading: require correct stage for each of the four, and the "first tripped seam" principle.*
