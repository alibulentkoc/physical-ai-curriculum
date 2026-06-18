---
module: 7
unit: 4
lesson: 4
type: answer_key
title: "Answer Key — Screw Motion: Unified Position + Orientation Interpolation"
audience: coaches
---

# Answer Key 4.4 — Screw Motion: Unified Position + Orientation Interpolation

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — C.** A screw rotates about and translates along one axis at constant twist.

**Q2 — B.** T(s)=T0·exp(s·log(T0⁻¹T1)) — replay a fraction s of the relative twist.

**Q3 — B.** Screw and decoupled agree at the endpoints but differ in between.

**Q4 — B.** Prefer decoupled when the position path must be a literal straight line.

**Q5 — B.** Chasles' theorem: any rigid displacement is a single screw motion.

---

**Q6 — model answer.** T0⁻¹T1 is the relative displacement from pose 0 to pose 1. Its matrix logarithm extracts the constant twist (combined linear+angular generator) that produces that displacement. exp(s·twist) replays a fraction s of that twist — a partial screw. Pre-multiplying by T0 anchors the motion at the start pose. The result glides from T0 (s=0) to T1 (s=1) at constant twist: rotation and translation advance in fixed proportion along one screw axis.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Both reproduce the same endpoint poses and both are smooth. In between they differ: decoupled (straight-line position + SLERP orientation on a shared clock) keeps the position path exactly straight, while the screw's position path generally curves because position is coupled to the rotation. Choose decoupled when the position must follow a literal straight line (e.g. sliding along a slot); choose the screw for the most natural, coordinated full-pose motion when the exact position path is flexible.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** By Chasles' theorem, any rigid displacement between two poses is achieved by exactly one screw — a single axis, a single amount of rotation, and a single pitch (translation per rotation). Screw interpolation replays that one screw at constant twist, so it is the unique, coordinate-free, minimal motion connecting the poses — the rigid-body analog of a straight line, which is the minimal path between two points in flat space.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Assuming the screw keeps position straight (it generally curves).
- Mis-ordering the relative transform (it's T0⁻¹T1) or forgetting the ω→0 limit.
- Treating the twist as dynamics — it's a kinematic interpolation generator (no forces; that's Module 8).
