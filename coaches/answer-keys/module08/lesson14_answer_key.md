---
module: 8
unit: 4
lesson: 2
type: answer_key
title: "Answer Key — Feedback Reacts, Feedforward Anticipates"
audience: coaches
---

# Answer Key 4.2 — Feedback Reacts, Feedforward Anticipates

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Feedback acts on the measured error (after it forms).

**Q2 — B.** Feedforward acts on the known reference, before any error.

**Q3 — B.** u_ff = m·q̈_d + b·q̇_d + ℓ.

**Q4 — B.** Feedforward consumes q̇_d and q̈_d (plus q_d).

**Q5 — B.** With a good model, feedforward alone tracks with almost no lag.

---

**Q6 — model answer.** Feedback acts on the measured error — it must wait for the joint to fall behind before it does anything, so on a moving reference it is always a step behind (lag). Feedforward acts on the known reference: using the planned velocity and acceleration, it computes in advance the command needed to produce the planned motion and applies it the instant it's needed, before any error forms. On a known trajectory with a good model, feedforward therefore produces the right command at every moment without ever needing an error to exist, so there's almost no following error. Feedback reacts to the past; feedforward anticipates the future.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** The command is u_ff = m·q̈_d + b·q̇_d + ℓ. The term m·q̈_d uses the planned acceleration q̈_d and supplies the force to produce that acceleration (overcoming inertia). The term b·q̇_d uses the planned velocity q̇_d and supplies the force to overcome viscous damping at that speed. The term ℓ holds the known load. Together they are the command that, with a perfect model and no disturbance, would make the joint follow the planned trajectory exactly. The point is that q̇_d and q̈_d — the very signals Module 7 computed and feedback ignored — are exactly what feedforward needs, which is why the reference layer carries velocity and acceleration, not just position.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Because the controller needs them to anticipate. Position alone (q_d) tells the controller where to be, but not where it's heading or how hard to push to get there on time — so a position-only controller can only react after falling behind, producing following-error lag. The planned velocity q̇_d and acceleration q̈_d describe the motion's direction and effort in advance, and feed directly into the feedforward command (b·q̇_d and m·q̈_d). With them, the controller computes most of the command from the plan and tracks fast trajectories with almost no lag. So Module 7 computed the derivatives precisely so Module 8 could anticipate — it's the hinge that makes the two modules one system.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Thinking feedforward is just a higher gain (it's a different signal — the plan).
- Believing feedforward replaces feedback (it can't reject the unknown).
- Using only q_d for feedforward (anticipation needs q̇_d and q̈_d).
