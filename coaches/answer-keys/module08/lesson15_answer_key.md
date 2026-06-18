---
module: 8
unit: 4
lesson: 3
type: answer_key
title: "Answer Key — Feedforward + Feedback Together"
audience: coaches
---

# Answer Key 4.3 — Feedforward + Feedback Together

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — C.** u = u_ff + u_fb.

**Q2 — B.** Feedforward: known plan; feedback: unknown residual + disturbance.

**Q3 — B.** The combination tracks several times tighter on the identical trajectory.

**Q4 — B.** Feedback effort is smaller — feedforward did the bulk.

**Q5 — B.** Feedback corrects the mismatch residual feedforward can't.

---

**Q6 — model answer.** The command is u = (m·q̈_d + b·q̇_d + ℓ) + PID(q_d − q): a feedforward term plus a feedback term. Feedforward handles the known, planned motion — using Module 7's q̇_d and q̈_d it supplies, in advance, most of the command the trajectory needs, giving lag-free performance. Feedback handles the unknown — the model is never perfect and disturbances happen, leaving a small residual error that the PID term corrects online. Because feedforward already did the bulk of the work, the residual is small, so the feedback gains can be modest and the loop stays well inside its stability margin. Feedforward for performance, feedback for robustness.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Feedback-only must generate the entire corrective command reactively: it waits for an error to form, then responds, so it always trails and leaves a following error. Adding feedforward changes the feedback's job: the feedforward term supplies the bulk of the command from the plan in advance, so the joint nearly follows the trajectory on its own, and only a small residual error remains for feedback to correct. Correcting a small residual takes a small command, so the feedback effort is smaller — and because the residual is small, the same gains drive it close to zero, giving much tighter tracking (several times lower RMS) on the identical trajectory. Less work, better result.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** It isn't. Higher feedback gains still rely on an error existing before the controller acts, so they only reduce — never eliminate — the following-error lag, and pushing them up spends stability margin and amplifies noise. Feedforward+feedback adds a different signal entirely: a command computed from the known plan (q̇_d, q̈_d), applied before any error forms. That anticipatory term removes the lag at its source rather than reacting harder to it. In fact, with feedforward present the feedback gains can be gentler, not higher, because feedback only handles the small residual. So the combination is more accurate and more stable than a high-gain feedback-only loop — a fundamentally different mechanism, not just a louder version of feedback.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Thinking the combination just means higher gains (it's a different signal).
- Expecting large feedback alongside feedforward (good feedforward → small feedback).
- Comparing on different trajectories instead of the identical one.
