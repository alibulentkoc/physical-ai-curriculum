---
module: 6
unit: 8
lesson: 30
type: answer_key
title: "Answer Key — Capstone Tracker"
audience: coaches
---
# Answer Key 8.2
**Q1 B · Q2 B · Q3 B · Q4 B · Q5 B.**
**Q6.** `(q_next, q_dot)` — the next configuration and the resolved joint-rate vector.
**Q7.** Euler integration of q̇ accumulates O(dt) error as J is recomputed at each step; smaller dt (or, later, feedback in M8) reduces it.
**Q8.** Consumes a commanded tool twist, produces a joint-rate stream; trajectory generation (M7) and feedback control (M8) are out of scope.
### Watch for: calling open-loop drift a bug — it is the expected, defining limitation that motivates M7/M8.
