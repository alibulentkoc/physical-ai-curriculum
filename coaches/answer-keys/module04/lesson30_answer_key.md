# Answer Key — Lesson 8.2: Building the Arm's DH Model

**Coaches only.** Capstone, formative.

1. **The assembled capstone outputs** — the gripper pose, fruit in base/gripper frames, and a move vector.
2. **Fruit relative to the gripper** — (T_0^n)⁻¹ · P_base.
3. **Build DH factors as fresh arrays to avoid aliasing bugs** — True.
4. **Why a reachability gate before reporting a move (short).** To avoid commanding the arm toward a fruit outside its workspace, which it physically can't reach.

**Challenge rubric.** Full credit: gate computes the fruit's distance from the base axis (and height) against the annulus bounds [|L1−L2|, L1+L2] and returns a clear "unreachable" flag when outside; gating before motion prevents wasted or unsafe moves toward unreachable targets and lets the planner reposition the base or skip the fruit. Partial: implements the gate without articulating why pre-motion gating matters.
