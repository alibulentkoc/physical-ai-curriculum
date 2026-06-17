# Module 4 — Completion Report
## Forward Kinematics using Denavit–Hartenberg Parameters

**Status: COMPLETE.** All 8 units (32 lessons) built, wired, and verified. Strict MkDocs build passes (133 pages site-wide). Every notebook executes clean; every SVG validates and renders; every quiz validates; answer keys complete; midpoint and capstone in place.

---

## Central result

Module 4 builds the **forward kinematics map** — from joint angles to the gripper's pose:

$$T_0^n(\boldsymbol\theta) = \prod_{i=1}^{n} T_{i-1}^i,\qquad T_{i-1}^i = \mathrm{Rot}_z(\theta_i)\,\mathrm{Trans}_z(d_i)\,\mathrm{Trans}_x(a_i)\,\mathrm{Rot}_x(\alpha_i),$$

where each factor is generated from a row of four **Denavit–Hartenberg parameters**. The resulting pose, composed with the base mounting, *is* the $T(\text{world}\leftarrow\text{arm})$ that Module 3's perception pipeline took as given — so this module supplies the transform that closes the perceive-to-act loop.

---

## Unit arc

| Unit | Title | What it added |
|---|---|---|
| 1 | Why Kinematics (Joints, Links, and Pose) | FK as $\boldsymbol\theta\to$ pose $T_0^n\in SE(3)$; links and joints; revolute/prismatic; DOF; configuration vs pose (many-to-one). |
| 2 | One Joint at a Time | One-joint planar arm $T_0^1(\theta)$; the joint transform = variable motion ∘ fixed geometry; reading pose from matrix columns. |
| 3 | Chaining Transforms (Two and Three Links) | FK = base→tip product $T_0^2 = T_0^1 T_1^2$; planar closed form = sum of reaches at accumulated angles $\varphi_k$. |
| 4 | The Forward Kinematics Map | General $T_0^n(\boldsymbol\theta) = \prod T_{i-1}^i$; position (translation column) + orientation (rotation block); FK in code (NumPy + SymPy); **midpoint**. |
| 5 | Denavit–Hartenberg Parameters | Why a convention; the four parameters $\theta, d, a, \alpha$; frame-assignment rules ($z$ = joint axis, $x$ = common normal); the table as the robot's kinematic identity. |
| 6 | Building and Using a DH Table | The DH link transform (four-factor product); reading a robot into a table (3-DOF capstone arm); DH FK in code; symbolic DH via SymPy. |
| 7 | Pose, Workspace, and Back to Perception | Reading the end-effector pose (position + approach axis); the reachable workspace (image of FK; planar annulus); $T_0^n = T(\text{world}\leftarrow\text{arm})$ — the perception bridge. |
| 8 | Mini Project: From Joints to the Fruit | Capstone integrating Modules 2–4: build the 3-DOF DH model, run the perceive-to-act pipeline, **verify** the FK (five independent checks), and reflect toward inverse kinematics. |

---

## Deliverables

| Asset | Count | Notes |
|---|---|---|
| Lessons | 32 | 8 units × 4 lessons; every lesson the standard 12-section structure (recaps shorter). |
| Notebooks | 32 | All execute "All checks passed."; NumPy throughout; SymPy for symbolic FK/DH; capstone verification suite. |
| Diagrams (SVG) | 32 | `m04-l1` … `m04-l32`; XML-valid and cairosvg-rendered; DH colour convention (z teal, x red, variable purple). |
| Interactive demos | 4 | `lesson05` one-joint arm; `lesson09` two-link arm; `lesson18` DH-parameter explorer; **`lesson29` flagship capstone "From Joints to the Fruit."** |
| Quizzes | 32 | mc / tf / match / short; formative, unlimited attempts. |
| Answer keys | 32 | Coaches-only; per-question answers + challenge rubrics; in `coaches/answer-keys/module04/`. |
| Assessments | 1 | Midpoint assessment (after Unit 4) + answer key. |

---

## Key insights established

- **A robot is four numbers per joint.** The DH convention reduces each joint's frame-to-frame transform to four parameters; an arm is a small table, and forward kinematics is "fill in each row, multiply."
- **One function, any arm.** `dh_fk(table, config)` computes the gripper pose for a 2-DOF toy, the 3-DOF capstone arm, or a 6-DOF industrial arm — only the data changes.
- **Forward kinematics is verifiable.** Independent checks (known configuration, planar reduction vs the closed form, single-joint revolution, SymPy-vs-numeric, rotation validity) make a silent error very unlikely — the practice that turns a demo into a system.
- **Kinematics meets perception.** $T_0^n$ (with the base mount) is exactly the world-to-arm transform Module 3 assumed; perception's $\mathbf P_{\text{cam}}$ plus calibrated mounts plus FK places a fruit in the arm's frame and yields a move vector.

---

## Bridges

**Backward.** Module 2 (SE(3)) supplies the composition and the elementary $\mathrm{Rot}/\mathrm{Trans}$ factors the DH transform is built from; Module 3 (camera geometry) supplies $\mathbf P_{\text{cam}}$ and *assumed* the $T(\text{world}\leftarrow\text{arm})$ this module now computes. The capstone joins all three.

**Forward.** Module 4 answers *given joint angles, where is the gripper?* — a function to **evaluate**. The reverse question — *given a desired pose, what joint angles achieve it?* — is **inverse kinematics**: solving $T_0^n(\boldsymbol\theta) = T_{\text{desired}}$, which may have zero, one, or many solutions. **Module 5** takes this on, using the forward map built here as its foundation. Velocity kinematics and Jacobians (Module 6), control, and motion planning (Module 7) remain deferred per the curriculum's educational boundary.

---

*Module 4 complete. Next: Module 5 — Inverse Kinematics.*
