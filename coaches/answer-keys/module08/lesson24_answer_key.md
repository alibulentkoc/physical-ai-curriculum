---
module: 8
unit: 6
lesson: 4
type: answer_key
title: "Answer Key — A Data-Flow Architecture Layered by Timing"
audience: coaches
---

# Answer Key 6.4 — A Data-Flow Architecture Layered by Timing

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** their timing — rate and tolerance to latency

**Q2 — B.** the inner control loop, because it IS the feedback timing

**Q3 — B.** run slower and tolerate more latency because the inner loop tracks whatever setpoint it's handed

**Q4 — B.** heavy latency in the inner loop is unstable, but the same slowness in the outer reference update stays stable

**Q5 — B.** real-time execution for the inner loop (Unit 7) and the ROS 2 stack that hosts all layers (Unit 8)

---

**Q6 — model answer.** Because the heavy, capable work — perception and motion planning — is computationally expensive and cannot run at inner-loop rates (hundreds to thousands of hertz). Demanding that of the whole robot is infeasible. The architectural resolution is to separate the parts that must be fast from the parts that can be slow: give the delay-sensitive inner control loop fast, predictable timing, and let the delay-tolerant outer layers (planning, perception, supervision) run slower. Matching each job's timing to its sensitivity is what makes the robot both responsive and capable.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** The joint controller belongs to the fast, latency-critical inner loop — it closes feedback around the joint and must run at a high, predictable rate (e.g., ~1 kHz) with bounded latency, because delay here destabilises it (6.3). The trajectory planner (Module 7) and the vision system are outer layers: they're heavy and delay-tolerant, running at tens of hertz or less, producing references the inner loop tracks between updates. The safety supervisor is an outer-layer overseer that runs at a modest rate but with high priority. A single publish–subscribe stack hosts all of them as nodes on topics; the inner loop gets the real-time guarantee (Unit 7) and ROS 2 (Unit 8) is the implementation.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Units 1–4 produced a controller that decides what command to send, assuming the command reached the joint instantly and perfectly. Unit 5 (actuators) replaced that fiction with the truth that a requested command becomes a delivered effort shaped by saturation, deadband, stiction, and rate limits — a feasibility envelope that bounds what the joint can physically do. Unit 6 (communication) replaced the other fiction — instantaneous, single-place execution — with a distributed system of nodes exchanging messages, where loop latency and a finite control rate can destabilise the loop, forcing a timing-layered architecture with a fast inner loop and slow outer layers. Together they carry the controller from an idealised decision to a real, distributed, delay-bound, actuator-limited system that actually moves the arm — and they tee up real-time execution (Unit 7) and the ROS 2 stack (Unit 8).
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Trying to make the whole robot fast — only the inner loop must be fast and predictable.
- Putting delay-sensitive work in a slow layer — joint control there goes unstable.
- Confusing 'layered' with 'built' — real-time (Unit 7) and ROS 2 (Unit 8) are named, not implemented.
