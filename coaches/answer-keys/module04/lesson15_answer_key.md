# Answer Key — Lesson 4.3: Forward Kinematics in Code

**Coaches only.** Formative.

1. **Clean FK implementation** — builds each joint factor, multiplies in order, extracts pose.
2. **SymPy is used to** — produce a symbolic formula for the gripper pose.
3. **Verify numeric FK against a trusted closed form** — True.
4. **Why fresh arrays (short).** To avoid in-place aliasing bugs, where mutating a shared array corrupts other factors.

**Challenge rubric.** Full credit: extends `fk` to return every intermediate frame T_0^i (accumulate and store the running product at each step); intermediate frames are needed to draw the arm and to collision-check along each link, not just at the tip. Partial: returns intermediate frames without the use cases.
