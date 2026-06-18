---
module: 8
unit: 2
lesson: 2
type: answer_key
title: "Answer Key — Integral Control: Erasing Steady-State Error (and Windup)"
audience: coaches
---

# Answer Key 2.2 — Integral Control: Erasing Steady-State Error (and Windup)

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Integral commands on the accumulated error ∫e.

**Q2 — B.** Its only equilibrium is e = 0, so it erases the offset.

**Q3 — B.** Windup = ∫e ballooning while the actuator is saturated.

**Q4 — B.** An anti-windup clamp limits the integral term.

**Q5 — B.** Integral adds lag and can cause overshoot.

---

**Q6 — model answer.** Integral action accumulates the error over time and commands Ki·∫e. As long as any steady error persists, the integral keeps growing, so the command keeps increasing — it cannot reach equilibrium until the error is zero. In effect, the integrator supplies the constant command needed to balance the load without requiring a standing error to generate it (unlike proportional). So the only resting state is e = 0: the offset that P-only control structurally required is erased, because the integrator, not a residual error, now provides the steady holding command.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Windup happens when the actuator saturates (hits its limit) during a large error: the joint can't move any faster, but the integrator keeps accumulating the persistent error, so ∫e balloons to a huge value. When the joint finally catches up, that enormous accumulated term keeps driving the output past the target, causing a large overshoot and slow recovery. An anti-windup clamp limits the integral term (caps ∫e or its contribution) so it can't balloon while saturated; when the actuator comes out of saturation the integrator is at a sane value and the response settles cleanly instead of overshooting badly.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Integral action adds phase lag: because it responds to accumulated past error rather than the present, it reacts slowly and can push the system past the target, adding overshoot and even oscillation if Ki is too large. It also can wind up against saturation. The tuning implication is that Ki should be large enough to erase the offset in reasonable time but small enough to avoid excessive overshoot and ringing, usually paired with derivative action to damp the overshoot integral introduces and with an anti-windup clamp to handle saturation. It's a balance, not a 'more is better' knob.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Thinking integral acts on the present error (it acts on accumulated error).
- Ignoring windup when the actuator saturates (clamp the integral).
- Assuming more Ki is always better (it adds lag/overshoot).
