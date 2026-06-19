---
module: 9
unit: 7
lesson: 26
type: answer_key
title: "Answer Key — Targeted Responses: Matching Action to Owner"
audience: coaches
---

# Answer Key 7.2 — Targeted Responses: Matching Action to Owner

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** A recovery policy maps a localised fault to a targeted response, routed by owner.

**Q2 — B.** TRACKING_FAILURE (owned by Execute) → retry-execute; the disturbance may be transient.

**Q3 — B.** UNREACHABLE and PLAN_INVALID are deterministic (non-retryable) — they recur identically.

**Q4 — B.** Retrying a deterministic fault loops; only transient faults are worth retrying.

**Q5 — True.** Every response is an existing layer call re-invoked, not a new algorithm.

---

**Q6 — model answer.** Occlusion → NO_TARGET, owner Perceive/Understand, response re-perceive, retryable: a leaf may have shifted, so a fresh perception frame might reveal the fruit; the orchestrator re-perceives and proceeds if the occlusion was transient. Blocked goal → PLAN_INVALID, owner Plan, response skip-target, NOT retryable: the obstacle is fixed, so re-planning the same goal fails identically; the right action is to skip this fruit and move on. Same orchestrator, opposite handling — because the policy reads whether retrying could possibly help.
*Grading: require retryable re-perceive vs deterministic skip, justified by whether retrying can help.*
