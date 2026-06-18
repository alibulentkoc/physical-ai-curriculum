---
module: 8
unit: 2
lesson: 4
type: answer_key
title: "Answer Key — The PID Controller: The Complete Single-Joint Tracker"
audience: coaches
---

# Answer Key 2.4 — The PID Controller: The Complete Single-Joint Tracker

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** u = Kp·e + Ki·∫e + Kd·ė.

**Q2 — B.** P pushes, I erases offset, D damps.

**Q3 — B.** Tuning balances the three terms (not maximizing any).

**Q4 — B.** I removes the offset, then D damps the overshoot.

**Q5 — B.** Feedforward (q̇_d, q̈_d) leads; feedback corrects the residual.

---

**Q6 — model answer.** The law is u = Kp·e + Ki·∫e + Kd·ė, where e = q_d − q. The proportional term Kp·e pushes in proportion to the current error — the main corrective effort, but it leaves a steady-state offset under load. The integral term Ki·∫e accumulates past error and supplies the standing command that erases that offset, since its only equilibrium is e = 0. The derivative term Kd·ė responds to how fast the error is changing and acts as a brake, damping overshoot and allowing higher P/I gains. Summed, they give a fast, accurate, well-damped single-joint tracker.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** P alone moves the joint toward the target but settles short by an offset ≈ load/Kp. Adding I gives PI: the integrator accumulates the persistent error and drives it to zero, erasing the offset — but integral lag makes the response overshoot and ring. Adding D gives PID: the derivative term brakes the fast approach, damping that overshoot into a clean, quick settle. So the progression is: P establishes the correction, I removes the steady-state offset, D damps the resulting overshoot — each term fixing the deficiency the previous one left, yielding accurate and well-behaved tracking.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Module 7 supplies not just q_d but the feedforward derivatives q̇_d and q̈_d. The tracker uses these to compute, in advance, most of the command needed to follow the planned motion — leading the reference rather than waiting for an error to build. The PID feedback term then only has to correct the small residual error from disturbances and model mismatch, instead of generating the entire command reactively. The result is much smaller tracking error, especially during fast motion, because the controller isn't perpetually chasing the reference from behind — feedforward does the bulk of the work and feedback cleans up what's left. This feedforward-plus-feedback combination is the central continuity theme from Module 7 into Module 8.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Maximizing all gains instead of balancing them.
- Expecting D to remove offset or I to damp overshoot (swapped roles).
- Ignoring Module 7's feedforward and tracking with feedback alone (larger error).
