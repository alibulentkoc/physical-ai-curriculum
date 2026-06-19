---
module: 9
unit: 3
lesson: 9
type: answer_key
title: "Answer Key — From Target Pose to Goal Configuration"
audience: coaches
---

# Answer Key 3.1 — From Target Pose to Goal Configuration

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** IK maps a target pose to joint angles (configuration); FK is the inverse direction.

**Q2 — B.** None means the pose is unreachable — outside the reach annulus.

**Q3 — C.** A reachable interior point has two configurations (elbow up / elbow down).

**Q4 — B.** FK(IK(target)) ≈ target verifies the configuration reaches the pose.

**Q5 — False.** Surface the unreachability (return None); fudging a boundary angle hides the fault (the Lesson 1.1 trap).

---

**Q6 — model answer.** Module 5 owns the IK math; Module 4 owns FK verification. Integration owns the decisions: invoking IK, choosing the elbow branch by a consistent policy, FK-verifying, and deciding what to do on None (route to Recover, never fudge). Math is the layers'; the seam decisions are integration's.
*Grading: require the M5/M4-math vs integration-decision split and the None-handling point.*

**Q7 — model answer.** cos q2 = (0.25 − 0.16 − 0.09)/0.24 = 0, |cos q2| ≤ 1 → reachable. q2 = ±π/2 → two solutions (elbow up/down), each FK-verified; the seam picks one branch by policy and records it.
*Grading: require reachable + two solutions; bonus for the policy/record point.*
