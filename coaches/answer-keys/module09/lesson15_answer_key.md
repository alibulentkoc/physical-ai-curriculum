---
module: 9
unit: 4
lesson: 15
type: answer_key
title: "Answer Key — A Goal Pose's Journey to Joint Motion"
audience: coaches
---

# Answer Key 4.3 — System Walkthrough: A Goal Pose's Journey to Joint Motion

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** pose → configuration → reference → executed motion → arrival.

**Q2 — B.** FK of the executed final state landing on the target pose.

**Q3 — B.** A good plan with large execution error localises to Execute (or its conditions), not IK/planning.

**Q4 — B.** The actual executed final configuration (not the planned q_goal, not home) is the next q_start.

**Q5 — True.** Execute produces motion; Track (Unit 5) judges whether the error is acceptable.

---

**Q6 — model answer.** Understand commits a target pose (M9). IK converts it to q_goal (M5), FK verifies FK(q_goal) = target (M4). The planner produces a validated reference(t) from q_start to q_goal (M7). The motion stack executes it, tracking to small RMS error (M8), producing the actual q(t). FK of the final q lands on the target pose — arrival. Each stage carries a value, an owner, and a check; a break localises the fault to a stage.
*Grading: one accurate value+owner+check per stage; full credit for the chain ending in FK arrival.*
