---
module: 7
unit: 2
lesson: 3
type: answer_key
title: "Answer Key — Polynomial Time Scaling: Cubic vs Quintic"
audience: coaches
---

# Answer Key 2.3 — Polynomial Time Scaling: Cubic vs Quintic

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** A cubic matches start/end position and velocity (4 conditions).

**Q2 — B.** The quintic additionally zeros endpoint accelerations → C².

**Q3 — B.** The quintic has slightly higher mid-move peaks (price of gentle ends).

**Q4 — B.** Cubic endpoint acceleration is nonzero, $\pm6\Delta/T^2$.

**Q5 — C.** Matching endpoint jerk too needs a degree-7 (septic) polynomial.

---

**Q6 — model answer.** A cubic satisfies 4: start and end position and start and end velocity. A quintic satisfies 6: also start and end acceleration. Each matched endpoint derivative consumes one coefficient and buys one rung of continuity.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** The cubic only constrains endpoint position and velocity, so its endpoint acceleration is whatever falls out — nonzero ($\pm6\Delta/T^2$), jumping from the resting zero. The quintic adds endpoint-acceleration conditions (=0), so acceleration is continuous with rest → C², no jump.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Six boundary conditions: position, velocity, acceleration at t=0 (0,0,0 for rest start) and at t=T (q_f, v_f, 0). That is a quintic (degree 5). 'Stop at the handoff' would be wrong because the following segment is already cruising; matching v_f keeps the motion C² across the handoff.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Using a cubic where C² (gentle ends) is needed.
- Forgetting the quintic's higher peaks when checking limits.
- Thinking more degree is always better — match degree to required continuity.
