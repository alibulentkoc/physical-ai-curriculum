---
module: 6
unit: 8
lesson: 32
type: answer_key
title: "Answer Key — The Velocity Layer"
audience: coaches
---
# Answer Key 8.4
**Q1 B · Q2 B · Q3 B · Q4 C · Q5 B.**
**Q6.** A single function taking the current configuration and a desired tool twist, returning a robust (scheduled-damping) joint-rate vector plus conditioning info — desired tool twists in, robust joint rates out.
**Q7.** Trajectory timing → Module 7; feedback/pose-error correction → Module 8; posture/null-space control → Module 6 velocity layer (with goals possibly set by M7).
**Q8.** It packages all of Module 6 (differential kinematics, manipulability, singularity handling, damped inverse) behind one interface — the velocity stream Module 7's trajectory generators will drive, keeping planning and control cleanly in M7/M8.
### Watch for: Q4 is Module 8 (feedback), not Module 6; the velocity layer is open-loop.
