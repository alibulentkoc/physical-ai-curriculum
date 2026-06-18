---
module: 8
unit: 2
lesson: 3
type: answer_key
title: "Answer Key — Derivative Control: Anticipate and Damp"
audience: coaches
---

# Answer Key 2.3 — Derivative Control: Anticipate and Damp

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Derivative acts on ė, the rate of change of error.

**Q2 — B.** It behaves like a brake/damper opposing fast changes.

**Q3 — B.** Damping from D buys gain headroom for higher P/I.

**Q4 — B.** Derivative amplifies measurement noise.

**Q5 — B.** Filter the derivative / derivative-on-measurement to tame noise.

---

**Q6 — model answer.** Derivative control acts on ė, the rate the error is changing, like a brake that senses how fast you're approaching a stop. As the joint rushes toward the target the error is shrinking fast (ė large and negative), so the derivative term produces an opposing command that slows the approach before the joint arrives — like easing the brake as you near a parking spot instead of slamming it at the line. This anticipatory braking bleeds off momentum ahead of the target, so the joint settles cleanly instead of overshooting and ringing the way pure P or PI does.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Gain headroom is the room to use larger proportional and integral gains — for faster, tighter response — without the loop overshooting or going unstable. Strong P/I alone tends to ring because there's nothing to damp the energy they inject. Derivative action adds damping: it opposes fast error changes, so it absorbs the oscillation that high P/I would cause. With D present, you can raise Kp and Ki further before the response becomes oscillatory, getting a faster, more accurate loop than P/I could safely achieve alone. So D 'buys' the headroom to be more aggressive elsewhere.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Differentiation responds to the rate of change of the signal, and noise is rapid small fluctuation — so taking the derivative of a noisy measurement multiplies those fast wiggles into large, jagged swings in the command (dividing tiny noise by the small time step blows it up). A smooth proportional command becomes a jittery derivative command. Remedies include low-pass filtering the derivative term so only genuine trends pass, taking the derivative of the measurement rather than the error (derivative-on-measurement, which also avoids spikes on setpoint changes), and keeping Kd modest. These keep the damping benefit while suppressing the noise it would otherwise amplify.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Thinking D removes steady-state error (that's integral's job).
- Cranking Kd on a noisy sensor without filtering (amplifies noise into jitter).
- Confusing D (rate of error) with I (accumulated error).
