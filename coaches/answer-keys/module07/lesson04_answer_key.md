---
module: 7
unit: 1
lesson: 4
type: answer_key
title: "Answer Key — The Motion Pipeline"
audience: coaches
---

# Answer Key 1.4 — The Motion Pipeline

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Plan → parameterize → execute open-loop (M6) → track (M8).

**Q2 — B.** Open-loop execution demonstrates feasibility/smoothness; it does not correct error.

**Q3 — B.** No feedback control, no dynamics.

**Q4 — B.** A validated reference trajectory (q_ref, q̇_ref, q̈_ref) plus conditioning info.

**Q5 — B.** Open-loop has no error signal; control closes the loop.

---

**Q6 — model answer.** It runs the planned trajectory forward through the M6 velocity layer to confirm the motion is executable on this arm — joint rates stay bounded, the arm stays clear and well-conditioned (a feasibility certificate). It deliberately does NOT measure the arm's actual state or correct any deviation; there is no error signal. Closing that loop is Module 8.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** (1) No feedback/closed-loop control — Module 7 produces and may run the reference open-loop but never measures error and corrects it; tracking is Module 8. (2) No dynamics — no forces, torques, masses, or inertia; 'efficiency' is a geometric/temporal proxy (time, path length, jerk, clearance).
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Correcting error requires measuring actual state and computing a feedback term — that is closed-loop control, Module 8's domain. It also pulls in stability concerns and soon dynamics. The clean alternative is for Module 7 to hand Module 8 a validated reference (with derivatives and conditioning info) so Module 8 can do the correcting properly.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Thinking open-loop execution is control — there is no error signal.
- Letting 'efficiency' smuggle in energy/forces — it is a geometric/temporal proxy in M7.
- Handing Module 8 a bare path instead of a time-parameterized reference.
