---
module: 8
unit: 8
lesson: 8.3
type: answer_key
title: "Answer Key 8.3 — The Control Layer: the Module 9 Handoff"
audience: coaches
---

# Answer Key 8.3 — The Control Layer: the Module 9 Handoff

*Coaches' key. Multiple-choice answers with the correct option; model answers for the short-response items, with grading guidance; and common misconceptions to watch for.*

**Q1 — B.** tracking_controller(reference, measured_state) → actuator_command

*Why:* Plan-plus-state in, actuator command out.

**Q2 — C.** The control layer (M8)

*Why:* M8 hands the control layer to M9.

**Q3 — B.** Feedforward + feedback + actuator

*Why:* All of Module 8's control machinery.

**Q4 — C.** Planning, coordination, and supervision

*Why:* Integration beyond the control layer is Module 9's job.

**Q5 — B.** An actuator command decomposable into feedforward, feedback, and delivered parts

*Why:* It tracks closed-loop and exposes the command's breakdown.

**Q6 — model answer.** tracking_controller(reference, measured_state) → actuator_command. It is the M8 link: velocity layer (M6) → reference layer (M7) → control layer (M8) → integrated system (M9). It consumes M7's reference and the measured state and outputs the actuator command M9 will integrate.

**Q7 — model answer.** Inside: feedforward (anticipate, from M7's velocity/acceleration), PID feedback (correct the error), and the actuator pipeline (deliver within limits) — all of Module 8. Outside (Module 9): deciding/planning the references against the world, coordinating subsystems, and supervising the task — no integration beyond the control layer.

**Q8 — model answer.** It lets Module 9 build an integrated autonomous system on top of a stable contract without re-deriving control or reaching into internals. The control layer can be tested, swapped, or reused across robots because what it consumes and produces is fixed, which keeps both modules' scope clean.

*Grading: award full credit for a short answer that captures the key idea in the model answer, even if briefer or differently worded; partial credit if the core mechanism is named but not fully explained.*

### Common misconceptions to watch for

- Letting the control layer decide the reference; the reference comes from Module 7 and is consumed here.
- Doing integration (planning, coordination, supervision) inside the layer — that is Module 9's job.
- Exposing internals instead of a fixed interface — the value is the stable tracking_controller contract.
