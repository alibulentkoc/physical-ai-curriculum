---
module: 9
unit: 3
lesson: 11
type: answer_key
title: "Answer Key — Integration Exercise: Pose to Plan, Wired End to End"
audience: coaches
---

# Answer Key 3.3 — Integration Exercise: Pose to Plan, Wired End to End

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** perceive → understand → to_configuration → plan_reference.

**Q2 — B.** Link 3: a validated reference whose endpoint's FK reaches the target.

**Q3 — B.** None at IK localises the fault to reachability (target outside the workspace).

**Q4 — B.** The second plan's q_start is the first plan's q_goal (where the arm ended up), not home.

**Q5 — True.** validated=False with a good, FK-verified goal is a Plan (trajectory) problem.

---

**Q6 — model answer.** The fault is in Plan: links 1–2 passed (target reachable, q_goal FK-verified), so a failed validation is about the trajectory between start and goal — a limit violation at the requested timing or no collision-free path. The fix is a Plan/Recover decision: relax timing, replan, or re-select. The trace localises it without opening the planner.
*Grading: require "Plan, not IK/perception" and a trajectory-feasibility reason.*
