# Answer Key — Lesson 7.1: The Camera-Frame 3D Point

**Coaches only.** Formative.

1. **P_c is expressed in** — the camera frame.
2. **To make P_c actionable** — apply a rigid transform T(world←cam).
3. **Camera-frame point handed to arm = frame error** — True.
4. **Why better detection won't fix it (short).** The detection and P_c are already correct; the error is the missing T(world←cam), so only applying the transform fixes it.

**Challenge rubric.** Full credit: explains that tweaking the detector can compensate numerically in one pose but breaks elsewhere, and proposes testing by checking whether P_c re-projects correctly (perception fine) while world placement is off (frame fault). Partial: identifies masking without the test.
