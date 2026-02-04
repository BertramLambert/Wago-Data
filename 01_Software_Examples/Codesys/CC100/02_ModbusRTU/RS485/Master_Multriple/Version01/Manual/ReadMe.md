# WAGO CC100 Modbus RTU Multi-Slave Polling Guide
[中文版](./ReadMe-zh.md) | [English Version](./ReadMe.md)

This document describes the implementation of a Modbus RTU Master on a **WAGO Compact Controller 100 (751-9301)** using a **CASE State Machine** to achieve dynamic multi-slave polling and sequential data storage in a 1D array.

## 🛠️ System Configuration
- **Hardware**: WAGO CC100 (Integrated RS485 Port)
- **Environment**: CODESYS V3 / e!COCKPIT
- **Communication**: 9600 bps, 8-N-1 (Standard RTU)
- **Data Layout**: Sequential 1D Array Mapping

---

## 💡 Key Design Principles

### 1. Parallel Task Arrays
Instead of hardcoding values, all communication parameters are stored in parallel arrays. This allows the master to dynamically update the query parameters by simply changing the task index (`iTaskIdx`).
- `aUnitIds`: List of Slave IDs.
- `aStartAddrs`: Corresponding register start addresses.
- `aQuantities`: Number of registers to read per slave.

### 2. Sequential 1D Data Storage
To ensure memory continuity (ideal for HMI/SCADA integration), all received data is mapped into a single 1D array `abc` using a fixed offset.
- **Formula**: `abc[iTaskIdx * 10 + offset]`
- **Reservation**: Each slave is allocated 10 slots to prevent data overlapping.



---

## 💻 Implementation (Structured Text)

```iecst
PROGRAM ModbusRTU_Master01
VAR
    // Modbus FB Instance
    fbMbMaster      : WagoAppPlcModbus.FbMbMasterSerial;
    utQuery         : WagoAppPlcModbus.typMbQuery;
    utResponse      : WagoAppPlcModbus.typMbResponse;

    // Control Variables
    xTrigger        : BOOL;
    timerTrigger    : TON;      
    iState          : INT := 0;  // CASE State Index
    iTaskIdx        : INT := 0;  // Current Task Pointer
    iMaxTasks       : INT := 2;  // Total tasks (0 to 2)
    iOffset         : INT;       // Calculated 1D Array Offset

    // Task Configuration Arrays
    aUnitIds        : ARRAY[0..2] OF BYTE := [1, 2, 3];        
    aStartAddrs     : ARRAY[0..2] OF UINT := [0, 10, 100];     
    aQuantities     : ARRAY[0..2] OF UINT := [2, 2, 2]; 

    // Sequential Data Buffer (3 slaves * 10 slots = 30)
    abc             : ARRAY[0..29] OF INT; 
END_VAR

// ---------------------------------------------------------
// 0. Continuous FB Execution
// ---------------------------------------------------------
fbMbMaster(
    xConnect    := TRUE, 
    I_Port      := COM1, 
    udiBaudrate := 9600, 
    ePhysical   := WagoTypesCom.eTTYPhysicalLayer.RS485_HalfDuplex, 
    eFrameType  := WagoAppPlcModbus.eMbFrameType.RTU,
    tTimeOut    := T#1500MS, 
    utQuery     := utQuery, 
    xTrigger    := xTrigger, 
    utResponse  := utResponse
);

// ---------------------------------------------------------
// 1. Polling State Machine
// ---------------------------------------------------------
CASE iState OF
    0:  // SETUP: Load Parameters & Inter-frame Delay
        utQuery.bUnitId        := aUnitIds[iTaskIdx];
        utQuery.uiReadAddress  := aStartAddrs[iTaskIdx];
        utQuery.uiReadQuantity := aQuantities[iTaskIdx];
        
        timerTrigger(IN := TRUE, PT := T#200MS); // Cool-down delay
        IF timerTrigger.Q THEN
            timerTrigger(IN := FALSE);
            xTrigger := TRUE;   // Rising edge to start communication
            iState   := 1;
        END_IF

    1:  // WAIT: Monitor Response or Error
        IF utResponse.bUnitId > 0 AND fbMbMaster.oStatus.uiID = 0 THEN
            // SUCCESS: Calculate offset and store data
            iOffset := iTaskIdx * 10; 
            abc[iOffset + 0] := WORD_TO_INT(utResponse.awData[0]);
            abc[iOffset + 1] := WORD_TO_INT(utResponse.awData[1]);
            iState := 2;

        ELSIF fbMbMaster.oStatus.xError THEN
            // ERROR: Skip to next slave to prevent loop hang
            iState := 2;
        END_IF

    2:  // RESET: Clear Flags & Increment Pointer
        xTrigger := FALSE;       
        utResponse.bUnitId := 0; // CRITICAL: Reset the response flag
        
        iTaskIdx := iTaskIdx + 1;
        IF iTaskIdx > iMaxTasks THEN
            iTaskIdx := 0;       // Loop back to first slave
        END_IF
        iState := 0;             
END_CASE

