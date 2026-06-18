---
module: 8
unit: 6
lesson: 2
type: answer_key
title: "Answer Key — Publish and Subscribe: Nodes, Topics, and Messages"
audience: coaches
---

# Answer Key 6.2 — Publish and Subscribe: Nodes, Topics, and Messages

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** publishes to and subscribes from named topics, without referencing other nodes

**Q2 — B.** the sensor publishes joint/state; the controller subscribes to it and publishes joint/command; the actuator subscribes to that

**Q3 — B.** publishers and subscribers don't reference each other; the topic is the only shared thing

**Q4 — B.** requires no change to the sensor or controller — it just subscribes

**Q5 — B.** one implementation of the pub/sub pattern, adding networking, message types, and QoS

---

**Q6 — model answer.** A node is an independent unit of computation (e.g., a sensor driver, a controller, an actuator driver). A topic is a named channel. A message is the typed data sent on a topic. The two verbs are publish(topic, message), which sends data on a topic, and subscribe(topic, callback), which registers interest so the callback runs on each new message. The defining property is decoupling: a publisher names only the topic, never its subscribers, and vice versa.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Because producers and consumers never reference each other, you can add, remove, or change a node without touching the others — only the shared topic names matter. A new logger, safety monitor, or second consumer just subscribes to an existing topic; a new sensor just publishes a new topic. In a point-to-point design where the controller calls the sensor directly, every such change means rewiring, and the number of connections grows explosively. Pub/sub keeps the system loosely coupled, so it can grow from one joint to a whole robot without becoming a tangle.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Pub/sub is a pattern because it describes a shape — nodes, named topics, messages, decoupled publish and subscribe — that can be implemented many ways (a tiny in-process bus, MQTT, DDS, ROS 2). The shape is what you learn and reuse; the implementation is a detail. ROS 2 (Unit 8) is one implementation that adds real networking and node discovery, typed message definitions, quality-of-service policies (reliability, history), and tooling — but underneath it is exactly the nodes/topics/messages pattern, so recognising the pattern means you'll recognise ROS 2 immediately.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Thinking nodes call each other — they publish/subscribe to topics; the topic mediates.
- Confusing the pattern with a framework (ROS 2, DDS, MQTT are implementations of it).
- Assuming a publisher needs a subscriber — publishing to an unsubscribed topic is fine.
