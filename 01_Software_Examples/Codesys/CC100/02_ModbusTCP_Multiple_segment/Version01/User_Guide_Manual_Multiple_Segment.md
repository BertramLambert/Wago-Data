# User Guide: ModbusTCP_ARRAY Function Block

> [!TIP]
> **Document Information**
> ![Version](https://img.shields.io/badge/Version-V1.0.0-blue) ![Status](https://img.shields.io/badge/Status-Stable-green) ![Protocol](https://img.shields.io/badge/Protocol-Modbus%20TCP-orange) ![FunctionCode](https://img.shields.io/badge/Function-FC03-red)

---

## 📖 目錄 (Table of Contents)
- [User Guide: ModbusTCP\_ARRAY Function Block](#user-guide-modbustcp_array-function-block)
  - [📖 目錄 (Table of Contents)](#-目錄-table-of-contents)
  - [1. 功能概述 (Overview)](#1-功能概述-overview)
  - [2. 系統需求 (Requirements)](#2-系統需求-requirements)
  - [3. 介面定義 (Interface Definition)](#3-介面定義-interface-definition)
    - [📥 輸入參數 (VAR\_INPUT)](#-輸入參數-var_input)
    - [📤 輸出參數 (VAR\_OUTPUT)](#-輸出參數-var_output)
  - [4. 運作邏輯 (Operational Logic)](#4-運作邏輯-operational-logic)
  - [5. 範例配置 (Example Configuration)](#5-範例配置-example-configuration)
  - [6. 故障排除 (Troubleshooting)](#6-故障排除-troubleshooting)

---

## 1. 功能概述 (Overview)
`ModbusTCP_ARRAY` 是一個高效的 PLC 功能塊，專為處理大規模 Modbus TCP 資料採集而設計。它允許使用者透過簡單的陣列配置，同時對多個不同站號 (Unit ID) 或位址段進行循環輪詢。



**核心特點：**
* **資料無縫拼接**：自動將多組分散的暫存器資料整合成連續的 `WORD` 陣列。
* **高容錯機制**：若單一組設備故障或通訊超時，功能塊會自動跳過並繼續下一組任務。
* **狀態透明化**：提供即時的進度字串 (`sDetailStatus`) 與連線狀態燈號。

---

## 2. 系統需求 (Requirements)
* **開發環境**: CODESYS V3.5 或相關相容平台 (如 WAGO e!COCKPIT)。
* **依賴函式庫**: 需安裝並引用 `ModbusFB` 函式庫。
* **支援功能碼**: **FC03** (Read Holding Registers)。

---

## 3. 介面定義 (Interface Definition)

### 📥 輸入參數 (VAR_INPUT)
| 變數名稱 | 數據類型 | 說明 |
| :--- | :--- | :--- |
| `aIPAddr` | `ARRAY[0..3] OF BYTE` | 目標 Slave 設備的 IP 位址。 |
| `uiNumOfGroups` | `UINT` | **總組數**：本次循環要讀取的任務數量 (範圍: 1-20)。 |
| `aUnitID` | `ARRAY[0..19] OF BYTE` | 各任務對應的 Modbus Unit ID (Slave ID)。 |
| `aStartAddr` | `ARRAY[0..19] OF UINT` | 各任務起始位址 (Zero-based)。 |
| `aQuantity` | `ARRAY[0..19] OF UINT` | 各任務讀取長度 (每組上限 125 Words)。 |
| `tTimeout` | `TIME` | 單次 Request 超時設定，預設為 `T#1S`。 |
| `uiMaxRetries` | `UINT` | 單次通訊失敗後的重試次數。 |

### 📤 輸出參數 (VAR_OUTPUT)
| 變數名稱 | 數據類型 | 說明 |
| :--- | :--- | :--- |
| `awResultData` | `ARRAY[0..3999] OF WORD` | **資料總表**：存放所有任務拼接後的讀取結果。 |
| `xIsConnected` | `BOOL` | TCP 連線成功標記。 |
| `xAllOk` | `BOOL` | 當輪輪詢全部成功且無錯誤時觸發。 |
| `xError` | `BOOL` | 當輪輪詢中只要有任一組出現錯誤，此位元即為 TRUE。 |
| `sDetailStatus` | `STRING` | 目前通訊進度描述 (例: "Reading: 3 / 10")。 |

---

## 4. 運作邏輯 (Operational Logic)

本模組內部基於 **有限狀態機 (FSM)** 運作：

1. **Wait Connection (State 0)**：檢測 `xEnable` 後，建立 TCP 連線。
2. **Execute Request (State 10)**：依據 `iPointer` 索引發送 FC03 指令，並將回傳值複製到 `awResultData` 的對應偏移位置。
3. **Switch & Delay (State 20)**：執行 20ms 的間隔延遲以釋放通訊頻寬，隨後切換至下一個任務索引。



---

## 5. 範例配置 (Example Configuration)

假設需讀取以下兩段位址：
1. **任務 0**: 讀取 Addr 0 開始的 10 個 Word。
2. **任務 1**: 讀取 Addr 100 開始的 5 個 Word。

**配置：**
- `uiNumOfGroups := 2;`
- `aStartAddr[0] := 0; aQuantity[0] := 10;`
- `aStartAddr[1] := 100; aQuantity[1] := 5;`

**資料結果 (awResultData)：**
- `Index [0..9]`：存放任務 0 的 10 筆資料。
- `Index [10..14]`：存放任務 1 的 5 筆資料。

---

## 6. 故障排除 (Troubleshooting)

| 錯誤現象 | 可能原因 | 排除步驟 |
| :--- | :--- | :--- |
| `xIsConnected` 為 FALSE | IP 不通或 Port 502 被占用 | 檢查實體線路並嘗試 Ping 設備。 |
| `xError` 燈號常亮 | 某組 Unit ID 不正確或位址不存在 | 觀察 `sDetailStatus` 確認出錯的組別。 |
| 數值位移 1 個單位 | Modbus 0-based 與 1-based 差異 | 將 `aStartAddr` 進行 -1 或 +1 修正。 |

---