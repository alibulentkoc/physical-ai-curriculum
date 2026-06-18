---
module: 8
unit: 5
lesson: 4
type: answer_key
title: "Answer Key — The Command Pipeline and the Feasibility Envelope"
audience: coaches
---

# Answer Key 5.4 — The Command Pipeline and the Feasibility Envelope

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** reference → controller → requested command → actuator → delivered effort → motion

**Q2 — B.** the effort and rate the actuator can actually deliver (plus the deadband floor)

**Q3 — B.** the missing effort is physically unavailable — the actuator can't deliver it

**Q4 — B.** re-plan the trajectory to fit inside the envelope (e.g., slow it)

**Q5 — B.** grounding trajectory feasibility in the actuator's hardware limits

---

**Q6 — model answer.** The feasibility envelope is the set of efforts and rates the actuator can actually deliver: the delivered effort is bounded by ±u_max, its rate of change by ±r_max, and there is a deadband floor below which nothing is delivered. A trajectory is trackable only if the effort the controller must request to follow it stays inside these bounds for the whole motion. When it does, delivered ≈ requested everywhere and tracking is tight; when the demand exceeds the envelope, the actuator clips and/or slews, the delivered effort falls short, and a tracking error opens that no gain can close.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** The controller, target, and actuator are identical; only the trajectory's aggressiveness changed. The gentle version stays inside the envelope, so it's delivered faithfully and tracked almost perfectly. The aggressive version demands more effort than u_max can deliver, so the actuator clips most of the run and the trajectory is missed. The envelope — not the controller — drew the line between trackable and not, which is the unit's thesis: the boundary of achievable motion belongs to the actuator.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** When the actuator clips, the controller is already requesting more than the hardware can deliver; the missing effort is physically unavailable, so increasing the gains just requests even more impossible effort and changes nothing about what's delivered. The only way to make the motion trackable is to lower its demand until it fits the envelope — exactly Module 7's feasibility re-planning (slow the move, smooth it, reduce peak acceleration). The alternative is bigger hardware (a larger envelope), but re-planning is usually the cheaper, principled fix.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Believing a good controller can track anything — beyond the envelope no gain can close the gap.
- Re-tuning instead of re-planning when the actuator clips.
- Ignoring the rate limit — a move can be within the effort ceiling yet demand an impossible slew.
