# Answer Key — Lesson 7.4: From Pixels to the Robot (Unit 7 Recap)

**Coaches only.** Formative consolidation.

1. **Full Module 3 pipeline** — undistort → back-project (+depth) → transform.
2. **Match** — T(arm←cam) → hand-eye calibration; T(world←arm) → robot joints (Module 4); T(world←cam) → composition of the two.
3. **Module 3 assumed T(world←arm); Module 4 computes it** — True.
4. **What Unit 7 adds (short).** It transforms the camera-frame point into the world frame via the Module 2 extrinsics chain T(world←cam).

**Challenge rubric.** N/A (recap). Confirm the learner states the full pipeline and identifies T(world←arm) as the Module 4 hand-off.
