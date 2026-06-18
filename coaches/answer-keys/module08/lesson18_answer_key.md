---
module: 8
unit: 5
lesson: 2
type: answer_key
title: "Answer Key — Saturation and Integral Windup"
audience: coaches
---

# Answer Key 5.2 — Saturation and Integral Windup

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — A.** the actuator's effort ceiling; commands above it are discarded

**Q2 — B.** the persistent error keeps the integrator accumulating command the actuator can't use

**Q3 — B.** a large overshoot once the joint reaches the target

**Q4 — B.** bounding the integrator so it can't bank command the actuator can't deliver

**Q5 — B.** degrades tracking on demanding moves because the needed effort can't be delivered

---

**Q6 — model answer.** On a large move the proportional command alone exceeds u_max, so the actuator is pinned at the ceiling and the joint climbs slowly. Because the joint can't keep up, the error stays positive for a long time, and the integrator — whose rule is to accumulate persistent error — keeps growing even though the extra command it produces is discarded by the saturated actuator. By the time the joint finally reaches the target, the integrator has banked a large value; with the error now near zero the banked integral keeps the command saturated, driving the joint past the target. That overshoot is the wound-up integral being honoured.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Windup is a controller problem, not an actuator problem: the actuator's ceiling is fixed, but the integrator was banking command the actuator could never deliver. The anti-windup clamp simply bounds the integrator (|e_i| ≤ clamp), sized near the steady command the joint actually needs, so it can't accumulate unusable command during saturation. The ceiling is unchanged; what changes is that the controller stops making the ceiling's consequences worse, so the joint settles near the target instead of overshooting.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** The gains and the saturation ceiling are identical in both runs, so neither the controller's aggressiveness nor the actuator's limit explains the difference — only the windup does. The plain integrator banks a large value during the long saturated climb and then overshoots far past the target (≈69%). The clamped integrator can't bank that unusable command, so it settles with a much smaller overshoot (≈18%). The lesson: the cure for saturation-driven overshoot is anti-windup, not detuning the gains.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Detuning the whole loop to fix overshoot that only appears at the limit (the cause is windup).
- Assuming more integral always helps — under saturation it just means more windup.
- Forgetting that command above u_max is discarded and only feeds windup.
