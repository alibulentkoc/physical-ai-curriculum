---
module: 8
unit: 8
lesson: 8.1
type: answer_key
title: "Answer Key 8.1 — The Closed-Loop Control Stack in ROS 2"
audience: coaches
---

# Answer Key 8.1 — The Closed-Loop Control Stack in ROS 2

*Coaches' key. Multiple-choice answers with the correct option; model answers for the short-response items, with grading guidance; and common misconceptions to watch for.*

**Q1 — B.** ROS 2 node/topic graph

*Why:* Sensor, controller, and actuator nodes communicate over topics.

**Q2 — B.** joint/state and joint/command

*Why:* The sensor publishes joint/state; the controller publishes joint/command.

**Q3 — B.** Subscribes to state + reference, computes the command, publishes it

*Why:* It carries the feedforward + PID law and the actuator pipeline.

**Q4 — B.** In the controller node

*Why:* The controller node carries the latency-critical inner loop (Unit 7).

**Q5 — B.** You subscribe to existing topics without rewiring the controller

*Why:* Pub/sub decoupling (6.2) lets new subscribers tap topics non-invasively.

**Q6 — model answer.** Sensor node: publishes joint/state (measured state, with the reference sample). Controller node (tracker): subscribes to joint/state, publishes joint/command. Actuator node: subscribes to joint/command and drives the plant. The motion is sensed again, closing the loop.

**Q7 — model answer.** Each communication hop (sensor→controller, controller→actuator) adds delay; the loop latency is the sum of the hops (Unit 6). The real-time target keeps the controller node's period deterministic and the hops small, so the total loop delay stays within the stable region.

**Q8 — model answer.** We modelled the pattern — nodes, topics, messages, publish/subscribe — using an in-process bus. We did not build the production implementation (DDS middleware, rclpy, executors, QoS), which is out of scope; the transferable idea is the node/topic structure.

*Grading: award full credit for a short answer that captures the key idea in the model answer, even if briefer or differently worded; partial credit if the core mechanism is named but not fully explained.*

### Common misconceptions to watch for

- Thinking nodes call each other directly; they publish/subscribe to topics, and the topic mediates.
- Assuming the graph alone guarantees timing — the real-time requirement lives in the controller node.
- Confusing the ROS 2 pattern with the framework — we model nodes/topics/messages, not DDS/rclpy.
