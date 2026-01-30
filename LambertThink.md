# Wago-Data
🌐 [English Version](./ReadMe.md) | [繁體中文版本](./ReadMe-zh.md)

本儲存庫提供 **WAGO** 相關軟體範例與技術操作手冊，旨在幫助使用者快速上手工業自動化、邊緣運算、分散式叢集以及未來的 AI 智能化任務。

📖 **[LambertThink](./LambertThink.md)**: 深入了解本專案背後的開發思維與架構哲學。

---

## 📂 內容概覽

- **軟體範例**: 包含 [Codesys](#codesys-範例)、[Python](#python-範例) 與 [Node-RED](#node-red-範例)。
- **系統架構範例**: 涵蓋進階的 [邊緣伺服器叢集 (Edge Swarm)](#-邊緣伺服器叢集-edge-server-swarm)。
- **控制器操作手冊**: 涵蓋 [CC100](#cc100-控制器)、[BC100](#bc100-控制器) 與 [PFC200](#pfc200-控制器) 的硬體指南。
- **環境設定**: 包含 [Docker](#-docker-操作)、[路由器](#-路由器-操作) 配置以及運行環境設定。

---

## 🛠 軟體範例

### Codesys 範例
- **SQLite 整合**: 示範如何在 Codesys Runtime 內直接建立與管理本地資料庫。
- **Modbus TCP 通訊**: 實現跨網域 (Cross-Domain) 與經由網關 (Gateway) 的數據讀寫實作。
- **MQTT 發佈/訂閱**: 實現控制器與雲端 Broker 之間的即時數據交換與指令控制。
- **OPC UA Server**: 將 I/O 訊號開放給 SCADA 或 HMI 系統進行標準化即時監控。

### Python 範例
- **網頁儀表板 (Web HMI)**: 使用 Flask 與 Vue.js 開發自定義的視覺化監控介面與 API。

### Node-RED 範例
- **Discord Bot 整合**: 實現聊天指令控制與硬體報警即時推播。
- **邊緣排程自動化 (Edge-Schedule)**: 獨立於 PLC 之外的彈性排程管理系統。
- **SQLite 資料記錄器**: 確保數據在地端的持久化儲存與歷史查詢能力。
- **通訊協議閘道器**: 橋接工業協議 (OT) 與 IT 標準 (JSON/REST API)。
- **互動式網頁儀表板**: 提供低代碼、高效率的即時監控 Web 介面。

---

## 🌐 邊緣伺服器叢集 (Edge Server Swarm)
*此部分展示如何將多台 WAGO 控制器整合為具備高可用性的分散式運算叢集。*

- **Docker Swarm 管理**: 叢集初始化、節點加入及跨控制器服務編排。
- **服務高可用性 (HA)**: 當單一節點故障時，自動遷移容器服務以維持系統運作。
- **虛擬網域佈署**: 透過 Overlay Network 實現跨硬體的容器通訊。

---

## 🗺 未來展望 (Roadmap)

- [x] **單機控制與數據整合 (Done)**: 已完成 Codesys, Python 與 Node-RED 基本模組。
- [ ] **邊緣伺服器叢集 (In Progress)**: 實現多控制器的高可用性與分散式運算。
- [ ] **雲端與混合架構 (Planned)**: 串接免費雲端服務 (Google Sheets, Adafruit IO) 與 VPN 私有雲。
- [ ] **工業人工智慧 (Industrial AI)**: 
  - **預測性維護**: 利用歷史數據模型預警設備故障。
  - **邊緣視覺 (Edge Vision)**: 整合 OpenCV/YOLO 進行自動化品質檢測與計數。

---

## 🏗 硬體規格與環境設定
*詳細內容請參閱目錄中 02_Controller_Operation_Manuals 與 03_Environment_Setup*

*最後更新日期: 2026/1/30*
