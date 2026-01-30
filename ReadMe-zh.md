# Wago-Data
🌐 [English Version](./ReadMe.md) | [繁體中文版本](./ReadMe-zh.md)

本儲存庫提供 **WAGO** 相關軟體範例與技術操作手冊，旨在幫助使用者快速上手工業自動化、邊緣運算以及分散式叢集任務。

---

## 📂 內容概覽

- **軟體範例**: 包含 [Codesys](#codesys-範例)、[Python](#python-範例) 與 [Node-RED](#node-red-範例)。
- **系統架構範例**: 涵蓋進階的 [邊緣伺服器叢集 (Edge Swarm)](#-邊緣伺服器叢集-edge-server-swarm)。
- **控制器操作手冊**: 涵蓋 [CC100](#cc100-控制器)、[BC100](#bc100-控制器) 與 [PFC200](#pfc200-控制器) 的硬體專屬指南。
- **環境設定**: 包含 [Docker](#-docker-操作)、[路由器](#-路由器-操作) 配置以及控制器運行環境 (Runtime) 設定。

---

## 🛠 軟體範例

### Codesys 範例
- **SQLite 整合**: 示範如何在 Codesys Runtime 內直接建立與管理本地資料庫。
- **Modbus TCP 通訊**: 實現跨網域 (Cross-Domain) 與經由網關 (Gateway) 的數據讀寫實作。
- **MQTT-發佈 (Publish)**: 將控制器數據（感測器數值/設備狀態）傳送至 MQTT Broker（如 Mosquitto, Azure IoT Hub）。
- **MQTT-訂閱 (Subscribe)**: 接收來自 Broker 的遠端指令或配置，藉此控制硬體輸出。
- **OPC UA Server**: 使控制器具備伺服器功能，透過標準化協定將 I/O 訊號與變數開放給 SCADA 或 HMI 系統進行即時監控與控制。

### Python 範例
- **網頁儀表板 (Web HMI)**: 使用 **Flask** 作為後端 API，並搭配 **Vue.js/HTML** 前端開發自定義的視覺化監控介面。

### Node-RED 範例
- **Webhook 整合**: 接收並處理來自外部雲端服務或第三方 API 的 HTTP 請求。
- **WebSocket 通訊**: 實現即時儀表板與低延遲控制的雙向數據交換。
- **Discord Bot 整合**: 
  - **互動式指令**: 透過 Discord 聊天指令遠端控制 WAGO 控制器。
  - **狀態通知**: 將硬體警報與事件日誌即時推播至 Discord 頻道。
- **邊緣排程自動化系統 (Edge-Schedule System)**:
  - **定時自動化**: 利用 Node-RED 處理複雜的時間邏輯（如 Cron Job），獨立於 PLC 主程式之外控制硬體輸出。
  - **營運靈活性**: 使用者可透過視覺化界面快速調整排程，無需重新燒錄控制器程式。
- **SQLite 資料記錄器 (SQLite DataLogger)**:
  - **本地持久化儲存**: 將關鍵運作數據存入控制器內部的 SQLite 資料庫，確保數據長期追蹤與斷網時的資料完整性。
  - **歷史數據查詢**: 讓使用者具備直接從控制器存儲空間中，檢索過去事件或趨勢記錄的能力。
- **通訊協議閘道器 (Protocol Gateway)**:
  - **IT/OT 技術融合**: 橋接工業協定（Modbus, OPC UA）與 IT 標準（MQTT, RESTful API, JSON）。
  - **跨平台互操作性**: 實現不同廠牌自動化硬體與雲端服務之間，無縫且即時的數據交換。
- **互動式儀表板 (Web HMI)**:
  - **即時監控**: 透過儀表與圖表將感測器數據與系統狀態視覺化。
  - **遠端控制**: 直接從網頁瀏覽器或行動裝置切換數位輸出或調整設定值（Setpoints）。
    
---

## 🌐 邊緣伺服器叢集 (Edge Server Swarm)
*此部分為進階議題，展示如何將多台 WAGO 控制器整合為分散式運算叢集。*

- **Docker Swarm 叢集管理**: 
  - **叢集建立**: 展示如何將多台控制器初始化並組合成 Manager 與 Worker 節點。
  - **服務編排 (Orchestration)**: 使用 Docker Stack 實現跨節點的自動化服務部署與負載平衡。
- **高可用性與容錯 (HA)**: 
  - 實驗當單一節點離線時，Container 服務自動轉移與復原的機制。
- **跨節點虛擬網路 (Overlay Network)**: 
  - 建立安全的跨控制器內部網路，使不同節點間的數據交換不受實體網域限制。

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

## 📶 路由器 操作

*最後更新日期: 2026/1/30*
