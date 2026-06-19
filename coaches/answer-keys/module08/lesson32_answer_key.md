---
module: 8
unit: 8
lesson: 8.4
type: answer_key
title: "Answer Key 8.4 — Capstone: The Greenhouse Arm Tracks Its Trajectory"
audience: coaches
---

# Answer Key 8.4 — Capstone: The Greenhouse Arm Tracks Its Trajectory

*Coaches' key. Multiple-choice answers with the correct option; model answers for the short-response items, with grading guidance; and common misconceptions to watch for.*

**Q1 — B.** The planar 2-link greenhouse arm

*Why:* Per-joint control layers track a Module 7 reference on the arm.

**Q2 — B.** ≈ 0.0000 (essentially perfect)

*Why:* The closed loop follows the plan almost exactly.

**Q3 — B.** ≈ 0.012 (near zero — rejected)

*Why:* Feedback drove the error back toward zero.

**Q4 — B.** ≈ 4.9 (large permanent miss)

*Why:* Open-loop feedforward cannot see or correct a disturbance.

**Q5 — B.** The control layer (the Module 9 handoff)

*Why:* tracking_controller(reference, measured_state) → actuator_command for Module 9.

**Q6 — model answer.** Feedforward only knows the plan (the reference's velocity/acceleration); it is open-loop and blind to a disturbance, so a kick pushes the joint off and it stays off. Feedback sees the resulting tracking error and pushes back until the error returns to zero — so only the closed loop rejects the disturbance.

**Q7 — model answer.** Open-loop execution drifts (U1); PID feedback corrects error (U2); stability/tuning make it well-behaved (U3); feedforward + feedback track the whole arm (U4); the actuator imposes real limits (U5); the loop runs as messages with latency (U6); it must execute periodically in real time (U7); and it is assembled as a ROS 2 control stack (U8), packaged as the control layer.

**Q8 — model answer.** It hands Module 9 the verified control layer — tracking_controller(reference, measured_state) → actuator_command. Module 9 integrates it into a full autonomous system: perception-driven planning that supplies references, coordination of subsystems, and task supervision — all built on top of the control layer, which Module 8 deliberately left to Module 9.

*Grading: award full credit for a short answer that captures the key idea in the model answer, even if briefer or differently worded; partial credit if the core mechanism is named but not fully explained.*

### Common misconceptions to watch for

- Crediting feedforward for disturbance recovery; feedforward is open-loop and blind to disturbances.
- Concluding perfect tracking means feedback is unnecessary — the disturbance run shows why the loop must close.
- Doing Module 9's integration work in the capstone — the capstone produces the control layer only.
