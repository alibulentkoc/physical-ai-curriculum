# Answer Key — Lesson 8.2: Building the Perception → World Pipeline

**Coaches only.** Project implementation.

1. **Why tested stages** — so a failure localizes to one stage.
2. **Identity extrinsics give** — P_w = P_c.
3. **Nonzero k1 changes only the undistort stage (then propagates)** — True.
4. **Composition (short).** P_w = transform(T(world←arm)·T(arm←cam), deproject(undistort(u,v), Z)).

**Challenge rubric.** Full credit: refactors transform to operate on an N×3 array using homogeneous coordinates (append ones column, multiply T by the 4×N stack, slice back), keeping points as rows and transposing for the matmul. Partial: correct idea, shape bugs.
