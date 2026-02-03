# ModbusTCP_ARRAY 功能塊說明書

> [!TIP]
> **標籤：** ![Modbus](https://img.shields.io/badge/Protocol-Modbus%20TCP-blue) ![FC03](https://img.shields.io/badge/Function-FC03-orange) ![Platform](https://img.shields.io/badge/Platform-CODESYS-green)

---
## 1. 概述
`ModbusTCP_ARRAY` 是一個專為 CODESYS 環境設計的 Modbus TCP 輪詢工具。它支援**多組（最多 20 組）**連續位址的讀取，並能將所有讀取到的資料無縫拼接（Seamless Join）到一個總表中，方便人機介面（HMI）或上層系統一次性調取資料。

---

## 2. 主要功能
* **動態組數配置**：可透過 `uiNumOfGroups` 決定要輪詢的組數。
* **自動重連機制**：當網路中斷時，功能塊會自動嘗試重連，無需人工干預。
* **異常跳過功能**：若其中一組設備通訊失敗，系統會記錄錯誤並自動跳過，繼續執行下一組，確保整體輪詢不卡死。
* **資料自動拼接**：將不同 Unit ID 或不同起始位址的資料，依序存入 `awResultData` 總表。

---

## 3. 參數說明

### 輸入參數 (VAR_INPUT)
| 變數名稱 | 類型 | 說明 |
| :--- | :--- | :--- |
| `aIPAddr` | `ARRAY[0..3] OF BYTE` | 目標設備的 IP 位址 (例如: `[192, 168, 1, 10]`) |
| `uiPort` | `UINT` | Modbus 通訊埠，預設為 `502` |
| `xEnable` | `BOOL` | 啟動輪詢。為 `FALSE` 時重置所有狀態 |
| `uiNumOfGroups` | `UINT` | 本次要輪詢的總組數 (範圍: 1~20) |
| `aUnitID` | `ARRAY[0..19] OF BYTE` | 每組對應的 Unit ID (Slave ID) |
| `aStartAddr` | `ARRAY[0..19] OF UINT` | 每組對應的 Modbus 起始通訊位址 |
| `aQuantity` | `ARRAY[0..19] OF UINT` | 每組要讀取的長度 (WORD 數量) |
| `tTimeout` | `TIME` | 單次請求的超時時間，預設 `T#1S` |
| `uiMaxRetries` | `UINT` | 單次通訊失敗後的重試次數 |

### 輸出參數 (VAR_OUTPUT)
| 變數名稱 | 類型 | 說明 |
| :--- | :--- | :--- |
| `awResultData` | `ARRAY[0..3999] OF WORD` | **最終資料表**。所有讀取到的值會依序拼接到此處 |
| `xError` | `BOOL` | 只要當輪有一組以上出錯，此燈號會亮起 |
| `xAllOk` | `BOOL` | 當輪**所有**組別都成功讀取時，此燈號才會亮起 |
| `xIsConnected` | `BOOL` | 目前 TCP 連線狀態 |
| `sDetailStatus` | `STRING` | 顯示目前的讀取進度 (例如: "Reading: 3 / 10") |

---

## 4. 運作邏輯

### 狀態機流程 (State Machine)
1.  **State 0 (Waiting)**：檢查連線狀態。
2.  **State 10 (Request)**：
    * 使用 **FC03 (Read Holding Registers)** 發送請求。
    * 成功：將 `awBuffer` 的值複製到 `awResultData` 的對應偏移位置。
    * 失敗：記錄該輪錯誤並跳轉。
3.  **State 20 (Switch)**：
    * 延遲 20ms 以釋放通訊頻寬。
    * 若為最後一組，則結算 `xAllOk` 並重置位址偏移量，回到第一組。



### 資料拼接機制範例
假設配置 2 組讀取：
1.  **Group 0**: UnitID 1, Addr 100, Qty 10
2.  **Group 1**: UnitID 2, Addr 50, Qty 5

**awResultData 分佈：**
* `Index [0..9]`：存儲 Group 0 的資料。
* `Index [10..14]`：存儲 Group 1 的資料。

---

## 5. 注意事項
> [!IMPORTANT]
> 1. **FC 限制**：目前版本固定使用 **FC03**。若需 FC04，需修改內部 Request FB 類型。
> 2. **單組上限**：Modbus 標準限制單次讀取上限為 **125 個 WORD**。
> 3. **總表上限**：請確保所有組別的 `aQuantity` 總和不超過 **4000**，否則會發生陣列越界。
