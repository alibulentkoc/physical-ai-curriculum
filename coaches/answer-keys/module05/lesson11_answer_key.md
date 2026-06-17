# Answer Key — Lesson 3.3: Decoupling Position and Orientation (Wrist-Partitioned Arms)

**Coaches only.** Formative.

1. **Decoupling requires** — a spherical wrist (last three axes intersect at a point).
2. **Wrist center** — p_w = p_d − d₆ R_d ẑ (step back along the approach axis).
3. **Position first, then orientation** — True.
4. **Why p_w depends on orientation (short).** The offset is along the gripper's approach axis (3rd column of R_d), so changing orientation moves the wrist center.

**Challenge rubric.** Full credit: without intersecting wrist axes, the wrist joints translate the wrist center as they rotate, so "place the wrist center with the arm, then orient with the wrist" no longer holds — position and orientation re-couple, and there is generally no closed form, forcing numerical methods. Partial: says decoupling fails without explaining the re-coupling.
