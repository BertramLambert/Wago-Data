# WAGO CC100 Modbus RTU Multi-Slave Polling Guide

This project documents the implementation of a Modbus RTU Master on the **WAGO Compact Controller 100 (751-9301)** using a **CASE State Machine** for dynamic multi-slave polling and sequential 1D array data storage.

## 🛠️ System Configuration
- **Hardware**: WAGO CC100 (Integrated RS485 Port).
- **Environment**: CODESYS V3 / e!COCKPIT.
- **Protocol**: Modbus RTU (9600-8-N-1).
- **Storage Strategy**: 1D Sequential Array (10 slots reserved per slave).

---

## 💡 Core Design Logic

### 1. Dynamic Parameter Arrays
All communication parameters (Slave ID, Address, Quantity) are stored in parallel arrays. The system switches tasks by incrementing the `iTaskIdx` pointer, allowing for easy expansion without modifying the execution logic.

### 2. Sequential 1D Storage Mapping
To maintain memory continuity, data is mapped into a single array using a fixed offset calculation:
> **Offset Formula**: `iTaskIdx * 10`
> *Example: Slave 1 data resides in `abc[0..9]`, Slave 2 in `abc[10..19]`, etc.*



### 3. State Machine Control Flow
- **State 0 (Setup)**: Loads parameters for the current task and waits for a "cool-down" delay to ensure bus stability.
- **State 1 (Execution)**: Triggers the Modbus request and monitors for completion (`bUnitId > 0`) or hardware error (`xError`).
- **State 2 (Reset)**: Forcibly resets `xTrigger` to `FALSE` and clears the response flag to ensure the next task starts on a fresh rising edge.

---

## 💻 Core Implementation (Structured Text)

```iecst
CASE iState OF
    0:  // --- Step 0: Load Task Parameters & Inter-frame Delay ---
        utQuery.bUnitId        := aUnitIds[iTaskIdx];
        utQuery.uiReadAddress  := aStartAddrs[iTaskIdx];
        utQuery.uiReadQuantity := aQuantities[iTaskIdx];
        
        timerTrigger(IN := TRUE, PT := T#200MS);
        IF timerTrigger.Q THEN
            timerTrigger(IN := FALSE);
            xTrigger := TRUE;   // Initiate communication (Rising Edge)
            iState   := 1;
        END_IF

    1:  // --- Step 1: Wait for Response or Error ---
        IF utResponse.bUnitId > 0 AND fbMbMaster.oStatus.uiID = 0 THEN
            // Success: Calculate offset and move data to 1D array
            iOffset := iTaskIdx * 10; 
            abc[iOffset + 0] := WORD_TO_INT(utResponse.awData[0]);
            abc[iOffset + 1] := WORD_TO_INT(utResponse.awData[1]);
            iState := 2;
            
        ELSIF fbMbMaster.oStatus.xError THEN
            // Error: Skip to next task to prevent system hang
            iState := 2;
        END_IF

    2:  // --- Step 2: Reset Flags & Shift Task Index ---
        xTrigger := FALSE; 
        utResponse.bUnitId := 0; // CRITICAL: Clear the buffer flag
        
        iTaskIdx := iTaskIdx + 1;
        IF iTaskIdx > iMaxTasks THEN 
            iTaskIdx := 0; // Return to first slave
        END_IF
        iState := 0;

END_CASE
