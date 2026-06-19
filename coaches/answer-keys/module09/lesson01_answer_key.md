---
module: 9
unit: 1
lesson: 1
type: answer_key
title: "Answer Key — Why Integration Is Hard: The Whole vs. The Parts"
audience: coaches
---

# Answer Key 1.1 — Why Integration Is Hard: The Whole vs. The Parts

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Passing per-layer tests proves component correctness only; system correctness is a separate property of the composition.

**Q2 — B.** The baton is information; it is dropped in the exchange zone — the seam between layers.

**Q3 — B.** Selection's postcondition (nearest ripe) doesn't guarantee the planner's reachability precondition — a contract violation.

**Q4 — C.** Controller overshoot is a Module 8 control concept, not one of the four seam failure modes (interface mismatch, contract violation, temporal coupling, shared-state drift).

**Q5 — False.** Module 9 wraps existing layers; it does not rebuild perception or control.

---

**Q6 — model answer.** Component correctness means each layer meets its own specification (its unit tests pass). System correctness is a property of the *composition*: whether each stage's postcondition satisfies the next stage's precondition, with consistent units, frames, timing, and shared state. A system of correct components can still be incorrect because the seams between them are untested by component checks.
*Grading: credit the parts-vs-composition distinction and at least one named seam concern.*

**Q7 — model answer.** Perception reports a ripe tomato at radius 1.99 m; selection forwards it; the planner plans to it; the controller tracks perfectly — but reach is 2.0 m and IK returned a boundary "best effort," so the gripper closes on empty air. Every layer met its spec; no layer owned "is this target reachable before we commit?", which lives in a seam.
*Grading: any example where each layer meets its contract yet the composition fails in an unowned seam earns full credit.*
