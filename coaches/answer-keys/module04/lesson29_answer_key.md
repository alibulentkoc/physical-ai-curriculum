# Answer Key — Lesson 8.1: The Project (From Joints to the Fruit)

**Coaches only.** Capstone, formative.

1. **The capstone integrates** — Modules 2–4 (transforms, perception, forward kinematics).
2. **What the capstone does NOT do** — solve for the joint angles to reach the fruit (that's IK, Module 5).
3. **The capstone arm is the 3-DOF DH model (base swivel + two planar links)** — True.
4. **Four pipeline blocks in order (short).** Perceive (P_cam) → bridge frames (P_base) → forward kinematics (T_0^3) → report target relative to gripper.

**Challenge rubric.** Full credit: extend by adding (a) a reachability check (fruit distance vs the workspace annulus, Lesson 7.2) and (b) an orientation/approach check (Lesson 7.1) before declaring "graspable"; a real system also needs collision checks, joint-limit checks, and a ripeness/quality gate. Partial: adds reachability or orientation but not the broader real-system checks.
