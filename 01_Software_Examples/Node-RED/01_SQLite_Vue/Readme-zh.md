# 🚀 WAGO CC100 IIoT Dashboard

[中文](Readme-zh.md)  | [English](Readme.md)

這是一個基於 **WAGO CC100 (751-9301)** 工業控制器的 Web 整合監控系統。透過 **Node-RED Dashboard 2.0** 與 **Vue.js** 技術棧，將工業現場的實體 IO 控制與現代化的 Web 服務（SQLite、Social Media API）進行深度整合。

## 🛠 技術架構
- **核心硬體**: WAGO CC100 (Dual Core Arm Cortex A7)
- **環境**: Node-RED (Dockerized / Native)
- **UI 框架**: Dashboard 2.0 (Vue 3 驅動)
- **資料庫**: SQLite 3 (本地端輕量化存儲)
- **通訊協議**: Modbus TCP / Web API (HTTP)

---

## 📱 畫面功能說明

### 1. Web 整合介面 (WebSite_api)
此模組實現了多平台資訊的統一入口，透過 Vue 的響應式資料管理，讓 CC100 成為一個強大的資訊閘道器。
* **WAGO 貼文**: 整合 LinkedIn/WAGO 官網動態，獲取最新技術趨勢。
* **多媒體整合**: 支援 YouTube 與 TikTok 影片嵌入，可用於設備維護手冊影片化。
* **動態載入**: 使用 `iframe` 結合 Vue 的雙向綁定，達成無刷新切換視窗。

### 2. 資料管理與實體控制 (HomePage)
結合了數據庫分析與實時硬體操作的監控面板。
* **SQLite 數據查詢**: 
    * 支援即時關鍵字搜尋與資料更新功能。
    * 優化 SQL 查詢語法，確保在嵌入式系統資源下保有流暢的 UI 反應。
* **IO 實體控制區 (Button Section)**:
    * **即時反饋**: 圓形 LED 狀態燈與 CC100 實體數位輸出 (DO_01 ~ DO_04) 狀態同步。
    * **批次操作**: 提供「全開/全關」按鈕，透過 Logic Node 處理批次 Modbus 指令分發。

---

## 📂 專案結構
```text
.
├── flows/
│   ├── main_logic.json     # Node-RED 主要邏輯流程
│   └── ui_config.json      # Dashboard 2.0 (Vue) UI 配置
├── db/
│   └── local_storage.db    # SQLite 資料庫文件
├── assets/
│   └── custom_style.css    # 針對 Dashboard 2.0 的自定義樣式
└── README.md
