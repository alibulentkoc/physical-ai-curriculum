---
module: 9
unit: 8
lesson: 30
type: answer_key
title: "Answer Key — Capstone: Harvesting a Row with Injected Failure"
audience: coaches
---

# Answer Key 8.2 — Capstone: Harvesting a Row with Injected Failure

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** The pick cycle iterated under a ledger of harvested/skipped fruit.

**Q2 — B.** The ledger guarantees termination and progress — each fruit decided once, the row completes.

**Q3 — B.** A transient fault recovers (harvested, recovered=True); the row still finishes.

**Q4 — B.** A deterministic fault is skipped-with-reason; the rest harvest; never stalls.

**Q5 — True.** Graceful degradation: a definite outcome per fruit, never stalling.

---

**Q6 — model answer.** The targeted fruit fails TRACKING_FAILURE on every attempt; the fault is retryable but persistent, so Recover exhausts the budget and escalates (retry-budget-exhausted) after 3 attempts — the fruit lands in the skipped set. Every other fruit harvests normally. Ledger: all-but-one harvested, one skipped (TRACKING_FAILURE, budget-exhausted), complete=True. The row still finishes; the persistent fault costs three attempts and a skip, not a stall.
*Grading: require budget-exhaustion skip for the one fruit, the rest harvested, complete=True.*
