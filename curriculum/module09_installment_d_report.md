---
title: "Module 9 — Installment D Report (Units 7–8, capstone)"
module: 09
installment: D
decision: D-074
status: delivered — MODULE 9 COMPLETE
---

# Module 9 · Installment D — Recover + Full System Integration (capstone)

**Scope.** Units 7–8, lessons L25–L32. The loop closes and the whole system assembles; **Module 9 completes.**

**Unit 7 — Recover.** The orchestrator is **coordination, not a new layer** — the sixth stage. `recover(world, q_start, target=…, max_attempts, …)` consumes detection's localised fault + owner and dispatches a targeted response via `RECOVERY_POLICY`: re-perceive (NO_TARGET), retry-execute (TRACKING_FAILURE) — **retryable**; re-select (UNREACHABLE), skip (PLAN_INVALID) — **deterministic**. A retry budget + state across attempts gives three terminating exits: a transient fault recovers, a persistent retryable fault escalates at the budget (`retry-budget-exhausted`), a deterministic fault escalates immediately (`skip-target`).

**Unit 8 — Full System Integration (capstone).** The full pick cycle composes the six stages into one self-healing loop (L29). `harvest_row(world, inject=…)` runs the cycle across a whole row under a ledger — **graceful degradation**: a mid-row fault recovers (transient) or is skipped-with-reason (deterministic), the row always completes, one stubborn fruit never stalls it (L30). Guarantees vs boundaries are stated honestly — accounting / completion / graceful degradation / localised faults, but *not* completeness, diagnosis, or optimal sequencing (L31). Module 9 closes and hands off to Module 10 (L32).

**Flagship D — End-to-End Pick-Cycle Player (L8.2):** animate the full row harvest, inject a fault, watch recover / skip and the live ledger.

**Boundaries held.** **No new estimation, planning, or control theory** anywhere in the module — every stage wraps a real layer; detection is reading, recovery is coordination + bookkeeping.

**Verification.** All 32 Module 9 notebooks pass under Restart-and-Run-All; `mkdocs build --strict` green at **293 lesson pages**; 4 flagship demos clean.

**Module 9 totals:** 8 units · 32 lessons · 32 notebooks · 32 SVGs · 4 demos · 32 quizzes · 32 answer keys. **MODULE 9 COMPLETE (D-074) — 9 of 10 signed off. Paused at the Installment D milestone. Next: Module 10 — Digital Twin Capstone.**
