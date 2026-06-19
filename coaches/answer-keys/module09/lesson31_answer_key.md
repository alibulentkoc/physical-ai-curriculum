---
module: 9
unit: 8
lesson: 31
type: answer_key
title: "Answer Key — Reading the Integrated System: Guarantees, Degradation, and Boundaries"
audience: coaches
---

# Answer Key 8.3 — Reading the Integrated System: Guarantees, Degradation, and Boundaries

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Accounting — every fruit ends harvested or skipped-with-reason (not completeness).

**Q2 — C.** Root-cause diagnosis is out of scope; the system localises that a fault occurred, not why.

**Q3 — B.** If the two are skipped-with-reason, it degraded correctly — best-effort, not completeness.

**Q4 — B.** The harvest report lets an operator judge the run (harvested, skipped-with-reason, attempts, recovered).

**Q5 — True.** Honest boundaries are an engineering deliverable; overclaiming causes field failures.

---

**Q6 — model answer.** Guarantees (any two): accounting (every fruit harvested or skipped, none lost); completion (the row always finishes); graceful degradation (recover or skip, never stall, bounded by the retry budget); localised faults (every skip carries a fault code and owner). Non-guarantees (any two): completeness (not every fruit picked — best-effort); root-cause diagnosis (localise, not explain physics); optimal sequencing (selection order, not optimal); new dynamics/control (qualitative M8 plant, no new theory).
*Grading: require two valid guarantees and two valid out-of-scope items.*
