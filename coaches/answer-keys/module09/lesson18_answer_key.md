---
module: 9
unit: 5
lesson: 18
type: answer_key
title: "Answer Key — System Monitoring: Telemetry and the Info Dictionaries"
audience: coaches
---

# Answer Key 5.2 — System Monitoring: Telemetry and the Info Dictionaries

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Monitoring collects existing per-layer info dictionaries into one dashboard — observation, not new theory.

**Q2 — B.** M6 emits manipulability w, σ_min, condition κ, and a singular flag.

**Q3 — B.** Low w means near a singularity — small tool moves demand large joint rates.

**Q4 — B.** Health and success are distinct; a run can succeed with worrying telemetry (a near-singular pass).

**Q5 — True.** The requested-vs-delivered effort gap is emitted by M8; nonzero saturation means the plan exceeds the actuator.

---

**Q6 — model answer.** The task succeeded (error/tracking excellent), but manipulability 0.004 is alarming — the arm passed very close to a singularity, where the velocity mapping is ill-conditioned. It succeeded barely, through a fragile region; a slightly different target might not. Correct reading: "succeeded, with a near-singular health warning worth investigating." Monitoring surfaces the latent risk the verdict hides.
*Grading: require recognising the manipulability warning despite the success verdict.*
