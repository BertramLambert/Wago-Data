# ModbusTCP_ARRAY Polling Function Block Documentation

## 1. Functional Overview
`ModbusTCP_ARRAY` is a high-flexibility communication Function Block (FB) designed for industrial PLCs. It allows users to automatically poll multiple data groups with different **Function Codes (FC)** over a single TCP connection using array-based configurations.

### Key Features
* **Dynamic FC Switching**: Mix and match Coils (FC1), Discrete Inputs (FC2), Holding Registers (FC3), and Input Registers (FC4) within a single polling cycle.
* **Automatic Connection Management**: Supports `xEnable` for control and includes an automatic retry mechanism for TCP disconnections.
* **Seamless Data Splicing**: Automatically calculates offsets to store results from different groups into a contiguous `awResultData` master array.
* **Transparent Diagnostics**: Built-in `sStatus` and `sDetailStatus` provide real-time feedback on polling progress for HMI monitoring.

---

## 2. Parameter Description

### 2.1 Inputs (VAR_INPUT)
| Parameter | Data Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `aIPAddr` | ARRAY[0..3] OF BYTE | - | Device IP Address (e.g., `[192, 168, 1, 10]`) |
| `uiPort` | UINT | 502 | Modbus TCP Port (Default 502) |
| `xEnable` | BOOL | - | **TRUE**: Start polling; **FALSE**: Stop and reset FB |
| `uiNumOfGroups` | UINT | 10 | Total number of polling groups (Max 20) |
| `aFunctionCode` | ARRAY[0..19] OF UINT | - | **1**:FC1, **2**:FC2, **3**:FC3, **4**:FC4 (Others default to 3) |
| `aUnitID` | ARRAY[0..19] OF BYTE | - | Modbus Unit ID (Slave ID) for each group |
| `aStartAddr` | ARRAY[0..19] OF UINT | - | Starting Modbus Register/Bit address |
| `aQuantity` | ARRAY[0..19] OF UINT | - | Number of items to read for each group |
| `tTimeout` | TIME | T#1S | Timeout duration for a single request |
| `uiMaxRetries` | UINT | 3 | Number of retries before reporting error |

### 2.2 Outputs (VAR_OUTPUT)
| Parameter | Data Type | Description |
| :--- | :--- | :--- |
| `awResultData` | ARRAY[0..3999] OF WORD | Master data table. Results are spliced sequentially |
| `xError` | BOOL | TRUE if any group in the current cycle fails |
| `sStatus` | STRING | General connection status (e.g., 'Connected', 'Disabled') |
| `xIsConnected` | BOOL | Status of the underlying TCP connection |
| `xAllOk` | BOOL | TRUE if the **entire** cycle completed without errors |
| `sDetailStatus` | STRING | Detailed progress (e.g., 'Reading: 1/5 (FC3)') |

---

## 3. Implementation Example (PLC_PRG)

```pascal
VAR
    MyPoller    : ModbusTCP_ARRAY;
    FinalData   : ARRAY[0..3999] OF WORD;
    
    // Example: Read 2 groups of FC3 and 1 group of FC4
    arrFC       : ARRAY[0..19] OF UINT := [3, 3, 4, 17(3)]; 
    arrAddr     : ARRAY[0..19] OF UINT := [0, 100, 500, 17(0)];
    arrQty      : ARRAY[0..19] OF UINT := [10, 10, 5, 17(0)];
END_VAR

// Call Function Block
MyPoller(
    aIPAddr       := [192, 168, 1, 224],
    xEnable       := TRUE,
    uiNumOfGroups := 3,
    aFunctionCode := arrFC,
    aUnitID       := [20(1)],
    aStartAddr    := arrAddr,
    aQuantity     := arrQty,
    awResultData  => FinalData
);
