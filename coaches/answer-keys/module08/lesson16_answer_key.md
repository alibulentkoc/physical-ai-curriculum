---
module: 8
unit: 4
lesson: 4
type: answer_key
title: "Answer Key — Disturbances, Load, and the Complete Tracker"
audience: coaches
---

# Answer Key 4.4 — Disturbances, Load, and the Complete Tracker

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Disturbance enters the plant, not the reference — feedforward never sees it.

**Q2 — B.** Feedback acts on the measured error the disturbance creates.

**Q3 — C.** Complete tracker = feedforward (known) + feedback (unknown).

**Q4 — C.** Disturbances enter at the plant.

**Q5 — B.** Interface: tracking_controller(reference, measured_state) → actuator_command.

---

**Q6 — model answer.** Feedforward is computed from the reference and the model only: u_ff = m·q̈_d + b·q̇_d + ℓ_nominal. A disturbance — an unmodelled load, a bump, changed friction — enters the plant, not the reference, so it never appears in anything feedforward uses. Feedforward therefore issues exactly the command it would have with no disturbance and cannot respond; the disturbance leaves a persistent error. Feedback, by contrast, is computed from the measured error: the disturbance changes the actual position q, which changes the error, which drives the feedback command to oppose it. Feedback doesn't need to know the disturbance exists or what caused it — it only needs to see its effect on q. That's why disturbance rejection is feedback's job alone.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** The complete tracker is u = m·q̈_d + b·q̇_d + ℓ + PID(q_d − q), run once per joint, taking Module 7's reference and the measured state and producing an actuator command. It's the right deliverable because Module 9 integrates a system that must run in the real world: it needs both performance and robustness. Feedforward alone gives performance (lag-free tracking of the plan) but is fragile — any disturbance or model error leaves a persistent error. Feedback alone is robust but lags moving references. Only the combination delivers accurate tracking of the planned motion and rejection of the unplanned disturbances reality throws at it. That is the controller a real greenhouse arm needs, so it's the interface — tracking_controller(reference, measured_state) → actuator_command — Module 8 hands forward.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Unit 1 showed that open-loop execution drifts because it never measures the result, so any load, friction, or disturbance accumulates uncorrected. Feedforward-only is exactly that situation in sophisticated form: it computes a smart command from the plan and model, but like open-loop it never looks at the actual output, so a disturbance it didn't plan for produces an error it can't see or fix. The drift is the same failure — no feedback means no correction of the unexpected. Feedback was the cure in Unit 1 and is the cure here: by measuring q and acting on the error, it rejects whatever reality does that the plan omitted. The module's first lesson and its last are the same truth: you cannot ship without feedback.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Trusting a good model to remove the need for feedback (no model anticipates disturbances).
- Forgetting disturbances enter the plant, not the reference.
- Shipping feedforward-only — fast on paper, fragile on contact with reality.
