---
module: 7
unit: 4
lesson: 3
type: answer_key
title: "Answer Key — Orientation Interpolation: SLERP"
audience: coaches
---

# Answer Key 4.3 — Orientation Interpolation: SLERP

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Averaging rotation-matrix entries gives a non-rotation (skews/shrinks).

**Q2 — B.** SLERP follows the shortest arc at constant angular rate, always valid.

**Q3 — B.** Sign-flip the far quaternion when q0·q1<0 to take the short way.

**Q4 — B.** Planar SLERP is shortest-arc angle interpolation (wrap to (−π,π]).

**Q5 — B.** Euler-angle interpolation risks gimbal lock and detours.

---

**Q6 — model answer.** Orientations don't live in a flat space, so the entry-wise average of two rotation matrices (or quaternions) is generally not a rotation at all — it skews and shrinks, like a slack dial. SLERP treats each orientation as a point on the unit sphere of rotations and slides along the great-circle arc between them: it stays on the sphere (always a valid rotation), takes the shortest path, and moves at constant angular rate — the rotational analog of a straight line.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** (1) Validity: the result is a unit quaternion for every s, so it's always a valid rotation. (2) Shortest arc: it traces the great-circle (shortest) path between the two orientations (with a sign flip to guarantee the short way). (3) Constant rate: it turns at a constant angular speed. Together these give a smooth, well-defined orientation path with no detours, no invalid intermediate states, and no gimbal lock.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** The shortest-arc difference is wrap(−170−170)=wrap(−340°)=+20°, so the tool turns +20° through 180° (the short way), reaching −180°/180° at the midpoint. Naive linear interpolation of the raw angles would sweep 170→−170 as −340°, spinning the wrist almost all the way around the long way — clearly wrong. SLERP/shortest-arc avoids that by wrapping the difference.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Averaging rotation matrices/quaternions naively (result isn't a rotation).
- Forgetting the shortest-arc sign flip (turns the long way).
- Interpolating Euler angles (gimbal lock); interpolating orientation independently of position timing.
