---
module: 7
unit: 8
lesson: 3
type: answer_key
title: "Answer Key — Validate and Hand Off: The Reference Trajectory Layer"
audience: coaches
---

# Answer Key 8.3 — Validate and Hand Off: The Reference Trajectory Layer

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** The handoff is gated on VALIDATE passing.

**Q2 — B.** The layer exposes reference(t) → (q_d, q̇_d, q̈_d, info) + metadata.

**Q3 — B.** It's the bookend to the Module 6 velocity layer (a clean handoff).

**Q4 — C.** No tracking error/gain/torque/motor command — that's Module 8.

**Q5 — B.** A validation failure blocks the handoff (rework).

---

**Q6 — model answer.** A factory doesn't just make a part — it inspects it (does it pass QC?) and then packages it with a label: part number, spec sheet, a 'passed inspection' stamp, and a clear interface for use. The customer gets a sealed, certified package and doesn't need the manufacturing details. The reference trajectory layer is Module 7's certified product: VALIDATE is the inspection (must pass every check), and packaging wraps the validated trajectory with a clean interface (call reference(t)) and a spec sheet (duration, rate, validated, metrics). A trajectory that fails inspection never ships — it goes back for rework.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** It exposes reference(t) → (q_d, q̇_d, q̈_d, info) — the feed-forward triple at any time — plus metadata: duration, control rate, the validated flag, and quality metrics. It's the bookend to Module 6's velocity layer because the modules chain through clean interfaces: Module 6 ended by handing Module 7 a velocity_layer(q, ξ_d) → q̇; Module 7 ends by handing Module 8 a reference(t) → (q_d, q̇_d, q̈_d). Each module's final artifact is the next module's input, which is what lets them compose into a working system.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Module 8 supplies the tracking law: it reads the reference, computes the tracking error against the measured state, applies control gains (and accounts for dynamics), and commands the actuators to follow the reference and reject disturbances. The layer contains none of that — it's the desired motion only, the input to the controller, not a controller. A crisp contract is valuable because it lets Module 8 be built and tested against a fixed, well-specified reference interface, and lets the same validated reference run in simulation and on hardware without change.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Shipping an unvalidated trajectory (the handoff is gated on VALIDATE).
- Putting control logic (error/gain/torque) in the layer — it's the reference, not a controller.
- Omitting metadata; blurring the M6→M7→M8 bookend.
