# WAGO CC100 Modbus RTU Master Implementation Guide

This document records the implementation of Modbus RTU Master communication on a **WAGO CC100 (751-9301)** controller using **Structured Text (ST)** to interface with **ModSim32**.

---

## ⚠️ Critical Technical Pitfalls

### 1. Hardware Path Mapping (`I_Port`)
On the CC100, the onboard RS485 port is defined as a hardware node, typically named `COM1`.
* **The Trap**: Unlike modular controllers (e.g., 750-8212) where serial modules generate global variables like `_750_652_xx`, the CC100 requires a direct reference to the onboard port.
* **Solution**: If `I_Port := COM1` causes a build error, use the **F2 Input Assistant** and select the port from **IoConfig_Globals** to ensure the correct hardware path is linked.

### 2. Manual Buffer Clearing (`bUnitId`)
The `WagoAppPlcModbus` library uses a global response structure `utResponse`. After a successful read, you **MUST** manually reset the unit ID.
* **Key Action**: `utResponse.bUnitId := 0;`
* **Reason**: If the `bUnitId` is not cleared, the condition `IF utResponse.bUnitId > 0` will remain TRUE in the following scan cycles due to residual data. This leads to logic errors or redundant data processing.

---

## 💻 Core Code Implementation (ST)



```iecst
PROGRAM ModbusRTU_Master01
VAR
    // Modbus Master Core
    fbMbMaster      : WagoAppPlcModbus.FbMbMasterSerial;
    utQuery         : WagoAppPlcModbus.typMbQuery;
    utResponse      : WagoAppPlcModbus.typMbResponse;

    // Control Variables
    xTrigger        : BOOL;         // Communication trigger pulse
    timerTrigger    : TON;          // Polling interval timer
    xInitDone       : BOOL;

    // Data Storage
    abc             : ARRAY[0..124] OF INT; 
    uiSuccessCount  : UINT;         // Diagnostic success counter
END_VAR

// 1. Initialization (Run once)
IF NOT xInitDone THEN
    utQuery.bUnitId         := 1;   // Target Slave ID
    utQuery.bFunctionCode   := 3;   // Function: Read Holding Registers
    utQuery.uiReadAddress   := 1;   // Address (Maps to ModSim 40001)
    utQuery.uiReadQuantity  := 2;   // Number of registers to read
    xInitDone := TRUE;
END_IF

// 2. Call Function Block (Link I_Port to the onboard COM1)
fbMbMaster(
    xConnect    := TRUE, 
    I_Port      := COM1, 
    udiBaudrate := 9600, 
    ePhysical   := WagoTypesCom.eTTYPhysicalLayer.RS485_HalfDuplex, 
    eFrameType  := WagoAppPlcModbus.eMbFrameType.RTU,
    tTimeOut    := T#2S, 
    utQuery     := utQuery, 
    xTrigger    := xTrigger, 
    utResponse  := utResponse
);

// 3. Polling Logic (Trigger every 1 second)
timerTrigger(IN := NOT xTrigger, PT := T#1S);

// 4. Data Transfer & [Buffer Clearing]
// Check if Trigger is done, Status is OK, and valid UnitId is present
IF xTrigger = FALSE AND fbMbMaster.oStatus.uiID = 0 AND utResponse.bUnitId > 0 THEN
    // Map raw data to application variables
    abc[0] := WORD_TO_INT(utResponse.awData[0]);
    abc[1] := WORD_TO_INT(utResponse.awData[1]);
    
    uiSuccessCount := uiSuccessCount + 1;
    
    // --- CRITICAL: Manually clear the response flag ---
    utResponse.bUnitId := 0; 
END_IF

// 5. Trigger Signal Management
IF timerTrigger.Q THEN
    xTrigger := TRUE;
ELSIF fbMbMaster.oStatus.xError OR (utResponse.bUnitId > 0) THEN 
    xTrigger := FALSE; // Reset trigger on completion or error
END_IF
