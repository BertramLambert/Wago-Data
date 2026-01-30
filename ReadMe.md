# Wago-Data
🌐 [English Version](./ReadMe.md) | [繁體中文版本](./ReadMe-zh.md)

This repository provides **WAGO** software examples and technical operation manuals to help you get started with industrial automation tasks.

---

## 📂 Overview

- **Software Examples**: Includes [Codesys](#codesys-example), [Python](#python-example), and [Node-RED](#node-red).
- **Controller Operation Manuals**: Covers hardware-specific guides for [CC100](#cc100-controller), [BC100](#bc100-controller), and [PFC200](#pfc200-controller).
- **Environment Setup**: Guides for [Docker](#docker-operation), [Switch](#-Switch-Opeartion) configurations, and controller runtime environments.

---

## 🛠 Software Examples

### Codesys Example
- **SQLite Integration**: Local database management within the Codesys runtime.
- **Modbus TCP Communication**: Read/Write data across different network domains and gateways.
- **MQTT-Publish**: Send controller data (Sensors/Status) to an MQTT Broker (e.g., Mosquitto, Azure IoT Hub).
- **MQTT-Subscribe**: Receive remote commands or configurations from a Broker to control hardware output.
- **OPC UA Server**: Enables the controller to provide I/O signals and variable access to SCADA/HMI systems via the OPC UA protocol.

### Python Example
- **Web Dashboard**: Python Runtime using **Flask** and **Vue.js/HTML** for custom Web HMI and API development.

### Node-RED
- **Webhook Integration**: Receive and process HTTP requests from external cloud services or third-party APIs.
- **WebSocket Communication**: Real-time bi-directional data exchange for live dashboards and low-latency control.
- **Discord Bot Integration**: 
  - **Interactive Commands**: Control the WAGO controller remotely via Discord chat commands.
  - **Status Notifications**: Push real-time hardware alarms and event logs directly to your Discord channel.
- **Edge-Schedule System**
  - **Timed Automation**: Implement complex scheduling logic (Cron jobs) to trigger hardware outputs independently of PLC runtime.
  - **Operational Flexibility**: Easily adjust production shifts or lighting schedules via a visual interface without recompiling PLC code.
- **SQLite DataLogger**:
  - **Local Persistence**: Log critical operational data into an internal SQLite database for long-term tracking and offline data integrity.
  - **Historical Querying**: Enable the ability to retrieve past events or trends directly from the controller's storage.
- **Protocol Gateway**:
  - **IT/OT Convergence**: Bridge the gap between industrial protocols (Modbus, OPC UA) and IT standards (MQTT, RESTful APIs, JSON).
  - **Cross-Platform Interoperability**: Enable seamless data exchange between different brands of automation hardware and cloud services.
- **Interactive Dashboard (Web HMI)**:
  - **Real-time Monitoring**: Visualize sensor data and system status through gauges, charts, and status indicators.
  - **Remote Control**: Toggle digital outputs or adjust setpoints directly from a web browser or mobile device.
  - **Low-code UI**: Demonstrate how to build a professional industrial interface without HTML/CSS knowledge.

---

## 🐳 Docker Operation
*Specific steps and best practices for running Docker containers on WAGO controllers.*

---

## 🏗 Hardware Controllers

### CC100 Controller
- **751-9301** (Compact Controller 100)
- **751-9401**

### BC100 Controller
- **750-8001**

### PFC200 Controller
- **750-8212** (PFC200 Generation 2)

---

## 📶 Switch Opeartion
-

---
*Last updated: 2026/1/30*
