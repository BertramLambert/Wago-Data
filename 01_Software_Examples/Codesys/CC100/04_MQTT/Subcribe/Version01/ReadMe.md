# User Guide: WAGO MQTT Connectivity & Subscriber Implementation

> [!TIP]
> **Technical Document Info:**
> ![Platform](https://img.shields.io/badge/Platform-WAGO%20PFC-ee0000) ![Protocol](https://img.shields.io/badge/Protocol-MQTT-blue) ![Library](https://img.shields.io/badge/Library-WagoAppCloud-green) ![Status](https://img.shields.io/badge/Status-Functional-brightgreen)

---

## 📖 目錄 (Table of Contents)
- [User Guide: WAGO MQTT Connectivity \& Subscriber Implementation](#user-guide-wago-mqtt-connectivity--subscriber-implementation)
  - [📖 目錄 (Table of Contents)](#-目錄-table-of-contents)
  - [1. WBM 網頁連線配置 (Hardware Setup)](#1-wbm-網頁連線配置-hardware-setup)
    - [配置步驟：](#配置步驟)
  - [2. 功能塊說明 (fbMqtt\_Subscriber)](#2-功能塊說明-fbmqtt_subscriber)
    - [核心邏輯架構：](#核心邏輯架構)
    - [介面定義：](#介面定義)
  - [3. 主程式實作 (PLC\_PRG Logic)](#3-主程式實作-plc_prg-logic)
- [資料彙整流程：](#資料彙整流程)
- [資料紀錄表結構 (Data Logging)](#資料紀錄表結構-data-logging)

---

## 1. WBM 網頁連線配置 (Hardware Setup)

在啟動 PLC 程式前，必須先透過 **WAGO Web-Based Management (WBM)** 完成 MQTT Broker 的基礎連線設定。

### 配置步驟：
1. 登入 WBM 頁面，導航至：**Cloud Connectivity** > **Connection 1**。
2. 切換至 **Configuration** 分頁。
3. **關鍵參數設定**（參考下表）：

| 欄位名稱 | 設定值 (範例) | 說明 |
| :--- | :--- | :--- |
| **Enabled** | ☑️ (勾選) | 啟用此路 MQTT 連線。 |
| **Cloud platform** | `MQTT AnyCloud` | 使用通用 MQTT 協議。 |
| **Hostname** | `192.168.1.224` | MQTT Broker 的 IP 位址。 |
| **Port number** | `1883` | 標準 MQTT 通訊埠。 |
| **Client ID** | `Wago750-9301` | 設備於 Broker 上的唯一識別碼。 |



---

## 2. 功能塊說明 (fbMqtt_Subscriber)

此功能塊封裝了 `WagoAppCloud.FbSubscribeMQTT`，實現了主題訂閱與歷史訊息的自動緩衝。

### 核心邏輯架構：
* **動態訂閱**：透過 `sTopicName` 輸入參數，實現不同實例訂閱不同主題。
* **Byte 轉 String 處理**：利用 `MemCopySecure` 將接收到的原始 Byte 陣列轉換為可讀的字串格式。
* **指標循環紀錄 (Ring Buffer)**：內建 `pIdx` 變數，當收到訊息時，會將訊息存入 `aHistoryRef` 陣列，並以 10 筆為上限自動循環覆蓋。

### 介面定義：
* **VAR_INPUT**: `sTopicName` (訂閱主題)。
* **VAR_IN_OUT**: `aHistoryRef` (外部陣列引用，確保資料能直接回傳至主程式)。

---

## 3. 主程式實作 (PLC_PRG Logic)

在主程式中，我們實例化了兩組訂閱器，分別監控溫度與濕度感測器。

```pascal
// 呼叫訂閱實例並傳入主題與儲存陣列
fbSub_Temp(sTopicName := '/sensor/temp', aHistoryRef := aHist_Temp);
fbSub_Hum(sTopicName := '/sensor/hum', aHistoryRef := aHist_Hum);

# 資料彙整流程：

主程式透過一個 FOR 迴圈，即時將兩個獨立的歷史紀錄陣列（aHist_Temp 與 aHist_Hum）彙整至一個二維陣列 aLogData 中，建立結構化的資料紀錄表。

# 資料紀錄表結構 (Data Logging)
彙整後的二維陣列 aLogData 結構如下，方便 HMI 或上層系統直接存取：索引 (i),Column 0 (溫度歷史),Column 1 (濕度歷史)
0,aHist_Temp[0],aHist_Hum[0]
1,aHist_Temp[1],aHist_Hum[1]
...,...,...
9,aHist_Temp[9],aHist_Hum[9]
