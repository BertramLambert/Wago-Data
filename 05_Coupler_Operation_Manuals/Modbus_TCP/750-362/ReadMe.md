# 技術手冊：WAGO 750-362 Modbus TCP Coupler 底層通訊與狀態解析

> [!IMPORTANT]
> **文件資訊：**
> ![Device](https://img.shields.io/badge/Device-WAGO%20750--362-ee0000) ![Protocol](https://img.shields.io/badge/Protocol-Modbus%20TCP-orange) ![Function](https://img.shields.io/badge/Focus-Low--Level%20Diagnostics-blue)

> [Hackmd參考文件](https://hackmd.io/@rLkw7TiWQemz2Qv-71l4PA/rk_iiopSWx)
---

## 📖 目錄 (Table of Contents)
1. [通訊狀態對應表 (Status Codes)](#1-通訊狀態對應表-status-codes)
2. [暫存器封包結構解析 (Register Structure)](#2-暫存器封包結構解析-register-structure)
3. [Modbus RTU over TCP 封包範例](#3-modbus-rtu-over-tcp-封包範例)
4. [WBM 雲端連線配置 (MQTT Bridge 參考)](#4-wbm-雲端連線配置-mqtt-bridge-參考)
5. [故障排除說明](#5-故障排除說明)

---

## 1. 通訊狀態對應表 (Status Codes)

在監測 750-362 的通訊過程時，Master 端的命令與 Slave 端的回應數值關係如下表：

| 下命令 (Request) | 狀態回應 (Response) | 說明 (Description) |
| :--- | :--- | :--- |
| **0X0216** | **0X0804** | **初始化 (Initialization)**：模組正在進行內部掃描與配置。 |
| **0X0108** | **0X0800** | **通訊待機 (Standby)**：系統已就緒，等待 Master 請求。 |
| **0X0103** | **0X0813** | **取得回應 (Acknowledge)**：Slave 已確認收到正確請求。 |
| **0X0108** | **0X0918** | **取得數據 (Data Received)**：資料已成功讀取並準備傳輸。 |

---

## 2. 暫存器封包結構解析 (Register Structure)

針對位址 **40513 ~ 40517**，其內部數據與實體 Modbus 封包欄位的對應關係如下：

| 暫存器 (Addr) | 高位字節 (HI) | 低位字節 (LO) | 欄位說明 (Field Description) |
| :---: | :---: | :---: | :--- |
| **40513** | **C1** | **C0** | **通訊命令碼**：定義當前傳輸的動作類型。 |
| **40514** | **D1** | **D0** | **功能碼 / 站號**：如 `03 01` 代表功能碼 03 且站號為 1。 |
| **40515** | **D3** | **D2** | **通訊起始位置**：目標暫存器的起始地址。 |
| **40516** | **D5** | **D4** | **通訊數量**：請求讀取或寫入的寄存器總數。 |
| **40517** | **D7** | **D6** | **CRC 校驗碼**：包含 CRC-High 與 CRC-Low。 |



---

## 3. Modbus RTU/TCP 封包範例

以下為對照表中顯示的實際數據流範例（以 40513-40517 橫向排列）：

| 40513 (C1/C0) | 40514 (D1/D0) | 40515 (D3/D2) | 40516 (D5/D4) | 40517 (D7/D6) | 解析說明 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `01 03` | `03 01` | `00 00` | `01 00` | `0A 84` | 站號 1, 讀取 Addr 0, 數量 1, CRC 0A84 |
| `01 03` | `03 01` | `00 00` | `02 00` | `0B C4` | 站號 1, 讀取 Addr 0, 數量 2, CRC 0BC4 |
| `01 03` | `03 01` | `00 00` | `03 00` | `CB 05` | 站號 1, 讀取 Addr 0, 數量 3, CRC CB05 |

---

## 4. WBM 雲端連線配置 (MQTT Bridge 參考)

若將 750-362 讀取的資料透過網關（如 CC100）轉發至雲端，其 WBM 配置如下：

* **Cloud Platform**: `MQTT AnyCloud`
* **Hostname**: 填入 Broker IP（如 `192.168.1.224`）
* **Port**: `1883`
* **Client ID**: 設備識別碼（如 `Wago750-9301`）



---

## 5. 故障排除說明

* **CRC 錯誤 (D7/D6)**：若 CRC 碼不符合封包內容，請檢查通訊電纜是否存在電磁干擾或終端電阻是否匹配。
* **狀態停滯於 0X0804**：代表 750-362 正在初始化後端 I/O 模組，若持續太久，請檢查模組排列順序或末端蓋 (End Module) 是否安裝。
* **站號錯誤 (D0)**：確保 Master 發送的 Unit ID 與 750-362 網頁設定的實體 ID 一致。

---
> **本文檔根據 750-362 實作封包截圖進行編寫，用於底層協議開發參考。**
