---
module: 08
unit: 06
lesson: 6.2
title: "Publish and Subscribe: Nodes, Topics, and Messages"
core_idea: "The publish–subscribe pattern is how distributed robot subsystems exchange information: independent nodes publish messages to named topics and subscribe to the topics they need, without referencing one another directly. Map the control loop onto it — a sensor node publishes state, a controller node subscribes to state and publishes commands, an actuator node subscribes to commands — and the decoupling becomes clear: publishers and subscribers don't know about each other; the topic mediates. This is the pattern Unit 8's ROS 2 implements, taught here as a pattern, not a framework."
estimated_time: "45 min"
difficulty: "Intermediate"
prerequisites:
  - "M8 L6.1 — The loop as messages"
learning_objectives:
  - "Define nodes, topics, and messages in the publish–subscribe pattern."
  - "Map the feedback loop onto publish–subscribe (who publishes and subscribes to what)."
  - "Explain the decoupling benefit of pub/sub over direct point-to-point wiring."
  - "State that ROS 2 (Unit 8) is one implementation of this pattern."
---

# Lesson 6.2 — Publish and Subscribe: Nodes, Topics, and Messages

> Lesson 6.1 said the loop is a conversation between subsystems. This lesson gives that conversation its grammar. The dominant pattern for robot communication is **publish–subscribe**: each subsystem is a **node**; messages flow over **named topics**; a node **publishes** to the topics it produces and **subscribes** to the topics it needs — and it never has to know who else is listening or talking. That last property, decoupling, is why pub/sub scales from one joint to a whole robot. We learn it as a *pattern* you could implement many ways; Unit 8's ROS 2 is one such implementation.

---

## 1. Why This Matters
A robot is dozens of subsystems that must share information without turning into a tangle of point-to-point wires. If every node had to know the address of every other node, adding a sensor would mean rewiring half the system. Publish–subscribe dissolves that problem: a node announces its data on a named topic and anyone who cares subscribes, so producers and consumers evolve independently. This is the organising idea behind essentially every modern robotics software stack, and understanding it as a pattern — before meeting any specific framework — means you'll recognise the same shape whether you're reading ROS 2, a custom middleware, or a car's internal network.

For this course, pub/sub is also the clean way to express the distributed loop from 6.1 and to set up the timing story of 6.3–6.4. Once the loop is a set of nodes on topics, "where does latency enter?" and "which parts must run fast?" become questions about the topic graph and its timing.

## 2. Physical Intuition
Think of a community notice board. Anyone can pin a notice under a heading — "Lost Pets," "For Sale," "Events." Anyone interested in a heading checks it and reads the latest notice. The person pinning a "For Sale" notice doesn't know or care who will read it; the reader doesn't know who pinned it. The *heading* is the meeting point. Add a new reader and nothing changes for the writers; add a new writer and readers just see more notices under that heading. The board scales effortlessly because no one tracks anyone else — they only share headings.

Publish–subscribe is that notice board for machines. The headings are **topics**; the notices are **messages**; the people are **nodes**. A sensor node "pins" the joint state under the topic `joint/state`; the controller node "reads" `joint/state`, decides, and "pins" a command under `joint/command`; the actuator node "reads" `joint/command`. None of them holds a reference to another — the topic is the only thing they share. This indirection is the whole trick, and it's why you can add a logger that also reads `joint/state` without touching the sensor or controller at all.

## 3. Mathematical Foundations
The pattern has three nouns and two verbs. **Nodes** are independent units of computation (a sensor driver, a controller, an actuator driver). **Topics** are named channels. **Messages** are the typed data sent on a topic. The verbs: **publish**(topic, message) sends; **subscribe**(topic, callback) registers interest so the callback runs on each new message. The defining property is **decoupling**: a publisher names only the topic, never the subscribers, and vice versa.

The engine's `Bus` is a minimal, in-process realisation of exactly this pattern — `subscribe(topic, cb)`, `publish(topic, msg)` (which delivers to every subscriber of that topic and stores the latest), and `latest(topic)`. It is deliberately tiny: no networking, no serialization, no framework — just the pattern, so the idea is visible without machinery. Mapping the loop onto it: a **sensor node** publishes `{q, q_d}` to `joint/state`; a **controller node** subscribes to `joint/state`, computes $u$, and publishes `{u}` to `joint/command`; an **actuator node** subscribes to `joint/command` and drives the plant. The verified facts from the notebook: every state message reaches all of its subscribers (four states published → four deliveries to each subscriber), the controller publishes exactly one command per state it receives, the latest command reflects the latest error, and a topic with no subscribers simply stores its latest message — pure decoupling, no node referencing another.

This is genuinely a *pattern*, not a framework tutorial. ROS 2 (Unit 8) implements publish–subscribe with real networking, message types, quality-of-service policies, and discovery — but the shape you're learning here, nodes/topics/messages with decoupled publish and subscribe, is exactly the shape ROS 2 provides. Learn the pattern now; meet the implementation in Unit 8.

## 4. Visual Explanation
`[Visual: a topic graph for the control loop — a SENSOR node with an arrow publishing to a topic box 'joint/state', a CONTROLLER node subscribing to 'joint/state' and publishing to a topic box 'joint/command', an ACTUATOR node subscribing to 'joint/command'; a dashed extra subscriber (a LOGGER) also reading 'joint/state' to show decoupling; nodes are drawn as circles, topics as labelled rounded boxes, publish/subscribe arrows distinguished; a caption notes nodes never reference each other — the topic mediates — and that ROS 2 is one implementation]`

**Diagram Specification**

- **Objective:** show nodes/topics/messages and the decoupling of publishers from subscribers.
- **Scene:** circles for nodes (**Sensor**, **Controller**, **Actuator**, plus a dashed **Logger**), rounded boxes for topics (**joint/state**, **joint/command**). Arrows: Sensor —publish→ joint/state; joint/state —subscribe→ Controller; joint/state —subscribe→ Logger (dashed, "added without touching anyone"); Controller —publish→ joint/command; joint/command —subscribe→ Actuator. A note: "nodes never reference each other — the topic mediates (decoupling)". A small footnote box: "ROS 2 (Unit 8) is one implementation of this pattern."
- **Labels:** "node", "topic", "message", "publish", "subscribe", "decoupling: add a subscriber freely", "pattern, not a framework".
- **Form:** SVG, a node/topic graph with distinct publish vs subscribe arrows. Nodes ink `#0f172a`, topic boxes teal-outlined `#0d9488` on soft `#f8fafc`, publish arrows sky `#0ea5e9`, subscribe arrows emerald `#10b981`, the added logger dashed muted `#64748b`.

## 5. Engineering Example
Publish–subscribe is the backbone of modern robotics middleware. ROS and ROS 2 organise an entire robot as nodes publishing and subscribing on topics — `/scan` for a lidar, `/cmd_vel` for velocity commands, `/joint_states` for the arm — so a navigation node and a logging node can both consume the lidar without the lidar driver knowing either exists. Automotive systems use the same shape over DDS and similar buses. Industrial and IoT systems use brokers like MQTT, where devices publish sensor readings to topics and dashboards subscribe. The common thread is decoupling for scale: in every one of these systems you can add a consumer (a recorder, a monitor, a safety checker) to an existing topic without modifying the producer — exactly the property the tiny `Bus` demonstrates.

## 6. Worked Example
The loop as a topic graph.

- **Setup:** a `Bus`; a sensor node publishing to `joint/state`; a controller node subscribing to `joint/state` and publishing to `joint/command`; an actuator node subscribing to `joint/command`. Two extra subscribers count deliveries.
- **Run:** publish four successive states (joint positions 0.0, 0.2, 0.5, 0.9 toward a target of 1.0). Each published state is delivered to every subscriber (four deliveries each), and the controller publishes one command per state.
- **Decoupling check:** the latest command equals $40 \times (1.0 - 0.9)$ — it reflects only the most recent error, computed by a controller that never references the sensor. A fresh topic with no subscribers returns its stored latest (or nothing if never published) — proof that publishing doesn't require knowing the audience.
- The notebook asserts all four deliveries reach each subscriber, the controller emits one command per state, the latest command matches the latest error, and an unsubscribed topic just stores its latest.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook. The flagship Message Bus demo for Unit 6 lives in Lesson 6.1.)*

**The topic-graph walkthrough.** In the notebook you:

1. Wire a sensor, a controller, and an actuator as nodes on a `Bus`, communicating only through topics.
2. Publish states and watch the controller react and publish commands — the loop running through topics alone.
3. Add a second subscriber to an existing topic and confirm nothing about the publisher changes — decoupling in action.

## 8. Coding Exercise
*(Companion notebook — uses `Bus.subscribe`, `Bus.publish`, `Bus.latest`.)*

In the notebook you:

1. Build a `Bus` and register subscribers that count delivered messages on `joint/state` and `joint/command`.
2. Wire a controller node that subscribes to `joint/state` and publishes to `joint/command`, then publish a sequence of states.
3. Assert every message reaches its subscribers, the controller emits one command per state, and the latest command reflects the latest error — confirming the loop runs purely through decoupled topics.

## 9. Knowledge Check
1. Define node, topic, and message.
2. Map the control loop onto publish–subscribe: who publishes and subscribes to what?
3. What does "decoupling" mean here, and why does it help a robot scale?
4. What is the relationship between this pattern and ROS 2?

## 10. Challenge Problem
A team wants to add data logging and a safety monitor to a running robot without risking the control loop. Explain how the publish–subscribe pattern lets them do this by subscribing the new nodes to existing topics, and why the same change would be invasive in a point-to-point design where the controller calls the sensor directly. Then describe the full topic graph of the control loop and identify exactly which decoupling property each addition relies on. Finally, state clearly what this lesson is and isn't: why is it correct to call pub/sub a *pattern* rather than "ROS 2," and what specifically does Unit 8's ROS 2 add on top of the pattern? *(You are defending decoupling as the reason pub/sub scales, and placing ROS 2 as an implementation.)*

## 11. Common Mistakes
- **Thinking nodes call each other.** They don't — they publish and subscribe to topics; the topic mediates.
- **Confusing the pattern with a framework.** Pub/sub is the shape; ROS 2, DDS, MQTT are implementations.
- **Assuming a publisher needs a subscriber.** Publishing to a topic with no subscribers is fine; the message is simply stored as the latest.
- **Hard-coding consumers into producers.** That breaks decoupling and the ability to add nodes freely.

## 12. Key Takeaways
- **Publish–subscribe** organises distributed robots: **nodes** publish **messages** to named **topics** and subscribe to the topics they need.
- The loop maps cleanly: **sensor** publishes `joint/state`; **controller** subscribes to it and publishes `joint/command`; **actuator** subscribes to that.
- **Decoupling** is the payoff — publishers and subscribers never reference each other, so nodes (loggers, monitors) can be added freely; the topic is the only shared thing.
- This is a **pattern, not a framework**: ROS 2 (Unit 8) is one implementation, adding networking, message types, and quality-of-service on top of the same nodes/topics/messages shape.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain publish–subscribe using the 'community notice board' analogy: headings = topics, notices = messages, people = nodes, and writers/readers never know each other. Then map the control loop onto it and explain why decoupling lets you add a logger without touching the sensor."
- **Practice (generate exercises):** "Give me a small robot subsystem set and ask me to design the topic graph — which nodes publish/subscribe to which topics — and to spot any broken decoupling. Withhold the answer until I respond."
- **Explore (connect to the real world):** "Give real pub/sub systems (ROS 2 topics like /scan and /cmd_vel, automotive DDS, MQTT IoT) and ask me to identify the nodes, topics, and the decoupling benefit in each, and what each adds beyond the bare pattern."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain the publish–subscribe pattern — nodes, topics, messages, decoupled publish and subscribe — map the control loop onto it, and explain decoupling and why ROS 2 (Unit 8) is one implementation — at a robotics-course level (pattern, not a framework tutorial; no ROS 2 API)."
- **Español:** "Explica el patrón publicar–suscribir — nodos, temas (topics), mensajes, publicación y suscripción desacopladas — mapea el lazo de control sobre él, y explica el desacoplamiento y por qué ROS 2 (Unidad 8) es una implementación — a nivel de curso de robótica (patrón, no un tutorial de framework; sin API de ROS 2)."
- **中文（简体）：** "解释发布–订阅模式——节点、话题(topic)、消息，以及解耦的发布与订阅——把控制回路映射到它上面，解释解耦以及为什么 ROS 2（第8单元）是一种实现——达到机器人课程水平（模式，而非框架教程；不涉及 ROS 2 API）。"
- **Türkçe:** "Yayınla–abone ol desenini açıkla — düğümler, konular (topic), mesajlar, ayrıştırılmış yayınlama ve abone olma — denetim döngüsünü buna eşle ve ayrıştırmayı, ayrıca ROS 2'nin (Ünite 8) neden bir uygulama olduğunu açıkla — robotik dersi düzeyinde (desen, framework öğreticisi değil; ROS 2 API yok)."

---

*Next: Lesson 6.3 — Latency and Control Rate: How Communication Destabilises the Loop.*
