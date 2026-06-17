# Answer Key — Lesson 2.2: The Joint Transform

**Coaches only.** Formative.

1. **A single joint transform is** — one SE(3) element depending on one joint variable.
2. **It splits into** — variable motion ∘ fixed link geometry.
3. **Revolute → rotation, prismatic → translation** — True.
4. **Revolute form (short).** T(i−1→i)(θ) = R_z(θ) · G (variable rotation composed with fixed link geometry).

**Challenge rubric.** Full credit: composing the fixed parts with zero joint variables yields the home pose; it's useful as a calibration/reference configuration to verify the model and zero the encoders. Partial: identifies home pose without the commissioning use.
