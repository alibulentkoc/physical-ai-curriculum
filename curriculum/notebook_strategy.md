---
title: Notebook Strategy
authority: D-019 (per-unit notebook timing); software stack D-009
status: standard — complete before large-scale notebook generation
---

# Notebook Strategy

> Defines the **notebook track**: the runnable counterpart to each lesson. Lessons teach and motivate; notebooks make the computation real. This document is the contract for how notebooks are built, named, and assessed, so every contributor produces consistent, reproducible material.

---

## 1. Purpose

In Units 1–7, lesson sections 7 (Interactive Demonstration) and 8 (Coding Exercise) are deliberately conceptual; their **runnable versions live here in the notebook track**. Notebooks exist to:

- turn each lesson's demonstration and coding exercise into executable, reproducible code;
- carry the curriculum's heaviest assessment weight — **Coding Exercises = 40%** (D-010) — as graded artifacts;
- give students hands-on computational practice aligned exactly with the lesson they just read;
- host the working visualizations that complement Gemini's static/animated assets.

## 2. Production pipeline (D-019)

Notebooks are generated **per unit, immediately after the unit's lessons are approved**:

```
Unit Lessons → Architect Review → Unit Approved → Generate Unit Notebooks → Next Unit
```

This prevents a notebook backlog, keeps lessons and code synchronized, and allows early testing of the computational activities.

## 3. Notebook standards

- **Format:** Jupyter (`.ipynb`), runnable in JupyterLab.
- **Reproducibility:** every notebook must pass **Restart & Run All** with no manual steps and no hidden state.
- **Determinism:** any randomness uses a fixed seed (`rng = np.random.default_rng(0)`).
- **Self-contained:** imports at top; no reliance on prior-notebook state.
- **Stack (D-009):** Python 3.12+, NumPy, Matplotlib, SymPy, Jupyter. No OpenCV/ROS 2/Gazebo in Module 1.
- **Structure mirrors the lesson:** a short intro cell, a "Demonstration" section (lesson §7), a "Coding Exercise" section (lesson §8) with a clearly marked `# YOUR CODE HERE` cell, and a "Check your work" section.
- **Narrative:** keep the Greenhouse Harvesting Robot framing in examples.
- **Comments explain the *why*,** not just the *what*.

## 4. Naming and location

- One notebook per lesson that has computational content: `modules/moduleNN/notebooks/lessonNN_slug.ipynb`, matching the lesson's filename slug.
- Unit 9 (mini project) gets a dedicated project notebook.
- A per-unit `00_unit_overview.ipynb` is optional for integrative practice.

## 5. Lesson-to-notebook mapping

| Lesson | Notebook | Computational focus |
|---|---|---|
| 1.2 Units & Dimensions | `lesson02_units_and_dimensions.ipynb` | unit conversions, dimension checks |
| 1.4 Measurement Error | `lesson04_measurement_error.ipynb` | absolute/relative error, averaging noise |
| 1.5 Accuracy & Precision | `lesson05_accuracy_and_precision.ipynb` | bias vs spread on sample data |
| 2.x Vectors | `lessonNN_*.ipynb` | vector ops, plotting, dot/cross products |
| 8.x Python | `lessonNN_*.ipynb` | full NumPy/Matplotlib workflows |
| 9.x Mini Project | `module01_mini_project.ipynb` | integrative workspace model |

Lessons whose §7/§8 are purely conceptual (e.g. 1.1, 1.3) may have a light or optional notebook; the mapping is finalized per unit at notebook-generation time.

## 6. Visualization conventions

- **Matplotlib** for in-notebook plots; always label axes with quantity **and unit**.
- Use a consistent, colorblind-safe palette; avoid relying on color alone to convey meaning.
- Vector plots use arrows (`quiver`/`annotate`) with a fixed, equal aspect ratio so geometry isn't distorted.
- Notebook plots are the *interactive/working* visuals; Gemini's storyboard-driven assets are the *polished/illustrative* visuals in `assets/`. The two should agree visually (same conventions, labels, framing).

## 7. Assessment integration

- Coding Exercises (40% of the grade, D-010) are completed in notebooks.
- Each exercise states its objective and includes a **self-check** cell (assertions or expected output) so students get immediate feedback — consistent with the formative, unlimited-attempts policy for knowledge checks (D-015).
- **Solutions and rubrics live in `coaches/`**, never in the learner-facing `notebooks/` folder.
- Where feasible, exercises are written so a grader (or autograder) can verify output programmatically.

## 8. Required tooling recap

See `software_environment.md` for install. Minimum: a Python 3.12+ virtual environment with `numpy`, `matplotlib`, `sympy`, `jupyterlab`, `ipykernel`. No GPU required for Module 1.
