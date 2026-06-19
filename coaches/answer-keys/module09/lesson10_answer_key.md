---
module: 9
unit: 3
lesson: 10
type: answer_key
title: "Answer Key — Invoking the Planner: Calling the Reference Layer"
audience: coaches
---

# Answer Key 3.2 — Invoking the Planner: Calling the Reference Layer

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Call the planner, check validated, hand off the reference — three verbs, no planning math.

**Q2 — B.** reference(t) returns q_d, qd_d, qdd_d (and info) at time t.

**Q3 — B.** validated=False means the plan failed its checks — route to Recover, do not execute.

**Q4 — B.** Module 7 is wrapped verbatim; Module 9 invokes it and routes its output.

**Q5 — True.** qd_d and qdd_d are the feed-forward terms Module 8 uses; keep them in the handoff.

---

**Q6 — model answer.** Module 7 is verified; reimplementing planning in the seam would duplicate and eventually contradict it — two sources of truth that drift. The discipline is to trust the verified layer, call it through its interface (q_start, q_goal, limits → reference, validated), and own only the call site and handoff, keeping the trajectory math in one place.
*Grading: credit the single-source-of-truth / no-duplication argument.*
