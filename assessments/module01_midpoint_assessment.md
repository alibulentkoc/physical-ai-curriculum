---
title: Module 1 — Midpoint Assessment (Readiness Checkpoint)
position: Between Unit 3 and Unit 4
covers: [Unit 1 physical quantities, Unit 2 vectors, Unit 3 coordinate frames]
excludes: [matrix mathematics]
purpose: Verify readiness for matrix-based transformations (Unit 4).
time_estimate: 45-60 minutes
---

# Module 1 — Midpoint Assessment

**A readiness checkpoint, not a final exam.** This assessment confirms you can reason about physical quantities, vectors, coordinate systems, and reference frames *before* matrices are introduced in Unit 4. **No matrix mathematics appears here.** Answers and rubric are in the coaches' key (`coaches/answer-keys/module01/midpoint_assessment_key.md`); the student version is below.

- **Format:** mixed (multiple choice, true/false, short answer, one applied problem).
- **Tools:** a calculator is fine; the coding parts can be checked with NumPy but hand-work is acceptable.
- **Passing intent:** a student ready for Unit 4 should answer most items correctly and, crucially, articulate *why the same point can have several correct coordinates.*

---

## Part A — Physical Quantities & Vectors (Units 1–2)

**A1 (MC).** A quantity that needs both a size and a direction is best represented as:
a) a scalar  b) a vector  c) a unit only  d) a single signed number

**A2 (MC).** The gripper is at (0.2, 0.1) and a tomato is at (0.5, 0.4) (same frame). The move the arm must make (displacement) is:
a) (0.7, 0.5)  b) (0.3, 0.3)  c) (−0.3, −0.3)  d) (0.25, 0.25)

**A3 (Short).** A vector has components (0.3, 0.4). Give its magnitude and explain in one sentence what the magnitude tells the robot.

**A4 (MC).** The dot product of a gripper's facing direction with the direction to a tomato is **negative**. This means the gripper is:
a) facing the tomato  b) perpendicular to it  c) facing away from it  d) touching it

**A5 (T/F).** A unit vector carries direction only; its length is 1. ____

**A6 (Short).** Give one robotics use each for (i) the cross product and (ii) the distance between two points.

## Part B — Coordinate Frames (Unit 3, conceptual)

**B1 (MC).** A coordinate like (0.3, 0.4) is meaningful only when you also know:
a) the time of day  b) the object's mass  c) the reference frame it's measured in  d) the battery level

**B2 (Short).** State the signature idea of Unit 3 in your own words (one sentence).

**B3 (MC).** World says a tomato is at (2.0, 1.5). The robot sits at (1.4, 1.3) with axes aligned to the world. The tomato's **robot-frame** coordinates are:
a) (2.0, 1.5)  b) (3.4, 2.8)  c) (0.6, 0.2)  d) (1.4, 1.3)

**B4 (T/F).** When the robot drives forward, the tomato's **world-frame** coordinates change. ____

**B5 (Match).** Match each frame to its usual role in a pick:
- camera frame → ____
- robot frame → ____
- world frame → ____
(options: *act / move the arm* · *remember / map it* · *perceive / see it*)

**B6 (Short).** Two tomatoes share the same (x, y) on the 2D map but one is higher than the other. Why can a 2D map not tell them apart, and what does the robot need?

**B7 (Short, conceptual transform — no matrices).** Frame B is offset from frame A by (1.0, 0.5) with no rotation. A point is at (2.0, 1.5) in A. Give its coordinates in B, and state in one sentence why the point itself has not moved.

## Part C — Applied (integrates Units 1–3)

**C1 (Applied).** A camera detects a tomato at (0.30, −0.10) in the **camera** frame. The camera is mounted 0.05 m ahead and 0.25 m above the robot's base (axes aligned). The robot base is at world (1.65, 1.35), axes aligned with the world.
1. Give the tomato's **robot-frame** coordinates.
2. Give the tomato's **world-frame** coordinates.
3. In one or two sentences, explain why all three descriptions (camera, robot, world) are correct for the same tomato.

**C2 (Short, readiness reflection).** In your own words: Unit 2 answered "how do we describe position?" What question does Unit 3 add, and why does it matter for a robot using a camera and an arm?

---

*When you can answer B2, B7, and C1 confidently, you're ready for Unit 4 — where the offset-and-rotation you just reasoned about becomes a single matrix.*
