# Answer Key — Lesson 6.3: DH Forward Kinematics in Code

**Coaches only.** Formative.

1. **DH FK in code** — builds each row's transform, multiplies, extracts the pose.
2. **SymPy is used to** — produce a symbolic end-effector pose from a symbolic DH table.
3. **DH FK reproduces the planar 2-link reach for the in-plane joints** — True.
4. **Why store the robot as a DH table (short).** One FK function serves any arm; swapping robots means swapping the table, not the code.

**Challenge rubric.** Full credit: accumulate the running product and store T_0^i after each row, returning all intermediate frames; their translation columns give each joint's position, which is needed to draw the arm and to collision-check along each link (not just the tip). Partial: returns intermediate frames without the drawing/collision use cases.
