---
module: 7
unit: 2
lesson: 1
type: answer_key
title: "Answer Key — Position, Velocity, Acceleration, Jerk"
audience: coaches
---

# Answer Key 2.1 — Position, Velocity, Acceleration, Jerk

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** $\dot q=q'(s)\dot s$.

**Q2 — B.** The curvature term $q''\dot s^2$ survives when $\ddot s=0$.

**Q3 — B.** Jerk is the third derivative of position, $\dddot q$.

**Q4 — B.** Motion derivatives = $s$'s derivatives scaled by the displacement $(q_f-q_0)$.

**Q5 — B.** A lurch is the sudden onset of acceleration — large jerk.

---

**Q6 — model answer.** q(t)=q(s(t)). Velocity: $\dot q=q'(s)\dot s$. Acceleration: $\ddot q=q'(s)\ddot s+q''(s)\dot s^2$ — a tangential term from changing speed plus a curvature term from the path bending while moving.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Even with $\ddot s=0$, the curvature term $q''\dot s^2$ is nonzero because the path bends. The acceleration points along $q''$ — toward the center of curvature (centripetal). Doubling path speed quadruples this acceleration ($\propto\dot s^2$), which is why curvature couples allowable speed to feasibility.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** No. 'At rest' means zero velocity ($\dot q(0)=0$), but a cubic has nonzero acceleration at the start ($\ddot q(0)\ne 0$). Velocity and acceleration are independent endpoint conditions; the quintic is what additionally zeros the endpoint acceleration.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Forgetting the curvature term — a curved path accelerates the tool even at constant speed.
- Confusing $\dot s$ (progress rate) with $\dot q$ (actual velocity).
- Assuming 'at rest' implies zero acceleration.
