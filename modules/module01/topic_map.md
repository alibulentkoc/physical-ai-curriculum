# Module 1 — Topic Map (Lesson Granularity)

> **Source:** manifest §7, unit structure D-008, and topic breakdown **D-014 (APPROVED, option B)**.
> **Granularity:** RESOLVED — **option B**, sub-topic level. Each sub-topic below becomes one lesson following the 12-part template.
> **Total Module 1 lessons:** **66** (within the architect's 60–70 estimate).

## 1. Unit sequence and focus

| # | Unit | Focus | Lessons |
|---|---|---|---|
| 1 | Physical Quantities and Measurements | Scalars vs. vectors; units, dimensions; precision, accuracy, uncertainty. | 6 |
| 2 | Vectors and Geometric Thinking | Vectors as objects; operations; dot & cross products; distance. | 9 |
| 3 | Coordinate Systems and Reference Frames | Cartesian/2D/3D; local vs. global; conceptual transforms; robot/camera frames. | 7 |
| 4 | Matrices as Transformations | Matrices as operators; rotation/scale/reflection; composition. | 8 |
| 5 | Linear Algebra for Robotic Systems | Linear systems; inverse; rank; eigen-structure; least-squares intuition. | 7 |
| 6 | Trigonometry for Motion and Perception | Angles/radians; sin/cos/tan; unit circle; triangle laws. | 9 |
| 7 | Modeling Physical Systems | Models; I/O; state; dynamics; feedback; constraints; validation. | 7 |
| 8 | Computational Mathematics with Python | NumPy arrays/ops; Matplotlib; numerical experiments; reproducibility. | 7 |
| 9 | Mini Project — Greenhouse Robot Workspace | Integrative application of U1–U8. | 6 |

## 2. Authoritative lesson list (D-014)

Each entry is one lesson. Lesson files will be named `lessonNN_slug.md` in `lessons/`, numbered globally 01–66 in this order.

### Unit 1 — Physical Quantities and Measurements
- 1.1 Physical AI and the Physical World
- 1.2 Units and Dimensions
- 1.3 Scalars and Physical Quantities
- 1.4 Measurement Error
- 1.5 Accuracy and Precision
- 1.6 Engineering Estimation

### Unit 2 — Vectors and Geometric Thinking
- 2.1 What Is a Vector?
- 2.2 Vector Representation
- 2.3 Vector Addition
- 2.4 Vector Subtraction
- 2.5 Magnitude and Direction
- 2.6 Unit Vectors
- 2.7 Dot Product
- 2.8 Cross Product
- 2.9 Distance Between Points

### Unit 3 — Coordinate Systems and Reference Frames
- 3.1 Why Coordinate Frames Matter
- 3.2 Cartesian Coordinates
- 3.3 2D Coordinate Systems
- 3.4 3D Coordinate Systems
- 3.5 Local and Global Frames
- 3.6 Conceptual Frame Transformations
- 3.7 Robot and Camera Frames

### Unit 4 — Matrices as Transformations
- 4.1 Matrices as Operators
- 4.2 Matrix Addition
- 4.3 Matrix Multiplication
- 4.4 Identity Matrix
- 4.5 Rotation Matrices
- 4.6 Scaling Transformations
- 4.7 Reflection Transformations
- 4.8 Composition of Transformations

### Unit 5 — Linear Algebra for Robotic Systems
- 5.1 Linear Systems
- 5.2 Matrix Inverse
- 5.3 Rank and Independence
- 5.4 Eigenvectors
- 5.5 Eigenvalues
- 5.6 Least Squares Intuition
- 5.7 Why Linear Algebra Powers Robotics

### Unit 6 — Trigonometry for Motion and Perception
- 6.1 Angles and Angular Measurement
- 6.2 Radians
- 6.3 Sine and Cosine
- 6.4 Tangent
- 6.5 Unit Circle
- 6.6 Triangle Geometry
- 6.7 Law of Sines
- 6.8 Law of Cosines
- 6.9 Trigonometry in Robotics

### Unit 7 — Modeling Physical Systems
- 7.1 What Is a Model?
- 7.2 Inputs and Outputs
- 7.3 State Variables
- 7.4 Dynamic Systems
- 7.5 Feedback Concepts
- 7.6 Physical Constraints
- 7.7 Model Validation

### Unit 8 — Computational Mathematics with Python
- 8.1 Scientific Python Ecosystem
- 8.2 NumPy Arrays
- 8.3 Vector Operations in NumPy
- 8.4 Matrix Operations in NumPy
- 8.5 Visualization with Matplotlib
- 8.6 Numerical Experiments
- 8.7 Reproducing Mathematical Results

### Unit 9 — Mini Project (Greenhouse Robot Workspace)
- 9.1 Greenhouse Environment Model
- 9.2 Coordinate Frame Definition
- 9.3 Fruit Position Representation
- 9.4 Workspace Visualization
- 9.5 Reachability Analysis
- 9.6 Project Report

## 3. Dependency order

Strictly downward; each unit assumes those above it:

```
U1 → U2 → U3 → U4 → U5
                 ├→ U6
                 └→ U7 → U8 → U9 (integrates U1–U8)
```

Cross-module: U2–U6 + U8 are the load-bearing prerequisites for Module 2 (SE(3)); see manifest §17.

## 4. Lesson template

Every one of the 66 lessons follows the standard 12-part template (D-005): Why This Matters · Physical Intuition · Mathematical Foundations · Visual Explanation · Engineering Example · Worked Example · Interactive Demonstration · Coding Exercise · Knowledge Check · Challenge Problem · Common Mistakes · Key Takeaways.
