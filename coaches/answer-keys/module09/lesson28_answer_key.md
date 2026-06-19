---
module: 9
unit: 7
lesson: 28
type: answer_key
title: "Answer Key — Unit 7 Recap: Recover"
audience: coaches
---

# Answer Key 7.4 — Unit 7 Recap: Recover

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Unit 7 added Recover — pure coordination, the sixth stage.

**Q2 — B.** Three exits: recovered, deterministic escalation, budget-exhaustion escalation.

**Q3 — B.** No — predicting persistence is estimation theory; bounded retry is the integration answer.

**Q4 — B.** Unit 8 assembles the full self-healing pick cycle across a harvest.

**Q5 — True.** Recovery adds no new theory — only control flow and bookkeeping around existing layers.

---

**Q6 — model answer.** Transient disturbance → recovers (TRACKING_FAILURE at attempt 0, retry-execute succeeds at attempt 1) because the kick is gone on the retry. Persistent disturbance → escalates at the budget (retry-budget-exhausted) because retry-execute fails identically every attempt until N is spent. Blocked goal → escalates immediately (PLAN_INVALID is deterministic, skip-target at attempt 1) because re-planning the same goal against the same obstacle is futile. Three faults, three terminating outcomes, all from the same orchestrator coordinating the same layers — the budget/counter and the retryable/deterministic tag decide which.
*Grading: require all three outcomes with correct reasons (transient clears, persistent exhausts budget, deterministic immediate).*
