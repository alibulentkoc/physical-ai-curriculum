---
title: "Module 9 — Installment C Report (Units 5–6)"
module: 09
installment: C
decision: D-073
status: delivered
---

# Module 9 · Installment C — Execute → Track + Failure Detection

**Scope.** Units 5–6, lessons L17–L24. The system gains the ability to judge, monitor, name, detect, and localise failure — everything except recover.

**Unit 5 — Execute → Track.** `track(record, …)` returns a success verdict against explicit criteria (final error, RMS, pose) with a localising reason; `system_monitor(record)` collects the health signals every layer already emits (M6 w/σ_min/κ, M8 effort, tracking error) into one dashboard. Key distinctions: *reached ≠ succeeded*, *health ≠ success*. A telemetry option was added additively to `execute_reference`.

**Unit 6 — Failure Detection.** `FAILURE_TAXONOMY` (six integration events on existing signals, split failure vs warning); health-signal **guards** that halt-or-flag at each seam (`run_pipeline`); `localize(event)` answers **What failed? → Where? → Who owns the fix?** — with the insight that where a fault surfaces can differ from who owns the fix (e.g. UNREACHABLE surfaces at the IK seam, owned by Understand).

**Flagship C — Failure-Injection Sandbox (L6.2):** inject occlusion / unreachable / block / disturbance / near-singular and watch the guarded pipeline halt or flag at the right seam with the triad.

**Boundaries held.** Detection is thresholded reading of existing outputs — **no estimation, fault-diagnosis, or control theory.** Recovery deferred to Unit 7. **APPROVED (D-073).**
