---
module: 9
unit: 8
lesson: 29
type: answer_key
title: "Answer Key — The Full Pick Cycle: Six Stages as One Loop"
audience: coaches
---

# Answer Key 8.1 — The Full Pick Cycle: Six Stages as One Loop

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** The six stages composed into one self-healing loop.

**Q2 — B.** Each stage is a wrapped existing layer.

**Q3 — B.** The only new content is the control flow (stage order, seam contracts, recovery loop).

**Q4 — B.** A healthy vs recovered pick differ only in the recovery bookkeeping (recovered, n_attempts).

**Q5 — True.** A complete pick cycle includes Recover; a forward-only path is not the full system.

---

**Q6 — model answer.** Healthy: the forward path runs once, Track passes, recover reports success=True, recovered=False, n_attempts=1. Transiently disturbed: the first attempt's Track fails (TRACKING_FAILURE), Recover (retry-execute, retryable) re-runs Execute, the disturbance has cleared, Track passes, and recover reports success=True, recovered=True, n_attempts=2. Only the recovery bookkeeping differs — the same composed stages, re-sequenced by the orchestrator, handle both cases.
*Grading: require both outcomes and the "only bookkeeping differs" insight.*
