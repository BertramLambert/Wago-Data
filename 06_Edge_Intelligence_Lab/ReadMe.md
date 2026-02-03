# 🤖 06_Edge_Intelligence_Lab

[中文版 (Chinese Version)](./ReadMe-zh.md)

> [!IMPORTANT]
> **Core Objective**: To explore the architectural integration of Industrial Controllers and Artificial Intelligence (AI).
> **Scope**: Covers Cloud LLM API integration, On-premise private LLM deployment, and the "Train on Cloud, Inference at Edge" paradigm.

---

## 📖 Theoretical Framework

### 1. Hybrid Industrial AI Architecture
In the Industry 4.0 landscape, we adopt a "Cloud-Edge Collaboration" strategy to balance computational power with data privacy:
* **Cloud-Based AI**: Leveraging the massive compute of **Gemini** or **ChatGPT** for complex reasoning, code generation, and technical documentation synthesis.
* **Edge-Based AI**: Deploying private models via **Ollama** or executing **TinyML** directly on controllers for high latency sensitivity and data sovereignty.

### 2. The Edge Inference Lifecycle: Train on Cloud, Deploy at Edge
1. **Data Acquisition**: Collecting real-time sensor data and machine states via edge gateways.
2. **Cloud Training**: Training robust models (e.g., Anomaly Detection) in high-performance GPU environments.
3. **Model Optimization**: Quantizing models into edge-compatible formats such as **ONNX** or **TensorFlow Lite**.
4. **Real-Time Inference**: Running inference engines within the embedded environment for localized diagnostics.

---

## 🛠️ Practical Implementation Examples

### A. Cloud AI Integration (LLM Bridge)
* **LLM Diagnostic Assistant**: Sending hex-based error codes to AI for automated maintenance recommendations.
* **Code Optimization**: Automated PLC code refactoring suggestions based on industrial best practices.
* **Path**: `01_Cloud_API/cloud_llm_bridge.py`

### B. On-Premise LLM (Private AI via Ollama)
* **Local RAG**: Integrating equipment manuals to allow personnel to query register definitions using natural language without cloud access.
* **Path**: `02_Ollama_Local/local_ai_service.py`

### C. Edge Model Deployment (Offline Inference)
* **Use Cases**: Vibration spectrum analysis and current signature anomaly detection.
* **Path**: `03_Edge_Inference/edge_engine.py`

---

## 📂 Folder Structure
* `01_Cloud_API/`: Cloud LLM integration scripts and Prompt Engineering templates.
* `02_Ollama_Local/`: Communication logic with local private AI servers.
* `03_Edge_Inference/`: Compressed lightweight models and edge inference scripts.
* `04_AI_Theory/`: Documentation on AI-assisted development and Human-AI collaboration.

---
> **LambertThink x Edge Intelligence Lab**
