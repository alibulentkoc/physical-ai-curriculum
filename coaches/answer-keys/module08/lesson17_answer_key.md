---
module: 8
unit: 5
lesson: 1
type: answer_key
title: "Answer Key — The Actuator: From Requested Command to Delivered Effort"
audience: coaches
---

# Answer Key 5.1 — The Actuator: From Requested Command to Delivered Effort

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** a converter from a requested command to a delivered effort

**Q2 — B.** small requests to deliver no motion until a threshold is crossed

**Q3 — B.** requests above u_max to be capped at the ceiling; the surplus is discarded

**Q4 — A.** the delivered effort cannot change faster than r_max per second (it ramps)

**Q5 — B.** the delivered-effort view is what shapes the command and motion; motor internals are out of scope here

---

**Q6 — model answer.** The controller outputs a requested command, but an actuator sits between it and the joint and re-shapes that request before it becomes physical effort. Three plant-level nonlinearities do the re-shaping: saturation caps the delivered effort at a ceiling ±u_max (surplus is discarded), a deadband delivers nothing for requests too small to register, and a rate limit prevents the delivered effort from changing faster than r_max per second so it ramps rather than jumps. Only after these does the request become the delivered effort that drives the plant, so requested ≠ delivered in general.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Plot requested command on the horizontal axis and delivered effort on the vertical. The curve is flat at zero across the central deadband (|request| ≤ d delivers nothing), rises with unit slope in the middle region (delivered ≈ request, shifted past the deadband), and flattens at ±u_max beyond the saturation ceiling. On top of this static curve, a rate limit means a sudden change in the request is delivered as a ramp, not a step.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Ideal actuator: 5 — it passes the request through. Deadband of 8: 0 — since |5| ≤ 8 the request is inside the dead zone and nothing is delivered. Ceiling of 3: 3 — the request exceeds u_max so it is capped at the ceiling and the surplus is discarded. Same request, three different deliveries — the actuator, not the controller, decides what reaches the joint.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Tuning against an ideal actuator — the loop you analysed isn't the loop that runs.
- Confusing the requested command with the delivered effort.
- Treating the deadband as negligible — it is exactly what blocks the final tiny move.
