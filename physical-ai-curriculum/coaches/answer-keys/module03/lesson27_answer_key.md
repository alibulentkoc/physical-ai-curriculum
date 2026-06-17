# Answer Key — Lesson 7.3: Estimating the Fruit's World Position

**Coaches only.** Formative.

1. **Full order** — undistort → back-project (+depth) → transform.
2. **NOT a valid sanity check** — that the detector's confidence is high.
3. **Distance preserved across frames** — True.
4. **One-line formula (short).** P̃_w = T(world←cam) · [ Z · K⁻¹ · undistort(u,v) ] (homogenized).

**Challenge rubric.** Full credit: a 5 cm z-error with perfect re-projection points to extrinsics (the translation/pose), not perception — because perfect re-projection means the camera-frame geometry is right, so the error entered in the camera→world transform. Partial: names extrinsics without the re-projection reasoning.
