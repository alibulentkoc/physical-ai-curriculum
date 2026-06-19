---
module: 9
unit: 5
lesson: 20
type: answer_key
title: "Answer Key — Unit 5 Recap: Execute → Track"
audience: coaches
---

# Answer Key 5.4 — Unit 5 Recap: Execute → Track

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Unit 5 added the stage that judges (Track) and monitors health — the system gains eyes.

**Q2 — B.** Move (Execute), judge (Track verdict), monitor (telemetry), read.

**Q3 — B.** A run can succeed yet show worrying telemetry (fragile success).

**Q4 — B.** Unit 6 adds a failure taxonomy and automatic detection (encoded readings).

**Q5 — True.** Track owns the verdict; the controller only produced the error.

---

**Q6 — model answer.** Execute produces the motion. Track judges it against criteria (final error, RMS, pose) and returns a verdict with a reason — Track owns this, M8 only produced the error. System monitoring collects each layer's existing health signals (M6 manipulability, M8 effort, tracking error) into one dashboard. Reading combines verdict and gauges into an assessment. Health ≠ success: a run can succeed while telemetry shows a fragile near-singular pass — monitoring reveals what the verdict hides. The output is a judged, monitored, readable run for Unit 6's detector.
*Grading: credit the act-judge-monitor-read loop, ownership, and the health-vs-success distinction.*
