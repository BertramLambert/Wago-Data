# WAGO CC100 Modbus RTU Master Guide

[中文版](/ReadMe-zh.md) | [English Version](/ReadMe.md)

---

<a name="chinese-version"></a>
## 🇹🇼 中文版 (Chinese Version)

### 專案說明
本專案紀錄如何在 WAGO Compact Controller 100 (751-9301) 上，使用 **ST (Structured Text)** 語言實作 Modbus RTU 主站通訊，並對接 ModSim32 模擬器。

### ⚠️ 核心技術陷阱
1. **硬體路徑連結 (I_Port Mapping)**
   * 在 CC100 中，內建序列埠路徑通常為 `COM1`。
   * **注意**：這與搭配 750-652 模組的操作不同。若 `I_Port := COM1` 報錯，請使用 `F2` 輸入輔助工具，從 **IoConfig_Globals** 中選取正確的硬體物件路徑。
2. **緩衝區標記清理 (The "BUnitId" Trap)**
   * WAGO 的 `utResponse` 是全域緩衝區。通訊成功後，**必須手動清零**。
   * **關鍵動作**：`utResponse.bUnitId := 0;`
   * **原因**：若不清除，判斷式會在下個掃描週期因舊資料殘留而誤判，導致讀取邏輯重複執行。

### 💻 核心程式碼 (ST)
```iecst
// 1. 初始化設定
IF NOT xInitDone THEN
    utQuery.bUnitId         := 1;   // 從站 ID
    utQuery.bFunctionCode   := 3;   // Read Holding Registers
    utQuery.uiReadAddress   := 1;   // 位址 (對應 ModSim 40001)
    utQuery.uiReadQuantity  := 2;   
    xInitDone := TRUE;
END_IF

// 2. 呼叫功能塊
fbMbMaster(I_Port := COM1, utQuery := utQuery, xTrigger := xTrigger, utResponse := utResponse);

// 3. 通訊週期控制
timerTrigger(IN := NOT xTrigger, PT := T#1S);

// 4. 資料搬運與【清理標記】
IF xTrigger = FALSE AND fbMbMaster.oStatus.uiID = 0 AND utResponse.bUnitId > 0 THEN
    abc[0] := WORD_TO_INT(utResponse.awData[0]);
    abc[1] := WORD_TO_INT(utResponse.awData[1]);
    
    // --- 重要：手動清除接收旗標 ---
    utResponse.bUnitId := 0; 
END_IF

// 5. 觸發控制
IF timerTrigger.Q THEN
    xTrigger := TRUE;
ELSIF fbMbMaster.oStatus.xError OR (utResponse.bUnitId > 0) THEN 
    xTrigger := FALSE; 

END_IF
