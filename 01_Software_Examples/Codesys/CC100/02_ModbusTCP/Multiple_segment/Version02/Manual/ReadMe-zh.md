# ModbusTCP_ARRAY POU Documentation

> [!TIP]
> **語言切換 / Language Switch:**
> [中文版 (Chinese)](./ReadMe-zh.md) | [English Version](./ReadMe.md)

---

<a name="中文版"></a>

# [中文版] ModbusTCP_ARRAY 輪詢功能塊說明

## 1. 功能概述
`ModbusTCP_ARRAY` 是一個專為 PLC 設計的高彈性通訊功能塊。它允許使用者透過陣列設定，在單一連線中自動循環讀取多組不同類型（Function Code）的 Modbus 資料。

### 核心特色
* **動態 FC 切換**：同一連線可混合讀取 Coils (FC1), Discrete Inputs (FC2), Holding Registers (FC3), Input Registers (FC4)。
* **自動化連線管理**：支援 `xEnable` 啟動與斷線自動重連機制。
* **無縫資料拼接**：自動計算位移（Offset），將不同組別的結果依序儲存在連續的 `awResultData` 總表中。
* **診斷透明化**：內建狀態字串與詳細進度顯示。

## 2. 參數說明
| 參數名稱 | 資料類型 | 說明 |
| :--- | :--- | :--- |
| `aIPAddr` | ARRAY[0..3] OF BYTE | 設備 IP 位址 (例如: `[192, 168, 1, 10]`) |
| `xEnable` | BOOL | TRUE: 啟動讀取; FALSE: 停止通訊並重置 |
| `aFunctionCode` | ARRAY[0..19] OF UINT | **1**:FC1, **2**:FC2, **3**:FC3, **4**:FC4 |
| `awResultData` | ARRAY[0..3999] OF WORD | 最終結果總表 (資料按輪詢順序自動拼接) |

## 3. 實作範例
```pascal
MyPoller(
    aIPAddr       := [192, 168, 1, 224],
    xEnable       := TRUE,
    uiNumOfGroups := 3,
    aFunctionCode := arrFC, // 例如 [3, 4, 1, ...]
    awResultData  => FinalData
);
