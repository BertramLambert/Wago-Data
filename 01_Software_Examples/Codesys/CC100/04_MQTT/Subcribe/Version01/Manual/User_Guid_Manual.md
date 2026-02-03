# User Guide: ModbusTCP_Master Example

> [!TIP]
> **Quick Tags:** > ![Version](https://img.shields.io/badge/Version-V1.0.0-blue) ![Status](https://img.shields.io/badge/Status-Example-yellow) ![Protocol](https://img.shields.io/badge/Protocol-Modbus%20TCP-orange) ![FunctionCode](https://img.shields.io/badge/Function-FC03-red)

---

## 1. 範例概述 (Overview)
本範例展示了如何在 CODESYS 環境中使用 `ModbusFB` 函式庫建立一個基礎的 **Modbus TCP Master (Client)**。程式會持續循環讀取遠端設備的 **Holding Registers (FC03)**，並將資料存儲於本地暫存器中。

---

## 2. 核心組件 (Core Components)

### 程式實體 (Function Blocks)
* **`fbClient`**: `ModbusFB.ClientTCP` - 負責建立與管理 TCP 連線。
* **`fbReadRegs`**: `ModbusFB.ClientRequestReadHoldingRegisters` - 專門執行 **Function Code 03** 的讀取請求。

### 關鍵參數設定 (Key Parameters)
| 變數名稱 | 設定值 | 說明 |
| :--- | :--- | :--- |
| `aDestIP` | `[192, 168, 1, 224]` | 目標 Modbus Slave 設備的 IP 位址。 |
| `uiPort` | `502` | 標準 Modbus TCP 通訊埠。 |
| `uiUnitId` | `1` | Slave ID / Unit ID。 |
| `uiStartItem`| `0` | 起始位址 (40001)。 |
| `uiQuantity` | `10` | 連續讀取的暫存器數量 (WORD)。 |

---

## 3. 實作邏輯說明 (Operational Logic)

本程式分為三個主要步驟執行循環通訊：

### STEP 1: 連線管理
透過 `fbClient` 指定目標 IP 位址。只要 `xConnect` 設定為 `TRUE`，功能塊會自動管理 TCP 連線與重連機制。

### STEP 2: 發送讀取請求 (FC03)
呼叫 `fbReadRegs` 並傳入 `fbClient` 實例。
* **資料指標**: 使用 `ADR(awData)` 將讀取的結果直接寫入 `awData` 陣列中。

### STEP 3: 循環觸發邏輯
程式包含一個自動觸發機制：
1. 當功能塊不在忙碌狀態 (`NOT fbReadRegs.xBusy`) 且執行標籤為 `FALSE` 時，將 `xExecute` 設為 `TRUE` 發起請求。
2. 當讀取完成 (`xDone`) 或通訊發生錯誤 (`xError`) 時，自動將 `xExecute` 設為 `FALSE`。
3. 此邏輯確保了通訊會以最短的間隔連續執行。



---

## 4. 注意事項 (Important Notes)
1. **IP 格式**: 在 `ModbusFB` 中，IP 位址必須以 `ARRAY[0..3] OF BYTE` 格式輸入，不支援字串格式。
2. **記憶體指標**: `pData` 參數必須使用 `ADR()` 取得目標陣列的記憶體位址。
3. **錯誤處理**: 在實際工程中，建議增加超時 (Timeout) 與重試次數的設定以增強穩定性。

---

## 5. 故障排除 (Troubleshooting)
* **連線失敗**: 請檢查電腦與 `192.168.1.224` 是否在同一網段，且設備支援 Port 502。
* **資料未更新**: 確認 `xExecute` 是否有在 `TRUE` 與 `FALSE` 之間切換。
* **錯誤代碼**: 若 `fbReadRegs.xError` 為真，請檢視 `fbReadRegs.udiErrorId` 以取得詳細錯誤資訊。


---
