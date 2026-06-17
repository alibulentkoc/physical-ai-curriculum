# Answer Key — Lesson 6.1: A Pixel Is a Ray

**Coaches only.** Formative.

1. **Back-projecting a pixel gives** — a ray from the camera center (direction, not a point).
2. **Ray direction** — (x_n, y_n, 1) with x_n=(u−c_x)/f_x, y_n=(v−c_y)/f_y.
3. **All points on the ray share the pixel** — True.
4. **Ray for (480,160), f=800, pp (320,240) (short).** x_n=0.2, y_n=−0.1 → direction (0.2, −0.1, 1).

**Challenge rubric.** Full credit: two fruits on the same ray are indistinguishable from one image because they share the pixel; one depth measurement (RGB-D, stereo, or known geometry) separates them. Partial: identifies ambiguity without the resolving measurement.
