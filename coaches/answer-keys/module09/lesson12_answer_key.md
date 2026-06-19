---
module: 9
unit: 3
lesson: 12
type: answer_key
title: "Answer Key — Unit 3 Recap: Understand → Plan"
audience: coaches
---

# Answer Key 3.4 — Unit 3 Recap: Understand → Plan

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** pose → configuration → reference.

**Q2 — B.** M5 (IK) and M7 (planner) do the math; integration owns the seam decisions.

**Q3 — B.** The seam hands Execute a validated reference(t).

**Q4 — B.** None at IK = unreachable; validated=False at Plan = infeasible trajectory.

**Q5 — True.** Unit 4 executes; judging tracking error vs. tolerance is Unit 5's Track stage.

---

**Q6 — model answer.** Understand commits a target pose (M9). to_configuration converts it to q_goal via Module 5 IK; Module 4 FK verifies FK(q_goal) = target. plan_reference invokes Module 7's wrapped planner for a validated reference(t) = (q_d, qd_d, qdd_d); check validated and that FK(reference(duration)) reaches the target. Math is M5/M7; integration owns the calls, the elbow-branch choice, and handling None (unreachable) or validated=False (infeasible) via Recover.
*Grading: one accurate value+owner+check per step; full credit for the chain plus the ownership split.*
