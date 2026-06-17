---
title: Internationalization Strategy
status: standard
authority: curriculum enhancement (AI-native, globally accessible; English authoritative)
---

# Internationalization Strategy

> How the curriculum stays **globally accessible** while keeping **English as the single authoritative source**. The near-term approach is AI-assisted: students learn in their language via copy/paste prompts, with no separate translated lessons to maintain.

## 1. English as the authoritative source language

- All lessons, notebooks, quizzes, diagrams, and assessments are authored and maintained in **English**.
- English is the **source of truth**: any translated or AI-generated explanation derives from the English lesson and never overrides it.
- This avoids the central failure mode of multilingual courseware — drift between language versions — by having exactly one canonical version.

## 2. AI-assisted multilingual learning workflow

Every lesson ends with a **Global Learning Support** block: ready-to-paste prompts that ask an AI assistant (ChatGPT, Claude, etc.) to explain *that* lesson in the student's language and produce a summary, three practice questions, and one challenge problem.

Workflow:
1. Student reads the English lesson (and uses the interactive assets).
2. Student copies the prompt for their language from Global Learning Support.
3. The AI produces an explanation + practice in their language, preserving English technical terms where appropriate.

This gives immediate, zero-maintenance multilingual access. The AI output is a **study aid**, not a published translation; the English lesson remains authoritative.

## 3. Language selector roadmap

- **Phase 1 (now):** English-only content + AI-assisted multilingual support (the prompts). No selector needed.
- **Phase 2:** A **language selector in MkDocs** (e.g. Material's i18n/translation plugin) that surfaces available languages per page.
- **Phase 3:** **Human-reviewed translations** for selected high-value modules, served through the Phase 2 selector, with the English version still authoritative.

## 4. Terminology preservation rules

To keep the curriculum interoperable with global robotics practice, the following are **kept in English** even in translated/AI output:

- **Mathematical notation** — symbols, equations, variable names ($\mathbf{v}$, $\theta$, SE(3)) are never localized.
- **Robotics terms of art** where English is the field standard — e.g. *frame*, *end-effector*, *Jacobian*, *Denavit–Hartenberg*, *forward/inverse kinematics*, *SLAM*, *ROS 2*.
- **Code, APIs, library names** — NumPy, Matplotlib, etc.
- **Units** follow SI; symbols (m, kg, rad) are universal.

Prose, intuition, and explanation are translated; the technical scaffolding stays in English so a student can move between languages and the literature without relearning terms. The Global Learning Support prompts encode this rule ("keep robotics/mathematical terminology in English when appropriate").

## 5. Future localization strategy

- Treat the English lesson as the source; generate **draft** translations (AI-assisted) for review rather than hand-writing from scratch.
- Localize in this order of value: lesson prose → quiz questions → diagram labels (SVG `<text>` is translatable) → notebook markdown (code/comments stay English).
- Maintain a **glossary** (English term → approved translation per language) so reviewed translations are consistent. This pairs with the curriculum notation glossary planned for `docs/`.
- Version translations against the English lesson's revision so drift is detectable; if English changes, the translation is flagged stale.

## 6. Supported-language roadmap

Initial set (Phase 1 prompts): **English, Español, 中文 (Simplified Chinese), Türkçe.**

Expansion is cheap in Phase 1 (add a prompt per language). Candidate additions as demand appears: Français, Deutsch, العربية, हिन्दी, Português. A language enters Phase 3 (human-reviewed) only when there is reviewer capacity and clear demand for that audience.

## 7. Where this lives in a lesson

Per the lesson template, two standard blocks appear after **Key Takeaways** and before the **Next lesson** footer:
1. **AI Learning Companion** — Tutor / Practice / Explore prompts (learning in English, another way).
2. **Global Learning Support** — per-language explanation prompts (learning in another language).

Both are generated from the lesson title, so they stay correct as lessons are added.
