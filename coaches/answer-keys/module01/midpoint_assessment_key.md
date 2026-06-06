# Module 1 — Midpoint Assessment · Answer Key & Rubric (instructor only)

**Purpose:** readiness checkpoint for Unit 4. The single most important signal is whether the student can articulate *why the same point has multiple correct coordinates* (B2, B7, C1.3, C2). No matrix content.

## Part A — Physical Quantities & Vectors
- **A1** b) a vector.
- **A2** b) (0.3, 0.3). [0.5−0.2, 0.4−0.1]
- **A3** Magnitude = √(0.3²+0.4²) = **0.5**. One sentence: it tells the robot *how far* (e.g. the size of the move / whether it's within reach), independent of direction.
- **A4** c) facing away from it. (Negative dot = angle > 90°.)
- **A5** True.
- **A6** (i) cross product → a surface normal (which way a surface faces) for grasp/approach, or torque r×F; (ii) distance → reachability check (≤ reach) and choosing the nearest fruit.

## Part B — Coordinate Frames (conceptual)
- **B1** c) the reference frame it's measured in.
- **B2** Accept any clear phrasing of: *the same point has different coordinates in different frames — the object hasn't moved, only the observer/frame changed.* (Signature insight.)
- **B3** c) (0.6, 0.2). [(2.0−1.4, 1.5−1.3)]
- **B4** False. (World coordinates are fixed; only local readings change.)
- **B5** camera → perceive/see it; robot → act/move the arm; world → remember/map it.
- **B6** A 2D map has no z (height); the two share (x,y) but differ in z, so the map can't distinguish them. The robot needs the **3D** coordinate (the height) to reach the correct one.
- **B7** P in B = (2.0−1.0, 1.5−0.5) = **(1.0, 1.0)**. The point hasn't moved because we only re-described it from frame B's origin — changing the *description*, not the physical location.

## Part C — Applied
- **C1.1** Robot frame: (0.30+0.05, −0.10+0.25) = **(0.35, 0.15)**.
- **C1.2** World frame: (0.35+1.65, 0.15+1.35) = **(2.00, 1.50)**.
- **C1.3** All three are correct because each measures the *same physical tomato* from a different origin/orientation (camera lens, robot base, room corner). Different numbers, one point.
- **C2** Unit 3 adds **"who is describing the position?"** — i.e. *in which frame*. It matters because a camera reports in the camera frame, the arm acts in the robot frame, and the map stores the world frame; confusing them makes the arm reach to the wrong place.

## Scoring guidance (readiness, not grading)
- **Ready for Unit 4:** correct on most of Part A and Part B, AND clear conceptual answers on B2, B7, and C1.3 (the "same point, different frames" idea). C1's arithmetic should be correct or only slip on signs.
- **Needs review first:** struggles to explain B2 / C1.3, or treats coordinates as absolute. Revisit 3.1, 3.5, 3.7 (and the 3.5/3.7 demos) before matrices.
- Part A gaps alone (e.g. dot/cross specifics) → quick Unit 2 refresh; not a blocker for Unit 4 as long as frame reasoning is solid.
