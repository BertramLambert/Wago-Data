# WAGO CC100 Modbus RTU Multi-Slave Polling Guide

[中文版](./ReadMe-zh.md) | [English Version](./ReadMe.md)

---

<a name="english-version"></a>

## 🇺🇸 English Version

### Project Description
This project documents the implementation of multi-slave Modbus RTU polling on the **WAGO CC100 (751-9301)**. It uses a **CASE State Machine** to dynamically load parameters (Slave ID, Address, Length) for each station and stores the retrieved data sequentially into a 1D array named `abc`.

### 💡 Core Design Logic
1. **Parameterized Arrays**: Slave IDs, addresses, function codes, and lengths are stored in parallel arrays, toggled via the `iTaskIdx` pointer.
2. **Sequential 1D Storage**: To ensure data continuity, a memory offset is calculated using the formula `iTaskIdx * 10`, reserving a fixed 10-slot space for each slave.

3. **State Machine Control**:
    - **State 0**: Load parameters and wait for inter-frame delay (cool-down time).
    - **State 1**: Trigger communication and wait for a response or error signal.
    - **State 2**: Forcibly reset `xTrigger` and clear `bUnitId` to ensure the next rising edge trigger for the subsequent station.

### 💻 Core Implementation (ST)
```iecst
CASE iState OF
    0:  // Load parameters and inter-frame delay
        utQuery.bUnitId        := aUnitIds[iTaskIdx];
        utQuery.uiReadAddress  := aStartAddrs[iTaskIdx];
        utQuery.uiReadQuantity := aQuantities[iTaskIdx];
        
        timerTrigger(IN := TRUE, PT := T#200MS);
        IF timerTrigger.Q THEN
            timerTrigger(IN := FALSE);
            xTrigger := TRUE;   // Initiate communication
            iState   := 1;
        END_IF

    1:  // Wait for completion and data transfer
        IF utResponse.bUnitId > 0 AND fbMbMaster.oStatus.uiID = 0 THEN
            iOffset := iTaskIdx * 10; // Calculate 1D array offset
            abc[iOffset + 0] := WORD_TO_INT(utResponse.awData[0]);
            abc[iOffset + 1] := WORD_TO_INT(utResponse.awData[1]);
            iState := 2;
        ELSIF fbMbMaster.oStatus.xError THEN
            iState := 2; // Force switch even on error
        END_IF

    2:  // Clear flags and increment task index
        xTrigger := FALSE; 
        utResponse.bUnitId := 0; // CRITICAL: Reset the response flag
        iTaskIdx := (iTaskIdx + 1) MOD 3; 
        iState := 0;

END_CASE
