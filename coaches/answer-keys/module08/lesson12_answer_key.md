---
module: 8
unit: 3
lesson: 4
type: answer_key
title: "Answer Key — Tuning a Controller: A Practical Workflow"
audience: coaches
---

# Answer Key 3.4 — Tuning a Controller: A Practical Workflow

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** P → D → I.

**Q2 — B.** Raise Kp to the oscillation edge, then back off.

**Q3 — B.** D damps overshoot and buys Kp headroom.

**Q4 — B.** I erases the steady-state offset.

**Q5 — B.** Leave margin — payload/wear/delay are harsher than the bench.

---

**Q6 — model answer.** Step 1 — P: with I and D off, raise the proportional gain until the response is brisk and just begins to oscillate, then back off (to roughly half–two-thirds) for margin; this sets the basic speed and shrinks the offset. Step 2 — D: add derivative to damp the overshoot and ringing; because D adds damping it also buys headroom to push Kp a little higher for speed. Step 3 — I: add the smallest integral that erases the steady-state offset left under load in acceptable time. Then verify the four metrics (rise, overshoot, settling, steady-state error) and confirm comfortable stability margin. Each step fixes the defect the previous one left: P sets speed, D calms overshoot, I removes offset.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Because derivative damps the overshoot and ringing that aggressive proportional (and, later, integral) action causes, and that damping creates the stability headroom you need before adding integral. Integral inherently adds lag and tends to increase overshoot — if you add it to a loop that's already lightly damped, you push it toward oscillation. By adding derivative first you make the loop well-damped, so when you then add integral to remove the offset, the extra lag it brings doesn't tip the response into ringing. D before I means you erase the offset on a stable, damped foundation rather than an oscillatory one.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** The payload changed the effective load and inertia the controller faces, so the gains that were balanced for the unloaded joint are now mismatched — relatively too aggressive for the heavier, slower-responding joint — and the response overshoots and rings. The fix is to re-run the workflow for the loaded condition (or a representative worst case): back off Kp, increase Kd to restore damping, and adjust Ki for the new offset, leaving margin. Tuning with margin originally would have reduced the problem, since the loop wouldn't have been at the edge to begin with. If the payload varies widely, you'd consider gains scheduled to the load rather than a single fixed set — but always keeping margin so the worst case stays comfortably stable.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Tuning all three gains at once instead of one at a time.
- Tuning to the oscillation edge with no margin.
- Using integral for speed (it's for offset) or over-using derivative (amplifies noise).
