# Wago-Data
🌐 [English Version](./ReadMe.md) | [繁體中文版本](./ReadMe-zh.md)

This repository provides software examples and technical manuals for **WAGO** controllers, designed to help users quickly implement industrial automation, edge computing, and distributed cluster tasks.

---

## 📂 Overview

- **Software Examples**: Includes [Codesys](#codesys-examples), [Python](#python-examples), and [Node-RED](#node-red-examples).
- **System Architecture**: Advanced topics on [Edge Server Swarm](#-edge-server-swarm).
- **Controller Manuals**: Hardware-specific guides for [CC100](#cc100-controller), [BC100](#bc100-controller), and [PFC200](#pfc200-controller).
- **Environment Setup**: Configurations for [Docker](#-docker-operations), [Routers](#-router-operations), and Controller Runtimes.

---

## 🛠 Software Examples

### Codesys Examples
- **SQLite Integration**: Demonstrate how to create and manage local databases directly within the Codesys Runtime.
- **Modbus TCP Communication**: Implement cross-domain data read/write operations and gateway integration.
- **MQTT-Publish**: Send controller data (sensor values/device status) to an MQTT Broker (e.g., Mosquitto, Azure IoT Hub).
- **MQTT-Subscribe**: Receive remote commands or configurations from a Broker to control hardware outputs.
- **OPC UA Server**: Enable the controller as a server to provide I/O signals and variables to SCADA or HMI systems via standardized protocols.

### Python Examples
- **Web Dashboard (Web HMI)**: Use **Flask** as a backend API with a **Vue.js/HTML** frontend to develop custom visual monitoring interfaces.

### Node-RED Examples
- **Webhook Integration**: Receive and process HTTP requests from external cloud services or third-party APIs.
- **WebSocket Communication**: Real-time bi-directional data exchange for live dashboards and low-latency control.
- **Discord Bot Integration**: 
  - **Interactive Commands**: Control the WAGO controller remotely via Discord chat commands.
  - **Status Notifications**: Push real-time hardware alarms and event logs directly to your Discord channel.
- **Edge-Schedule System**:
  - **Timed Automation**: Implement complex scheduling logic (Cron jobs) to trigger hardware outputs independently of the PLC main task.
  - **Operational Flexibility**: Easily adjust schedules via a visual interface without recompiling PLC code.
- **SQLite DataLogger**:
  - **Local Persistence**: Log critical operational data into an internal SQLite database to ensure data integrity and offline traceability.
  - **Historical Querying**: Retrieve past events or trends directly from the controller's internal storage.
- **Protocol Gateway**:
  - **IT/OT Convergence**: Bridge the gap between industrial protocols (Modbus, OPC UA) and IT standards (MQTT, RESTful API, JSON).
  - **Cross-Platform Interoperability**: Enable seamless data exchange between different automation hardware brands and cloud services.
- **Interactive Dashboard (Web HMI)**:
  - **Real-time Monitoring**: Visualize sensor data and system status through gauges, charts, and status indicators.
  - **Remote Control**: Toggle digital outputs or adjust setpoints directly from a web browser or mobile device.

---

## 🌐 Edge Server Swarm
*Advanced section demonstrating the integration of multiple WAGO controllers into a distributed computing cluster.*

- **Docker Swarm Orchestration**: 
  - **Cluster Initialization**: How to initialize and join multiple controllers as Manager and Worker nodes.
  - **Service Deployment**: Use Docker Stack for cross-node service deployment and load balancing.
- **High Availability & Failover (HA)**: 
  - Mechanisms for automatic service migration and recovery when a single node goes offline.
- **Virtual Overlay Network**: 
  - Establish secure internal networks for container-to-container communication across different controllers.

---

## 🐳 Docker Operations
*Best practices for running Docker containers on WAGO hardware, including image management and resource allocation.*

---

## 🏗 Hardware Specifications

### CC100 Controller
- **751-9301** (Compact Controller 100)
- **751-9401**

### BC100 Controller
- **750-8001**

### PFC200 Controller
- **750-8212** (PFC200 Generation 2)

---

## 📶 Router Operations

*Last updated: 2026/01/30*
