---
module: 8
unit: 7
lesson: 7.2
type: answer_key
title: "Answer Key 7.2 — The Periodic Control Loop: Running at a Fixed Rate"
audience: coaches
---

# Answer Key 7.2 — The Periodic Control Loop: Running at a Fixed Rate

*Coaches' key. Multiple-choice answers with the correct option; model answers for the short-response items, with grading guidance; and common misconceptions to watch for.*

**Q1 — B.** Periodic task: sense → compute → actuate each period

*Why:* On hardware the loop executes once per control period, then waits.

**Q2 — B.** 1/T_c

*Why:* Rate is the reciprocal of the period (e.g., 1 ms → 1 kHz).

**Q3 — B.** sense + compute + actuate fit within T_c

*Why:* All three steps must complete within one period (worst-case version is the real-time requirement).

**Q4 — B.** It acts at sample instants and holds the command between them

*Why:* The controller acts at t = 0, T_c, 2T_c, … and holds its command in between (zero-order hold).

**Q5 — B.** RMS ≈ 0.0007 (essentially perfect)

*Why:* At a high enough rate the discrete execution reproduces the continuous design.

**Q6 — model answer.** Sense (read the measured state), compute (feedforward + PID through the actuator), actuate (send the command). They are bounded by the per-period timing budget: their total must fit within the control period T_c.

**Q7 — model answer.** A lower bound from stability: too low a rate adds loop delay and destabilises (Unit 6). An upper bound from the budget: too high a rate shrinks the per-period time available to finish the work. A good rate sits between them.

**Q8 — model answer.** Because it acts at closely spaced sample instants and holds the command between them; at a high rate the held-between-samples staleness is negligible, so the sampled loop behaves like the continuous one. (Formal sampled-data analysis is out of scope.)

*Grading: award full credit for a short answer that captures the key idea in the model answer, even if briefer or differently worded; partial credit if the core mechanism is named but not fully explained.*

### Common misconceptions to watch for

- Imagining the controller runs continuously; on hardware it runs once per period and holds the command between.
- Maximising the rate blindly — a faster rate shrinks the per-period budget and stresses the worst case.
- Forgetting the rate is bounded below by stability — too slow adds loop delay and destabilises (Unit 6).
