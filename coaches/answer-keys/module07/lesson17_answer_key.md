---
module: 7
unit: 5
lesson: 1
type: answer_key
title: "Answer Key — Why a Trajectory Can Be Infeasible: Velocity and Acceleration Limits"
audience: coaches
---

# Answer Key 5.1 — Why a Trajectory Can Be Infeasible: Velocity and Acceleration Limits

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** A smooth, goal-reaching trajectory can still demand impossible speeds/accelerations.

**Q2 — B.** Feasibility caps maximum velocity and maximum acceleration per joint.

**Q3 — B.** Peak speed scales as 1/T, peak acceleration as 1/T².

**Q4 — B.** Peaks scale with displacement; the largest-Δq joint binds first.

**Q5 — B.** A reachable goal can still have an infeasible timing — separate checks.

---

**Q6 — model answer.** You can plan a smooth motion to cross the room in half a second; the plan's shape is fine, but below some duration it demands a top speed your legs can't reach — it's infeasible, not wrong. A robot joint is the same: a smooth quintic over too short a duration demands a peak speed or acceleration past the motor's limit. The geometry never changed; the timing pushed the peaks past the hardware ceiling. Feasibility asks whether the demanded peaks fit under the limits.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** For a quintic, peak speed = (15/8)|Δq|/T and peak acceleration = (10/√3)|Δq|/T² — speed scales as 1/T, acceleration as 1/T². So shrinking T inflates the peaks (acceleration faster than velocity) and a short-enough T always breaks feasibility. The implication: going the other way — lengthening T (slowing down) — always shrinks the peaks back under the limits, which is the fix in the next lesson.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** The 0.2 s snap demands very high wrist speeds and accelerations (peaks scale as 1/T and 1/T²), almost certainly exceeding the small distal motor's velocity/acceleration limits — so the controller either clamps the speed (smearing the move) or rejects the trajectory as infeasible. The goal is reachable; the timing isn't. The fix is to lengthen the duration until the peaks fall under the limits.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Confusing feasibility with smoothness (a C² quintic can be infeasible).
- Confusing feasibility with reachability (reachable goal, impossible timing).
- Forgetting acceleration grows as 1/T² and usually binds before velocity at short T.
