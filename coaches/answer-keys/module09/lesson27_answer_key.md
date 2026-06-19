---
module: 9
unit: 7
lesson: 27
type: answer_key
title: "Answer Key — Retry Limits and State Across Attempts"
audience: coaches
---

# Answer Key 7.3 — Retry Limits and State Across Attempts

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** The budget and cross-attempt state guarantee termination; without them a persistent fault loops forever.

**Q2 — B.** A transient disturbance (attempt 0 only) recovers at attempt 2 — the retry runs clean.

**Q3 — B.** A persistent retryable fault escalates when the budget is spent (at attempt N).

**Q4 — B.** A deterministic fault escalates immediately at attempt 1 — retrying is pointless.

**Q5 — True.** The retry budget is an integration choice (no new theory) — big enough to clear transients, small enough to fail fast.

---

**Q6 — model answer.** A small budget (~3) is right. If a leaf briefly hides a fruit, one or two fresh perception frames usually reveal it, so ~2–3 re-perceives cover the common transient case. A budget of 1 gives up too early (one unlucky frame ends the pick); a budget of 50 stalls the robot on a permanently occluded fruit, when the better action after a few tries is to skip it and harvest the next. So a small budget balances clearing transients against failing fast on permanents. We do NOT make NO_TARGET non-retryable — re-perceiving genuinely helps transient occlusion; we just bound it. The counter is what lets the orchestrator honour the budget.
*Grading: credit a small bounded budget with the transient-vs-permanent justification; reject "make it non-retryable".*
