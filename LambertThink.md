# LambertThink - Development Philosophy & DevLog 🧠

> "This is not just a stack of code; it is an experiment in the fusion of Industrial Automation and Edge Computing."

This document records my core thinking process during the three-month development of the `Wago-Data` project. My goal was not merely to create examples, but to cultivate a modern **Industrial IoT Tech Stack** on the foundation of WAGO controllers.

---

## 💡 Why go this "Crazy"?

In the traditional automation world, Programmable Logic Controllers (PLCs) are often viewed as closed-box logic switches. From my perspective, a WAGO controller—equipped with a Linux kernel and Docker support—is actually a **hidden edge server inside a power distribution cabinet.**

Over the past 90 days, my development has followed three core philosophies:

### 1. Data Sovereignty and "Near-Field" Processing
I do not believe in blindly pushing all raw data to the cloud.
* **The Necessity of SQLite**: Data should be structured and stored locally first. This mitigates the risk of network outages and provides an "on-device" historical record for self-diagnosis.
* **Data Cleaning**: Processing data at the edge and only uploading critical results is the hallmark of an efficient architecture.

### 2. Node-RED: The Bridge between IT and OT
Node-RED serves as the "Digital Glue" of this project.
* It allows a PLC to speak to Discord and interact with Webhooks for the first time.
* When a hardware alarm becomes a real-time mobile notification, the value of OT (Operational Technology) finally becomes visible to IT-level management.

### 3. From Standalone to Cluster: The Revelation of Docker Swarm
The move toward Swarm orchestration marks a major turning point in my thinking.
* **High Availability (HA)**: A factory shouldn't lose its data pipeline just because one controller fails. By clustering, I can make services "hop" between hardware, achieving true industrial-grade server resilience.

---

## 🚀 The Path to Advanced Edge Computing

My goal is to build a **bottom-up** comprehensive system:

1.  **L1 - Perception Layer (Codesys)**: Ensuring stable communication and logic—the source of all data.
2.  **L2 - Mediation Layer (Node-RED & SQLite)**: Processing, transforming, and persisting data to make it "talk."
3.  **L3 - Orchestration Layer (Docker Swarm)**: Integrating multiple nodes into a single entity to provide server-level computing resources.
4.  **L4 - Integration Layer (Cloud Hybrid)**: Connecting local clusters with private or public clouds for cross-regional management.

---

## 🛠 Solving Pain Points

- **Cross-Domain Communication**: Resolved difficulties in Modbus access across different network segments and gateways.
- **Discord Integration**: Bridged the gap between industrial protocols and modern encrypted APIs.
- **Scheduling Flexibility**: Broke the limitation of needing to re-compile PLC code for logic changes by releasing operational flexibility through a visual interface.

---

## 🤖 The AI Frontier: The Next Conquest

Once the Swarm cluster is stable, the next step is to give these controllers the ability to "think."
I plan to introduce **Industrial AI** to move beyond simple logic toward:
- **Predictive Maintenance**: Letting equipment "call for help" before a failure occurs to avoid downtime losses.
- **Edge Vision**: Integrating image processing (OpenCV/YOLO) to give the controller visual judgment capabilities.

We don't necessarily need expensive cloud storage. Through software-defined architecture, we can build powerful and flexible monitoring centers right at the edge.

---
**Lambert** *Written on January 30, 2026 - The 3-Month Project Milestone*
