---
module: 9
unit: 4
lesson: 13
type: answer_key
title: "Answer Key — The Motion Stack"
audience: coaches
---

# Answer Key 4.1 — The Motion Stack: Reference → Velocity → Tracking Controller

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Each tick: sample the reference, measure the plant, compute the command, drive the plant.

**Q2 — B.** reference (M7) → tracking controller (M8) → plant, with M6's velocity layer as the differential primitive.

**Q3 — B.** Friction, load, and inertia make an open-loop command drift; feedback corrects the gap.

**Q4 — B.** Feed-forward anticipates the planned motion so the controller isn't always catching up.

**Q5 — False.** Module 8 is wrapped verbatim; Execute only assembles and runs the loop.

---

**Q6 — model answer.** Sample the reference to get (q_d, q̇_d, q̈_d); measure the plant's (q, q̇); pass both to the tracking controller, which combines feed-forward (from the derivatives) with PID feedback (on q_d − q) to produce a command u; drive the plant one step with u, producing a new (q, q̇). Repeat at the fixed timestep; over the run q → q_d and the gripper reaches the target.
*Grading: require the four sub-steps and the feed-forward + feedback combination.*
