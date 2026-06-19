---
module: 9
unit: 6
lesson: 24
type: answer_key
title: "Answer Key — Unit 6 Recap and Installment C Milestone"
audience: coaches
---

# Answer Key 6.4 — Unit 6 Recap and Installment C Milestone

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Judge, monitor, name, detect, and localise — everything except recover (Unit 7).

**Q2 — B.** The stage reached, the fired event(s), and a what/where/who with an owner.

**Q3 — B.** Recovery must be targeted, and targeting needs a reliable, localised, owned fault to aim at.

**Q4 — B.** Unit 7 consumes the localised fault with its owner.

**Q5 — True.** The detect-and-localise pipeline reads only existing signals — no new theory.

---

**Q6 — model answer.** Recovery must be targeted — the right stage acting on the right failure — and targeting requires a reliable, localised, owner-tagged fault. Building recovery first means responding to failures the system can't yet name or place, producing untargeted fixes that loop or compound. So detection is the dependency, not a parallel track. Unit 6 hands Unit 7 the stage reached, the fired event(s), and the what/where/who localisation with a named owner — exactly what a targeted recovery needs.
*Grading: credit the targeting-needs-localisation argument and the concrete handoff (event + stage + owner).*
