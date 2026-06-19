---
module: 9
unit: 5
lesson: 17
type: answer_key
title: "Answer Key — Closing the Loop: Tracking Error and Success Criteria"
audience: coaches
---

# Answer Key 5.1 — Closing the Loop: Tracking Error and Success Criteria

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Track decides success; Execute only produces the motion.

**Q2 — B.** Final error, tracking RMS, and tool-pose reached — all three.

**Q3 — B.** Reached is necessary but not sufficient for succeeded (a plan to the wrong place could "reach").

**Q4 — B.** The thresholds are integration choices ("how good is good enough"), not new theory.

**Q5 — True.** The verdict names the first failed criterion — the start of fault localisation.

---

**Q6 — model answer.** Verdict: success = False, reason = rms. The arm ended near the reference and the tool is near the target, but tracking was poor along the way (RMS failed) — arrived correctly yet tracked badly mid-flight. An end-point-only check would wrongly pass it; the RMS criterion catches it.
*Grading: require reason = rms and the "arrived but tracked badly" interpretation.*

**Q7 — model answer.** Execute asks "what motion happened?" and produces it; Track asks "is it good enough?" and judges it. Conflating them allows false success or unnoticed failure. Track is the owned gate that turns motion into a verdict the back half acts on; M8 only produces the error Track reads.
*Grading: credit the different-questions framing and the ownership point.*
