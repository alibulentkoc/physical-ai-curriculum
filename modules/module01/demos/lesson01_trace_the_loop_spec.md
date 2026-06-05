---
lesson: 1.1
title: Interactive Demonstration Spec — "Trace the Loop"
maps_to: Lesson 1.1 §7 (Interactive Demonstration)
status: specification (build in the notebook/web track)
---

# Interactive Demonstration — "Trace the Loop"

> Specification for the Lesson 1.1 interactive. The lesson's §7 describes it conceptually; this document is the build contract. A runnable first version lives in the notebook (`notebooks/lesson01_*.ipynb`); a richer web version can follow.

## 1. Purpose

Let the learner *feel* that moving a tomato changes everything downstream: its position, the reasoning about reachability, and the resulting action. It makes the perception → reasoning → action loop tangible without any math.

## 2. Learner-facing behavior

- A 2D greenhouse scene shows the **gripper at the origin** and a **draggable tomato**.
- As the learner drags the tomato:
  - an **arrow** from gripper to tomato updates live;
  - a **readout** shows the tomato's position `(right, up)` in meters and the straight-line distance;
  - a **reachability badge** turns green ("reachable") inside a reach radius and red ("out of reach") outside it.
- A **"Trace the loop"** button steps through the three stages with short captions:
  1. PERCEIVE — "camera detects the tomato"
  2. REASON — shows position + distance + reachable?
  3. ACT — "move & grip" (if reachable) or "reposition / skip" (if not)
- A **reach slider** (0.3–1.0 m) lets the learner change the arm's reach and watch the badge flip.

## 3. States & data

| State | Type | Notes |
|---|---|---|
| `tomato` | (x, y) meters | from drag; bounded to the scene |
| `reach` | meters | from slider, default 0.7 |
| `distance` | meters | derived: sqrt(x²+y²) |
| `reachable` | bool | derived: distance ≤ reach |
| `stage` | enum | perceive / reason / act, advanced by the button |

All state is in-memory; no persistence required.

## 4. Visual mapping

- Reuse the lesson palette (perceive blue, reason violet, act green).
- The reach radius is drawn as a faint circle around the origin.
- Matches `assets/diagrams/m01-l1-perception-action-loop.svg` stylistically so the static and interactive visuals feel like one family.

## 5. Acceptance criteria

- Dragging updates arrow, readout, and badge with no perceptible lag.
- The badge flips exactly at `distance == reach`.
- "Trace the loop" produces the three captioned stages in order.
- Works with keyboard (arrow keys nudge the tomato) for accessibility; readout has an aria-live region.

## 6. Implementation notes

- **Notebook version (now):** the `trace_the_loop()` function and the Matplotlib plot in `notebooks/lesson01_*.ipynb` already realize the core (position → distance → reachable → action). This satisfies §7's "conceptual / guided" bar for Units 1–7 (D-017).
- **Web version (later):** a small self-contained HTML/JS widget embedded in the MkDocs page; no backend, no browser storage. Keep it dependency-light.
- Do **not** block lesson delivery on the web version; the notebook version is the deliverable for the prototype.
