# Module 1 Manifest
## Mathematical Foundations for Physical AI, Robotics, and Digital Twins

> **Document type:** Module specification (manifest).
> **Status:** Draft for architect review.
> **Purpose:** This manifest is the authoritative contract for Module 1. ChatGPT, Claude, Gemini, and human contributors all generate lessons, notebooks, diagrams, quizzes, and demos *against this document*. It defines scope, sequence, outcomes, and dependencies — it does **not** contain lesson content.

---

## 1. Module Overview

Module 1 establishes the mathematical and computational substrate that every later module depends on. It answers a single guiding question:

> **What mathematics does a robot need before it can perceive and act in the physical world?**

The module deliberately resists being a generic "math review." Each mathematical idea is introduced because a robot needs it — to represent a fruit's position, to relate a camera's view to a gripper's reach, to describe how a joint angle changes a tool's location. The Greenhouse Harvesting Robot is the throughline that gives every concept a physical reason to exist.

By the end, students possess the vocabulary and tools — vectors, frames, matrices as transformations, trigonometry of motion, and Python-based computation — required to begin Module 2 (Spatial Transformations and SE(3)) without remediation.

---

## 2. Module Vision

Module 1 turns abstract mathematics into the *language of a physical system*. Students should leave able to look at a robot reaching for a tomato and see the underlying structure: points in space, frames attached to bodies, transformations that relate one frame to another, and the linear-algebraic machinery that makes those transformations computable.

The module is built on the curriculum's five-layer philosophy — **physical intuition → visual understanding → mathematical formulation → computational implementation → system integration** — so that no equation is introduced before the student can picture what it does and why it matters.

---

## 3. Learning Outcomes

On successful completion of Module 1, a student can:

- **LO1.** Represent physical quantities (position, displacement, velocity, force) as vectors and reason about units, dimensions, and measurement uncertainty.
- **LO2.** Distinguish points, vectors, and frames, and explain why a position is only meaningful relative to a reference frame.
- **LO3.** Define and switch between coordinate systems (Cartesian, polar/cylindrical) and articulate where each is natural in a robotic context.
- **LO4.** Interpret a matrix as a geometric transformation (rotation, scaling, shear, projection) rather than only as a grid of numbers.
- **LO5.** Apply core linear-algebra operations — matrix–vector products, composition, inverse, transpose, dot/cross products — to robotic problems.
- **LO6.** Use trigonometry to relate angles, lengths, and positions in 2D/3D motion and simple perception geometry.
- **LO7.** Build simple mathematical models of physical systems and reason about their assumptions and limits.
- **LO8.** Implement and visualize the above using Python (NumPy, Matplotlib), producing reproducible notebooks.
- **LO9.** Integrate these skills to model the workspace of the Greenhouse Harvesting Robot in the mini project.

---

## 4. Relationship to the Greenhouse Harvesting Robot

Every unit connects to the robot's eventual job: locate a fruit and move a gripper to it.

| Concept in Module 1 | Role in the harvesting robot |
|---|---|
| Vectors & measurements | Representing a fruit's position and the gripper's location |
| Reference frames | Relating the camera's view, the robot base, and the world |
| Matrices as transformations | Converting a point seen by the camera into the robot's frame |
| Linear algebra | The computational engine behind every later transformation |
| Trigonometry | Relating joint angles to reach; angles in the camera's field of view |
| Modeling | Describing the reachable workspace and its constraints |
| Python computation | The tool used to compute, simulate, and visualize all of the above |

The **mini project** (Unit 9) makes this explicit: students model the robot's workspace as a geometric region in space, using only Module 1 mathematics.

---

## 5. Prerequisites

**Assumed incoming knowledge:**
- High-school algebra and basic trigonometry (sine, cosine, right triangles).
- Comfort with functions and graphs.
- Basic programming exposure is helpful but not required; Python is taught at the level needed.

**Explicitly NOT assumed:**
- Prior linear algebra.
- Prior robotics, ROS, or simulation experience.
- Calculus beyond intuitive notions (formal calculus is reinforced where used, not gatekept).

A companion document, `curriculum/mathematical_prerequisites.md`, will enumerate the precise entry competencies and provide a self-check diagnostic.

---

## 6. Topic Map

```
Module 1 — Mathematical Foundations
│
├── Unit 1  Physical Quantities and Measurements
├── Unit 2  Vectors and Geometric Thinking
├── Unit 3  Coordinate Systems and Reference Frames
├── Unit 4  Matrices as Transformations
├── Unit 5  Linear Algebra for Robotic Systems
├── Unit 6  Trigonometry for Motion and Perception
├── Unit 7  Modeling Physical Systems
├── Unit 8  Computational Mathematics with Python
└── Unit 9  Mini Project — Greenhouse Robot Workspace
```

Dependency direction is strictly downward: each unit assumes the ones above it. Units 1–3 build representation; Units 4–5 build the transformation machinery; Units 6–7 connect to motion and modeling; Unit 8 makes it computational; Unit 9 integrates everything.

---

## 7. Unit Breakdown

Each unit below lists its **focus**, the **competencies** it delivers, and its **link to the robot**. Topics within units will follow the standard 12-part template at lesson-generation time (Phase 4); none of that content is specified here.

### Unit 1 — Physical Quantities and Measurements
- **Focus:** Scalars vs. vectors; units, dimensions, and dimensional reasoning; precision, accuracy, and measurement uncertainty.
- **Competencies:** Express physical quantities with correct units; reason about error and significant figures; recognize when a quantity needs direction.
- **Robot link:** Every measurement the robot makes — distance to a fruit, gripper width — carries units and uncertainty.

### Unit 2 — Vectors and Geometric Thinking
- **Focus:** Vectors as geometric objects; addition, scaling, dot and cross products; magnitude and direction; vectors vs. points.
- **Competencies:** Manipulate vectors algebraically and geometrically; interpret dot product (projection/angle) and cross product (area/normal).
- **Robot link:** A fruit's position relative to the gripper is a vector; the dot product underlies "how aligned is the gripper with the target."

### Unit 3 — Coordinate Systems and Reference Frames
- **Focus:** Cartesian, polar, cylindrical coordinates; the concept of a frame; expressing the same point in different frames.
- **Competencies:** Convert between coordinate systems; explain why position is frame-relative; set up a world frame, base frame, and camera frame conceptually.
- **Robot link:** The camera sees the fruit in its own frame; the robot must express that position in its base frame. This unit plants the seed for SE(3).

### Unit 4 — Matrices as Transformations
- **Focus:** Matrices as operators on vectors; rotation, scaling, shear, reflection, projection; composition as matrix multiplication; the identity and inverse.
- **Competencies:** Read a matrix as a geometric action; compose and invert transformations; predict the effect of a matrix on a shape.
- **Robot link:** Rotating and translating a point from camera frame to robot frame is matrix multiplication — the direct precursor to homogeneous transforms in Module 2.

### Unit 5 — Linear Algebra for Robotic Systems
- **Focus:** Systems of linear equations; matrix inverse and rank; linear independence and span; eigen-intuition (qualitative); least-squares intuition for noisy data.
- **Competencies:** Solve and reason about linear systems; recognize singular/ill-conditioned cases; understand why redundancy and noise call for least-squares.
- **Robot link:** Solving for unknown positions/angles, and coping with noisy perception, are linear-algebra problems that recur in kinematics and calibration.

### Unit 6 — Trigonometry for Motion and Perception
- **Focus:** Angles and radians; sine/cosine in rotation; law of sines/cosines; angles in projection geometry; small-angle intuition.
- **Competencies:** Relate angles to positions and lengths; build 2D rotation by hand; reason about a camera's angular field of view.
- **Robot link:** Joint angles determine reach; the camera's field of view is angular. Trigonometry is the bridge from "angle" to "position."

### Unit 7 — Modeling Physical Systems
- **Focus:** What a mathematical model is; assumptions, idealizations, and limits; static vs. dynamic description; degrees of freedom (intuitive).
- **Competencies:** Build a simple model of a physical situation; state assumptions explicitly; judge when a model breaks down.
- **Robot link:** The harvesting arm's reachable region is a *model*; students learn to build and critique such models before formal kinematics.

### Unit 8 — Computational Mathematics with Python
- **Focus:** Python for numerical work; NumPy arrays and vectorized operations; representing vectors/matrices in code; plotting with Matplotlib; reproducible notebooks.
- **Competencies:** Implement Unit 1–7 mathematics in Python; visualize vectors, frames, and transformations; produce clean, runnable notebooks.
- **Robot link:** Every later module computes in Python; this unit establishes the toolchain and conventions used throughout the curriculum.

### Unit 9 — Mini Project: Modeling the Greenhouse Harvesting Robot Workspace
- **Focus:** Integrative project applying Units 1–8.
- **Deliverable:** A Python notebook that defines a world frame and a robot base frame, places fruit positions as vectors, models a simplified reachable workspace, transforms fruit positions into the robot frame, and visualizes which fruits are reachable.
- **Robot link:** This is the first end-to-end taste of perception-to-action geometry, using only Module 1 mathematics, and it directly sets up SE(3) in Module 2.

---

## 8. Software Stack

Module 1 keeps the stack intentionally minimal — math and visualization only. Heavier robotics tooling is introduced in later modules and is listed here only as forward context.

**Used in Module 1:**
- Python 3.x
- NumPy (vectors, matrices, linear algebra)
- Matplotlib (2D/3D visualization)
- Jupyter (notebooks)
- *(Optional)* SymPy for symbolic checks

**Introduced later (not required here):**
- OpenCV → Module 3 (perception)
- ROS 2 → Module 8 (communication/control)
- Gazebo / Isaac Sim → Modules 9–10 (integration, digital twin)

Exact versions and a reproducible environment specification will live in `curriculum/software_environment.md`.

---

## 9. Mathematical Competencies

A checklist version of the learning outcomes, suitable for mastery tracking:

- [ ] Classify and dimensionally check physical quantities
- [ ] Perform vector algebra; interpret dot and cross products geometrically
- [ ] Convert among Cartesian, polar, and cylindrical coordinates
- [ ] Express a point in multiple reference frames
- [ ] Interpret and compose matrix transformations; compute inverses
- [ ] Solve linear systems and recognize singular/ill-conditioned cases
- [ ] Apply trigonometry to rotation and projection geometry
- [ ] Build and critique a simple mathematical model
- [ ] Implement all of the above in NumPy and visualize with Matplotlib

---

## 10. Engineering Competencies

Beyond the mathematics, Module 1 develops engineering habits:

- Stating assumptions explicitly and identifying when a model is valid.
- Reasoning about units, error, and uncertainty in real measurements.
- Choosing an appropriate coordinate system / frame for a problem.
- Translating a physical situation into a computable representation.
- Producing reproducible, well-documented computational work.

---

## 11. Assessments

Assessment follows the curriculum-wide strategy (to be detailed in `curriculum/assessment_strategy.md`). For Module 1:

- **Per-topic Knowledge Checks** — short formative questions embedded in each lesson (template section 9).
- **Per-topic Challenge Problems** — stretch problems for deeper mastery (template section 10).
- **Unit checkpoints** — a short assessment at the end of each unit confirming the unit's competencies.
- **Mini-project rubric** — summative assessment of Unit 9 (correctness, clarity of assumptions, code reproducibility, visualization quality).

Answer keys and rubrics are authored separately under `coaches/` and are never placed in learner-facing folders.

---

## 12. Demonstrations

Interactive demonstrations to be produced (storyboards by Gemini, implementations by Claude Code):

- Vector addition and dot/cross product visualizer.
- Coordinate-system converter (Cartesian ↔ polar/cylindrical) with live plot.
- "Same point, different frame" demo showing one fruit expressed in camera vs. base frame.
- Matrix-as-transformation playground (apply rotation/scale/shear to a shape and a point cloud).
- 2D rotation-by-angle demo linking trigonometry to matrix form.

---

## 13. Coding Activities

Each unit includes at least one coding exercise (template section 8). Indicative set:

- Implement vector operations from scratch, then verify against NumPy.
- Write a coordinate-conversion function library.
- Build and apply 2D/3D transformation matrices to point sets.
- Solve a small linear system and detect a singular case.
- Plot a camera field-of-view cone and test whether a point falls inside it.

All activities are delivered as runnable Jupyter notebooks following the conventions in `CONTRIBUTING.md`.

---

## 14. Mini Project

**Title:** Modeling the Greenhouse Harvesting Robot Workspace.

**Goal:** Integrate Units 1–8 into a single notebook that models where the robot can and cannot reach, and which fruits are reachable.

**Required elements:**
1. Define a world frame and a robot base frame.
2. Represent several fruit positions as vectors in the world frame.
3. Model a simplified reachable workspace (e.g., a bounded region) using Module 1 mathematics.
4. Transform fruit positions into the robot base frame.
5. Determine and visualize which fruits are reachable.
6. Document assumptions and limitations explicitly.

**Why it matters:** This is the curriculum's first integrated perception-to-action geometry exercise and the concrete bridge into SE(3).

---

## 15. Deliverables

Produced during later phases, against this manifest:

- `modules/module01/README.md` — module overview and objectives
- `modules/module01/learning_objectives.md`
- `modules/module01/topic_map.md`
- `modules/module01/assessments.md`
- `modules/module01/lessons/` — one lesson per topic (Phase 4)
- `modules/module01/notebooks/` — coding activities and demos
- Mini-project notebook and rubric (rubric under `coaches/`)
- Supporting diagrams and storyboards under `assets/`

---

## 16. Exit Criteria

A student exits Module 1 ready for Module 2 when they can:

- Represent a point/position as a vector in a chosen frame and convert it to another frame.
- Read and compose matrix transformations and compute an inverse.
- Use trigonometry to relate angles to positions.
- Implement and visualize all of the above in Python.
- Complete the Unit 9 mini project with explicit, defensible assumptions.

Meeting the exit criteria means the student needs **no mathematical remediation** to begin SE(3).

---

## 17. Dependencies for Module 2

Module 2 (Spatial Transformations and SE(3)) consumes Module 1 directly. The dependency chain:

```
Module 1  Mathematical Foundations
      ↓   (vectors, frames, matrices, rotations, trigonometry)
Module 2  Spatial Transformations and SE(3)
      ↓
Module 3  Camera Geometry and Perception
      ↓
Module 4  Forward Kinematics (DH parameters)
      ↓
Module 5  Inverse Kinematics
      ↓   ...
```

**What Module 2 requires that Module 1 must deliver:**

| Module 2 needs | Provided by Module 1 |
|---|---|
| Vectors and points | Units 2–3 |
| Reference frames and frame-relative position | Unit 3 |
| Matrices as transformations; composition; inverse | Units 4–5 |
| Rotation via trigonometry | Unit 6 |
| Python representation and visualization of frames | Unit 8 |
| Workspace/modeling intuition | Units 7, 9 |

If any of these is weak at exit, Module 2 will stall — which is precisely why Module 1 is sequenced as above rather than as a loose topic list.

---

*End of Module 1 manifest. No lesson content is included by design; lessons are generated in a later phase against this specification.*
