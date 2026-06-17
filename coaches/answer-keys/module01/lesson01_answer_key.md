---
lesson: 1.1
title: Physical AI and the Physical World — Answer Key & Feedback
audience: instructors / AI coach ONLY (not learner-facing)
location_policy: answer keys live in coaches/, never in modules/
---

# Lesson 1.1 — Answer Key & Feedback

> Instructor/coach reference for `modules/module01/quizzes/lesson01_quiz.yaml`. Knowledge checks are formative (D-015): the feedback below is what the system shows after each attempt, not a grade.

## Knowledge Check

**1.1-q1 — Physical AI vs software AI (short answer).**
Accept answers conveying: Physical AI **senses, decides, and acts in the real, physical world** (through sensors and actuators), whereas software-only AI operates on already-digital data with no physical consequence. *Feedback if weak:* emphasize the sensing→acting loop and real-world consequences.

**1.1-q2 — Loop ordering (MC).** Correct: **B (Perception → Reasoning → Action).**
*Feedback:* the robot must sense before it can decide, and decide before it acts; the loop then repeats.

**1.1-q3 — Stage ↔ language (matching).**
Perceive → **pixels**; Reason → **meters / frames**; Act → **joint angles**.
*Feedback:* the "languages" differ at each stage, which is why translation between them is the core problem.

**1.1-q4 — Why not use the camera-frame position directly (short answer).**
Accept: the camera and the arm are in **different reference frames**; a position expressed in the camera's frame is not the same numbers in the robot's base frame, so it must be **transformed** first (foreshadows Unit 3 / Module 2). *Feedback if weak:* name "different frames" explicitly.

**1.1-q5 — Nature of the chain (MC).** Correct: **A (translating between different spatial representations).**
*Feedback:* each arrow is a change of representation, handled by the math of Module 1.

**1.1-q6 — Small position error has no cost (T/F).** Correct: **False.**
*Feedback:* in Physical AI, a few centimeters can mean grabbing a leaf or crushing a stem — physical consequences are exactly why precision matters.

## Challenge Problem (§10) — Rubric

Open-ended; no single answer. Score on transfer and reasoning rather than correctness.

| Criterion | Strong response shows |
|---|---|
| Identifies sensor/decision/actuator | Correctly names all three for the chosen system |
| Locates a spatial "language" translation | Points to a real sensor-frame → world-frame (or similar) translation |
| Predicts a physical consequence | Gives a concrete, plausible real-world failure of a mis-translation |
| Transfer quality | Maps the perception-action loop cleanly onto a system *outside* agriculture |

Suggested band (per D-015 competency framing): full credit if all four criteria are met with a coherent argument; partial if the spatial-translation insight is missing (the key idea of the lesson).
