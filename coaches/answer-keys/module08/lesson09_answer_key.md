---
module: 8
unit: 3
lesson: 1
type: answer_key
title: "Answer Key — When Correction Goes Wrong: From Too Weak to Runaway"
audience: coaches
---

# Answer Key 3.1 — When Correction Goes Wrong: From Too Weak to Runaway

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** sluggish → clean → overshoot → oscillation → runaway.

**Q2 — B.** Too weak: slow, lagging, settles short.

**Q3 — B.** Too strong: overshoot and ringing.

**Q4 — B.** Delay can turn a fine loop into runaway oscillation.

**Q5 — B.** The goal is balance, not maximum correction.

---

**Q6 — model answer.** Too weak: the joint approaches the target slowly and settles short, under-correcting (a visible offset, sluggish). As strength increases it reaches a good regime: brisk, smooth arrival on target. Push further and it overshoots — sailing past the target and ringing back. Stronger still (or with damping removed) it oscillates with sustained, non-decaying swings. Beyond that, or with delay in the loop, the swings grow instead of shrinking and the joint runs away — divergence. Same joint and target; the entire character is set by how hard it corrects.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Delay means the controller acts on a measurement from the past — it corrects for where the joint was, not where it is now. By the time the correction is applied, the joint has moved on, so the correction can be in the wrong direction, adding energy to the motion instead of removing it. With enough delay, each swing is reinforced rather than damped, and the oscillation grows into divergence — even though the gains were sensible. This is the swing pushed a beat late: same push strength, but mistimed, so the arc grows. It's why latency, not just gain, is a leading cause of runaway.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Because the behaviour spectrum ends in runaway. Increasing corrective strength helps only up to a point: it sharpens tracking and shrinks offset, but past the balance point it causes overshoot, then sustained oscillation, then divergence that can damage hardware. Maximum correction sits at the dangerous end of the spectrum. The goal is balance — enough strength to be responsive and accurate, with enough damping and margin that the loop stays comfortably stable as the payload, wear, and delay vary. Good control optimises for a well-shaped, safely-stable response, not for the largest possible gain.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Believing more gain is always better (the spectrum ends in runaway).
- Thinking only gain — not delay — causes instability.
- Confusing too-weak (sluggish/offset) with a broken controller.
