# Wago-Data

本儲存庫提供 **WAGO** 相關軟體範例與技術操作手冊，旨在幫助使用者快速上手工業自動化與邊緣運算任務。

---

## 📂 內容概覽

- **軟體範例**: 包含 [Codesys](#codesys-範例)、[Python](#python-範例) 與 [Node-RED](#node-red-範例)。
- **控制器操作手冊**: 涵蓋 [CC100](#cc100-控制器)、[BC100](#bc100-控制器) 與 [PFC200](#pfc200-控制器) 的硬體專屬指南。
- **環境設定**: 包含 [Docker](#docker-操作)、L2 Switch 配置以及控制器運行環境 (Runtime) 設定。

---

## 🛠 軟體範例

### Codesys 範例
- **SQLite 整合**: 示範如何在 Codesys Runtime 內直接建立與管理本地資料庫。
- **Modbus TCP 通訊**: 實現跨網域 (Cross-Domain) 與經由網關 (Gateway) 的數據讀寫實作。
- **MQTT-發佈 (Publish)**: 將控制器數據（感測器數值/設備狀態）傳送至 MQTT Broker（如 Mosquitto, Azure IoT Hub）。
- **MQTT-訂閱 (Subscribe)**: 接收來自 Broker 的遠端指令或配置，藉此控制硬體輸出輸出。

### Python 範例
- **網頁儀表板 (Web HMI)**: 使用 **Flask** 作為後端 API，並搭配 **Vue.js/HTML** 前端開發自定義的視覺化監控介面。

### Node-RED 範例
- **Webhook & WebSocket**: 實現即時數據交換與第三方 API 服務整合。
- **Discord Bot 整合**: 
  - **互動式指令**: 透過 Discord 聊天頻道遠端下達指令給 WAGO 控制器。
  - **狀態通知**: 當硬體發生警報或特定事件時，即時推播訊息至 Discord 頻道。

---

## 🐳 Docker 操作
*針對在 WAGO 控制器上運行 Docker 容器的具體步驟、鏡像管理與資源分配的最佳實踐。*

---

## 🏗 硬體控制器規格

### CC100 控制器
- **751-9301** (Compact Controller 100)
- **751-9401**

### BC100 控制器
- **750-8001**

### PFC200 控制器
- **750-8212** (PFC200 第二代)

---
*最後更新日期: 2026*
