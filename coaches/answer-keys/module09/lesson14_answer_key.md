---
module: 9
unit: 4
lesson: 14
type: answer_key
title: "Answer Key — Handoff Contracts: ξ_d, q̇, and Real-Time Execution"
audience: coaches
---

# Answer Key 4.2 — Handoff Contracts: ξ_d, q̇, and Real-Time Execution

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** (q_d, q̇_d, q̈_d) in consistent joint-space units — q_d for feedback, derivatives for feed-forward.

**Q2 — B.** ξ = J(q) q̇, and q̇ = J⁺ ξ_d via the (damped) pseudoinverse.

**Q3 — B.** The same frame (and consistent units); a base-frame Jacobian with a tool-frame twist is wrong.

**Q4 — B.** Real-time = fixed-Δt periodic execution, treated qualitatively; formal scheduling is out of scope.

**Q5 — True.** ξ = [v; ω] (linear on top) is the locked convention.

---

**Q6 — model answer.** Dropping q̇_d and q̈_d removes the feed-forward terms, so the controller reverts to pure feedback on q_d − q — it reacts instead of anticipating, so tracking lags, especially on fast segments, with no exception thrown. The violated contract is the reference → controller handoff, which must carry the full (q_d, q̇_d, q̈_d) because the controller's feed-forward depends on the derivatives. It is a silent seam bug, visible only as degraded tracking.
*Grading: require "feed-forward lost → lag" and naming the reference→controller contract.*
