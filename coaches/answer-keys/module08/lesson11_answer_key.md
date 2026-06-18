---
module: 8
unit: 3
lesson: 3
type: answer_key
title: "Answer Key — Stable, Marginal, Unstable — and What Tips a Loop Over"
audience: coaches
---

# Answer Key 3.3 — Stable, Marginal, Unstable — and What Tips a Loop Over

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Stable: envelope decays, settles.

**Q2 — B.** Marginal: constant-amplitude ringing forever.

**Q3 — C.** Unstable: envelope grows, diverges.

**Q4 — D.** Too little gain causes sluggishness, not instability.

**Q5 — B.** Latency makes corrections mistimed, adding energy — as dangerous as excess gain.

---

**Q6 — model answer.** Stable: the oscillation envelope decays and the response settles to a constant — the joint reaches and holds the target (the normal, desired case). Marginal: the envelope is constant, so the response rings at fixed amplitude indefinitely — the joint never settles, buzzing about the target (usable for nothing precise, and right at the edge). Unstable: the envelope grows, each swing larger than the last, and the response diverges — on hardware the joint slams its limits, strips gears, or throws the payload. Stability is the safety property: stable is fine, marginal is the cliff edge, unstable is the crash.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** The three are too much gain, too little damping, and too much delay. Too much gain injects large corrections that, without enough damping to remove the energy, build into growing swings. Too little damping removes the mechanism (derivative action, friction) that bleeds energy out of fast motion, so oscillations persist or grow. Delay belongs because a controller acting on stale measurements computes its correction for a past state; by the time it's applied the joint has moved, so the correction can push in the wrong direction and add energy. Enough delay destabilises even a modest, well-damped loop — which is why loop timing matters as much as the gains.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** The slower sensor added latency to the feedback path. Even though the gains were untouched, the controller is now acting on older measurements, so its corrections are mistimed — applied after the joint has already moved past where they were computed for. That mistiming turns corrections that used to damp the motion into ones that reinforce it, growing the oscillation into divergence. The fix isn't necessarily lower gains: reduce the delay (faster sensor, less filtering, tighter loop timing) or add damping/derivative to widen the stability margin. This is the classic 'it started oscillating after we changed the hardware' delay-induced instability.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Treating marginal (sustained ringing) as acceptable — it's the edge.
- Blaming only the gains and ignoring delay or lost damping.
- Assuming sim stability implies hardware stability (real loops add delay).
