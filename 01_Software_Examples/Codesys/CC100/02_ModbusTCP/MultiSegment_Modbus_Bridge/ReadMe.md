# User Guide: MultiSegment_Modbus_Bridge (Data Bridge Mode)

> [!TIP]
> **Technical Document Info:**
> ![Device](https://img.shields.io/badge/Device-WAGO%20CC100--751--9301-ee0000) ![Feature](https://img.shields.io/badge/Feature-Dual--Network--Bridge-blue) ![Protocol](https://img.shields.io/badge/Protocol-Modbus%20TCP-orange) ![Status](https://img.shields.io/badge/Status-Implemented-brightgreen)

---

## 📖 目錄 (Table of Contents)
1. [專案核心架構 (Core Architecture)](#1-專案核心架構-core-architecture)
2. [硬體配置：雙網口獨立設定 (Dual Port Setup)](#2-硬體配置雙網口獨立設定-dual-port-setup)
3. [程式邏輯：填表式資料轉發 (Table-Driven Logic)](#3-程式邏輯填表式資料轉發-table-driven-logic)
4. [資料映射與彙整 (Data Mapping)](#4-資料映射與彙整-data-mapping)
5. [故障排除與維修 (Troubleshooting)](#5-故障排除與維修-troubleshooting)

---

## 1. 專案核心架構 (Core Architecture)
本專案將 **WAGO CC100** 定義為數據中繼橋接器。利用其雙乙太網路孔的特性，達成跨網段的資料採集與同步：

* **來源端 (Field Segment)**：透過第一個網孔與現場設備通訊，讀取原始數據。
* **數據中轉 (PLC Logic)**：在程式內部建立緩衝表（Array），對資料進行清洗與排版。
* **目標端 (Host Segment)**：將整理後的緩衝表透過第二個網孔寫入至另一台 PLC。



---

## 2. 硬體配置：雙網口獨立設定 (Dual Port Setup)

為了達成物理隔離與跨網段傳輸，需在 **WAGO Web-Based Management (WBM)** 與 **CODESYS 裝置樹** 進行以下配置：

### 🌐 網路埠分配
* **Ethernet (Port 1)**: 連接現場 Modbus TCP Slave 設備（例如：感測器、流量計）。
* **Ethernet_1 (Port 2)**: 連接上層系統或其他 PLC 站點。

### ⚙️ 設定重點
1.  **IP 分配**: 確保兩個網孔位於不同的子網段（Subnet），避免路由衝突。
2.  **Modbus Master 掛載**: 在 CODESYS 的 `Devices` 樹狀圖中，將採集用的 Master 掛在第一個網孔，轉發用的 Master 掛在第二個網孔。



---

## 3. 程式邏輯：填表式資料轉發 (Table-Driven Logic)

本程式的核心在於 **「填表 (Mapping)」**，而非單純的透明傳輸。

### 執行步驟：
1.  **分散採集**: 透過多個 Modbus 讀取任務，將資料分別存入本地變數（如 `wTemp_01`, `wHumi_02`）。
2.  **資料彙整**: 使用程式邏輯（如 `FOR` 迴圈或直接賦值）將這些分散變數寫入二維陣列 `aLogData`。
3.  **批量發送**: 呼叫寫入功能塊，將整份 `aLogData` 表單一次性寫入目標 PLC 的指定位址。

---

## 4. 資料映射與彙整 (Data Mapping)

二維陣列（Table）的設計邏輯確保了資料在傳輸過程中的整潔性：

| 陣列索引 (Index) | Column 0 (來源網段 A) | Column 1 (來源網段 B) |
| :---: | :--- | :--- |
| **0** | 溫度感測器 01 | 濕度感測器 01 |
| **1** | 溫度感測器 02 | 濕度感測器 02 |
| **...** | ... | ... |
| **9** | 第 10 組採集數據 | 第 10 組採集數據 |

---

## 5. 故障排除與維修 (Troubleshooting)

| 現象 | 可能原因 | 檢查項目 |
| :--- | :--- | :--- |
| **目標 PLC 沒收到資料** | 網孔 2 的 IP 設定錯誤或 Gateway 不通 | 檢查 WBM 中 Ethernet_1 的設定與 Ping 狀態。 |
| **資料順序錯誤** | 填表迴圈指標 `i` 邏輯有誤 | 檢查 `PLC_PRG` 中對 `aLogData` 的賦值順序。 |
| **通訊延遲高** | 兩網段同時讀寫頻率過快 | 建議增加任務間的間隔時間 (Gap Time)。 |
