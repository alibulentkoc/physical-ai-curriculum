# Answer Key — Lesson 7.3: Closing the Loop with Perception

**Coaches only.** Formative.

1. **T_0^n (with base mount) is** — T(world←arm), the transform Module 3 assumed.
2. **Fruit in the base frame** — P_base = T_base^cam · P_cam.
3. **The perceive-to-act loop is one chain of SE(3) products** — True.
4. **Two things besides P_cam needed to place the fruit in the gripper frame (short).** The calibrated camera mount (T_base^cam) and the current FK pose T_0^n.

**Challenge rubric.** Full credit: for an eye-in-hand camera, P_base = T_0^n · T_gripper^cam · P_cam — the placement now depends on the current configuration through T_0^n, because the camera moves with the gripper, so the same P_cam maps to different base-frame points as the arm moves. Partial: writes the transform without explaining the configuration dependence.
