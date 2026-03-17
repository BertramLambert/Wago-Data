# 🚀 Lambert Nexus V2: WAGO CC100 IIoT Dashboard

[中文](Readme-zh.md) | [English](Readme.md)

This project is a sophisticated Web Integration and Control System based on the **WAGO CC100 (751-9301)** industrial controller. It leverages **Node-RED Dashboard 2.0** powered by **Vue.js** to bridge the gap between physical industrial IO control and modern web services (SQLite, Social Media APIs).

## 🛠 Tech Stack
- **Core Hardware**: WAGO CC100 (Dual Core Arm Cortex A7)
- **Runtime**: Node-RED (Dockerized / Native Linux environment)
- **UI Framework**: Dashboard 2.0 (Vue 3 Driven)
- **Database**: SQLite 3 (Lightweight local edge storage)
- **Communication**: Modbus TCP / Web API (HTTP/HTTPS)

---

## 📱 Feature Modules

### 1. Web Integration Interface (`WebSite_api`)
This module acts as a unified information gateway, utilizing Vue's reactive data management to toggle between various external web services.
* **WAGO Latest Updates**: Integrated LinkedIn/WAGO feed to keep track of the latest industrial automation trends.
* **Multimedia Integration**: Supports YouTube and TikTok video embedding—ideal for digitalizing maintenance manuals and operator training videos.
* **Dynamic Loading**: Implementation of `iframe` combined with Vue's two-way binding for seamless content switching without page refreshes.

### 2. Data Management & Hardware Control (`HomePage`)
A comprehensive dashboard combining database analytics with real-time hardware manipulation.
* **SQLite Data Center**: 
    * Supports real-time keyword searching and manual data synchronization.
    * Optimized SQL queries tailored for embedded system constraints to ensure high UI responsiveness.
* **Industrial IO Control (Button Section)**:
    * **Real-time Feedback**: Circular LED status indicators are synced with the CC100's physical Digital Outputs (DO_01 ~ DO_04).
    * **Batch Operations**: Includes "All ON" and "All OFF" functionality, utilizing logic nodes to distribute batch Modbus commands efficiently.

---

## 📂 Project Structure
```text
.
├── flows/
│   ├── main_logic.json     # Core Node-RED logic and signal processing
│   └── ui_config.json      # Dashboard 2.0 (Vue) UI configurations
├── db/
│   └── local_storage.db    # SQLite database file
├── assets/
│   └── custom_style.css    # Custom CSS for Dashboard 2.0 components
└── README.md
