# `coaches/` — Instructor & AI Coaching Material

Material that supports **teaching** the curriculum rather than learning it: instructor guides, facilitation notes, and AI-tutor ("coach") configurations.

## Purpose

A learner reads `modules/`. An instructor — human or AI — works from `coaches/`. This folder holds everything that helps someone *deliver* the curriculum or build an AI assistant that guides students through it.

## What belongs here

- **Instructor guides** — pacing, common student misconceptions, discussion prompts
- **AI coach prompts / personas** — system prompts and behavior specs for AI tutors that walk students through topics
- **Answer keys & rubrics** — solutions and grading guidance for exercises, knowledge checks, and challenge problems
- **Assessment design** — quiz banks, project rubrics, mastery criteria
- **Office-hours playbooks** — how to unblock students on hard topics (e.g. inverse kinematics singularities, DH-parameter sign conventions)

## Suggested layout

```
coaches/
├── instructor-guides/      # per-module teaching notes
├── ai-coach/               # AI tutor prompts & personas
├── rubrics/                # grading rubrics & mastery criteria
└── answer-keys/            # solutions (keep separate from learner-facing folders)
```

## Note on solutions

Keep answer keys and rubrics here, **out of the learner-facing `modules/` tree**, so solutions aren't accidentally exposed alongside exercises.

> **Status:** Placeholder. No coaching material generated yet.
