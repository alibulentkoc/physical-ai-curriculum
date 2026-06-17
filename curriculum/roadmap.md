# Curriculum Roadmap

> **Scope:** The full 10-module program and how the modules connect.
> **Authority:** Module roadmap **D-004**; narrative **D-001**.
> **Purpose:** Show the whole arc — what each module teaches, what it contributes to the Greenhouse Harvesting Robot, and how modules depend on one another — so contributors can see where any piece fits.

---

## 1. The arc in one line

From **"what mathematics does a robot need?"** (Module 1) to **"build and validate a digital twin of the robot"** (Module 10) — every module adds one capability to the same Greenhouse Harvesting Robot, assembling a complete perception-to-action pipeline.

## 2. The modules

| #  | Module | Core question it answers | Contribution to the robot |
|----|--------|--------------------------|---------------------------|
| 01 | Mathematical Foundations | What math does a robot need before it can perceive and act? | Vectors, frames, matrices, trig, Python — the substrate |
| 02 | Spatial Transformations and SE(3) | How do we rigorously relate one frame to another in 3D? | Express the fruit's position in any frame |
| 03 | Camera Geometry and Robotic Perception | How does a camera turn the world into pixels, and back? | Perceive fruit and estimate its position |
| 04 | Forward Kinematics (DH parameters) | Given joint angles, where is the end-effector? | Know where the gripper is for any pose |
| 05 | Inverse Kinematics | Given a target pose, what joint angles reach it? | Compute how to reach a specific fruit |
| 06 | Jacobians and Differential Motion | How do joint velocities map to end-effector motion? | Control velocity; detect singularities |
| 07 | Trajectory Generation and Motion Planning | How do we move smoothly and safely to the target? | Plan a collision-free path to the fruit |
| 08 | Robot Communication, Embedded Systems, and Control | How do commands reach motors and get executed? | Send commands; actuate the motors |
| 09 | Physical AI System Integration | How do all the pieces become one working loop? | The full perceive→plan→act pipeline |
| 10 | Digital Twin Capstone | How do we build a faithful virtual replica to test and validate? | A digital twin of the harvesting robot |

## 3. Dependency chain

Each module is a prerequisite for the next; the chain is mostly linear, with perception and kinematics converging at integration.

```
M1 Mathematical Foundations
      ↓
M2 Spatial Transformations / SE(3)
      ↓
M3 Camera Geometry & Perception ─┐
      ↓                          │
M4 Forward Kinematics            │
      ↓                          │
M5 Inverse Kinematics            │
      ↓                          │
M6 Jacobians & Differential Motion
      ↓                          │
M7 Trajectory Generation & Planning
      ↓                          │
M8 Communication, Embedded, Control
      ↓                          │
M9 System Integration  ←─────────┘  (perception + kinematics + control converge)
      ↓
M10 Digital Twin Capstone
```

## 4. How a single fruit travels through the curriculum

A useful way to read the roadmap is to follow one tomato:

- **M3** the camera sees it and estimates its position (in the camera frame).
- **M2** that position is transformed into the robot's base frame.
- **M5** inverse kinematics computes the joint angles that place the gripper there.
- **M4/M6** forward kinematics and the Jacobian confirm the pose and control the approach.
- **M7** a smooth, safe trajectory to the fruit is planned.
- **M8** the trajectory becomes motor commands that actuate the arm.
- **M9** all of this runs as one closed loop.
- **M10** the entire journey is replicated and validated in a digital twin.
- **M1** underlies every step above — none of it is possible without the foundations.

## 5. Software progression

The toolchain grows module by module; nothing heavy is introduced before it is needed (D-009 governs Module 1).

| Tool | Enters at |
|---|---|
| Python, NumPy, Matplotlib, SymPy, Jupyter | Module 1 |
| OpenCV | Module 3 |
| ROS 2 | Module 8 |
| Gazebo / Isaac Sim | Modules 9–10 |

Each module that adds tooling will ship its own environment spec, mirroring `software_environment.md`.

## 6. Common structure across modules

Every module shares the same scaffolding so learners and contributors always know where things are:

- A **manifest** in `curriculum/` defines the module (the contract).
- A folder in `modules/moduleNN/` holds `README.md`, `learning_objectives.md`, `topic_map.md`, `assessments.md`, and `lessons/`, `notebooks/`, `assets/`.
- Every topic follows the **12-part template** (D-005).
- Progression is **competency-based** (D-015).

## 7. Status

| Module | Manifest | Scaffolding | Lessons |
|---|---|---|---|
| 01 | ✅ | ✅ | pending (66 lessons planned, D-014) |
| 02–10 | ⬜ | ⬜ | ⬜ |

Module 1 is the only module designed so far. Modules 2–10 each begin with their own manifest before any scaffolding or lessons.
