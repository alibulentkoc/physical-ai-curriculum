---
module: 7
unit: 2
lesson: 2
type: answer_key
title: "Answer Key — Continuity Classes C⁰/C¹/C² and Why Jerk Matters"
audience: coaches
---

# Answer Key 2.2 — Continuity Classes C⁰/C¹/C² and Why Jerk Matters

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — C.** C¹ guarantees continuous velocity; acceleration may still jump.

**Q2 — B.** Continuous acceleration ⇒ continuous force ⇒ no shock loads.

**Q3 — B.** Bounded jerk is a separate quantitative requirement on top of C².

**Q4 — B.** Rest endpoints give C¹; an endpoint acceleration jump prevents C².

**Q5 — B.** Linear→C⁰, cubic→C¹, quintic→C².

---

**Q6 — model answer.** C⁰: position is continuous (velocity may jump). C¹: position and velocity are continuous (acceleration may jump). C²: position, velocity, and acceleration are all continuous (no force jumps).
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** A C² move whose acceleration ramps up very fast has large but finite jerk. Nothing is discontinuous, but the rapid force onset is felt as a snap. Unbounded jerk is to blame; bounding jerk is the separate finishing requirement.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** C¹: velocities match across the join, $v^-=v^+$. C² also requires accelerations to match, $a^-=a^+$ (with positions already equal). 'Stop at every via-point' makes velocities zero on both sides (trivially C¹) but is wasteful; matching nonzero $v$ and $a$ keeps C² continuity without stopping.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Equating 'continuous' with 'smooth' — C⁰ is continuous yet can be violent.
- Stopping at C² and ignoring jerk.
- Thinking zero endpoint velocity implies C² (it gives only C¹).
