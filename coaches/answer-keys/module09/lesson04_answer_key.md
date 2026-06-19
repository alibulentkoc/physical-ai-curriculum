---
module: 9
unit: 1
lesson: 4
type: answer_key
title: "Answer Key — Unit 1 Recap: The System View"
audience: coaches
---

# Answer Key 1.4 — Unit 1 Recap: The System View

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Seams, spine, trace.

**Q2 — B.** All-unripe → `current_target = None` is a correct Understand outcome (nothing to pick), not a failure.

**Q3 — B.** Passing parts ≠ correct system; the seams are untested by per-layer suites.

**Q4 — B.** Module 9 adds the seams (data flow, contracts, ownership, recovery), not new layers; the digital twin is Module 10.

**Q5 — False.** You need each stage's owner (and I/O), not just the names — the owner is what you reason about under failure.

---

**Q6 — model answer.** *Seams:* a system of individually correct layers can fail in the handoffs between them, so integration is its own discipline. *Spine:* the module is organised as Perceive → Understand → Plan → Execute → Track → Recover, each stage with a named owner, an input, and an output. *Trace:* we verify cooperation by snapshotting the shared blackboard after each stage and checking the contract chain link by link, which localises any fault to a specific stage.
*Grading: one accurate sentence per idea; full credit for all three, partial otherwise.*
