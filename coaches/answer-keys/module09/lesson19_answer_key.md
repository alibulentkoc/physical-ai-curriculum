---
module: 9
unit: 5
lesson: 19
type: answer_key
title: "Answer Key — Case Study: Reading Telemetry"
audience: coaches
---

# Answer Key 5.3 — Case Study: Reading Telemetry

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Reading is interpreting the pattern across signals into an assessment, not one gauge.

**Q2 — B.** Error/effort spike with nominal manipulability = an external strain on execution (a disturbance).

**Q3 — B.** A sharp manipulability drop = a near-singular geometry/planning condition (the path grazed a singularity).

**Q4 — B.** A near-singular, high-effort success should be flagged as fragile, not ignored.

**Q5 — True.** The reading begins answering what happened / where to look — the on-ramp to Unit 6.

---

**Q6 — model answer.** It failed on RMS (poor tracking throughout) with moderate peak error/effort — but the standout is manipulability 0.003, an order of magnitude below the healthy ~0.086. That points to the trajectory passing very near a singularity, where tracking naturally degrades. Reading: "failed on tracking quality, most likely because the planned path grazed a near-singular configuration — a geometry/planning condition, not a disturbance. Look at the configurations the plan traversed."
*Grading: require identifying manipulability as the moved signal and a geometry/planning (not disturbance) localisation.*
