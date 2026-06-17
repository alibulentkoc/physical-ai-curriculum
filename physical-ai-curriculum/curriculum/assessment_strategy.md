# Assessment Strategy

> **Scope:** Assessment philosophy for the curriculum, calibrated to **Module 1**.
> **Authority:** Weights are Architect Decision **D-010** (APPROVED). Mastery thresholds in §4 are **drafted by Implementation** and await architect confirmation.
> **Purpose:** Define how learning is measured, how it maps to the 12-part topic template, and how grades are composed — without writing any assessment items (those are authored per topic later).

---

## 1. Philosophy

Assessment serves learning, not ranking. It follows the curriculum's five-layer philosophy: a student demonstrates mastery by **doing** — computing, coding, and modeling — not only by recalling. Most assessment weight therefore sits on applied work (coding and the mini project), with lighter formative checks confirming conceptual understanding along the way.

Two complementary modes:
- **Formative** — low/no stakes, frequent, embedded in lessons; tells the student (and coach) where understanding is thin while there's still time to fix it.
- **Summative** — graded, confirms competency at unit and module boundaries.

---

## 2. Module 1 grade composition (APPROVED — D-010)

| Component | Weight | Mode | Maps to template section |
|---|---|---|---|
| Coding Exercises | **40%** | Summative | §8 Coding Exercise |
| Knowledge Checks | **25%** | Formative→graded | §9 Knowledge Check |
| Challenge Problems | **15%** | Summative (stretch) | §10 Challenge Problem |
| Mini Project | **20%** | Summative (integrative) | Unit 9 deliverable |
| **Total** | **100%** | | |

The weighting deliberately privileges applied skill: 60% (coding + mini project) is "build something that works," 40% (knowledge checks + challenges) confirms the reasoning underneath.

---

## 3. How each component works

### Coding Exercises (40%)
Per-topic notebooks where students implement the mathematics (e.g. vector ops, coordinate conversion, transformation matrices). Graded on correctness, reproducibility (Restart & Run All passes), and clarity. This is the largest weight because computational implementation is the curriculum's core skill.

### Knowledge Checks (25%)
Short conceptual questions embedded in each topic. **Formative only** — unlimited attempts with immediate feedback. They are not summatively graded; participation credit applies only where an LMS requires a score. Their purpose is to catch thin understanding early, not to rank.

### Challenge Problems (15%)
One stretch problem per topic, beyond the worked examples. Rewards depth and transfer. Lower weight so it motivates without punishing students who master the core but not every stretch.

### Mini Project (20%)
The Unit 9 integrative deliverable — modeling the Greenhouse Robot workspace. Graded against a rubric covering: correctness of the model, explicitness of assumptions, code reproducibility, and quality of visualization. This is where the five layers come together.

---

## 4. Mastery thresholds (FINAL · D-015)

| Level | Overall score | Meaning |
|---|---|---|
| Mastery | ≥ 85% | Strong readiness for Module 2 |
| Proficient | 70–84% | Ready, with light review of weak units |
| Developing | 50–69% | Targeted remediation before Module 2 |
| Beginning | < 50% | Repeat key units |

**Exit gate (competency-based, overrides numeric score):** A student does not advance to Module 2 until the manifest §16 competencies are demonstrated, regardless of percentage. A passing numeric grade alone is insufficient. The required competencies are: vector representation/operations, coordinate frames, matrix transformations, trigonometric reasoning, computational mathematics in Python, and workspace modeling.

---

## 5. Unit checkpoints

Each of Units 1–8 ends with a short checkpoint confirming that unit's competencies (per manifest §9). Checkpoints are formative early in a unit and graded at the unit boundary. Unit 9 *is* the mini project and has no separate checkpoint.

---

## 6. Rubrics and answer keys

To keep solutions out of learner-facing folders:
- **Rubrics** (mini project, challenge problems, checkpoints) live in `coaches/rubrics/`.
- **Answer keys** live in `coaches/answer-keys/`.
- Neither is placed in `modules/`.

Rubric and key authoring is a later deliverable; this document defines the *strategy*, not the items.

---

## 7. Feedback loop

- Formative results steer pacing: a unit checkpoint failing broadly signals the lesson needs revision, not just the student.
- The coaching layer (`coaches/`) uses checkpoint data to target office-hours playbooks at the topics that reliably trip students up (e.g. frame conventions, matrix composition order).

---

## 8. Resolved policy (D-015)

- ✅ Mastery thresholds set: 85 / 70 / 50 (Mastery / Proficient / Developing / Beginning).
- ✅ Knowledge Checks are formative only (unlimited attempts, immediate feedback).
- ✅ Competency-based exit gate overrides the numeric score.
