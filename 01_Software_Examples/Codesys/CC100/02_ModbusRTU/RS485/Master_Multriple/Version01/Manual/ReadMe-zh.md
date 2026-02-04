# WAGO CC100 Modbus RTU Multi-Slave Polling Guide

[中文版](./ReadMe-zh.md) | [English Version](./ReadMe.md)

---

<a name="chinese-version"></a>

## 🇹🇼 中文版 (Chinese Version)

### 專案說明
本專案紀錄如何在 WAGO CC100 (751-9301) 上實作多站 Modbus RTU 輪詢。透過 **CASE 狀態機** 動態載入各站參數（站號、位址、長度），並將讀取到的數據依序存入一維陣列 `abc` 中。

### 💡 核心設計邏輯
1. **參數陣列化**：站號、位址、功能碼與長度分別儲存在平行陣列中，透過 `iTaskIdx` 指標切換。
2. **一維序列化儲存**：為確保資料連續性，使用公式 `iTaskIdx * 10` 計算存儲偏移量，每站固定預留 10 個空間。
3. **狀態機控制**：
    - **State 0**: 載入參數，等待站間冷卻時間。
    - **State 1**: 觸發通訊並等待回應或錯誤。
    - **State 2**: 強制重置 `xTrigger` 與清理 `bUnitId`，確保下一次上升沿觸發。

### 💻 核心程式碼 (ST)
```iecst
CASE iState OF
    0:  // 載入參數與間隔冷卻
        utQuery.bUnitId        := aUnitIds[iTaskIdx];
        utQuery.uiReadAddress  := aStartAddrs[iTaskIdx];
        utQuery.uiReadQuantity := aQuantities[iTaskIdx];
        
        timerTrigger(IN := TRUE, PT := T#200MS);
        IF timerTrigger.Q THEN
            timerTrigger(IN := FALSE);
            xTrigger := TRUE;   // 觸發通訊
            iState   := 1;
        END_IF

    1:  // 等待完成並搬運資料
        IF utResponse.bUnitId > 0 AND fbMbMaster.oStatus.uiID = 0 THEN
            iOffset := iTaskIdx * 10; // 計算一維偏移
            abc[iOffset + 0] := WORD_TO_INT(utResponse.awData[0]);
            abc[iOffset + 1] := WORD_TO_INT(utResponse.awData[1]);
            iState := 2;
        ELSIF fbMbMaster.oStatus.xError THEN
            iState := 2; // 報錯也強迫換站
        END_IF

    2:  // 清理標記與指標位移
        xTrigger := FALSE; 
        utResponse.bUnitId := 0; // 關鍵：清盤子
        iTaskIdx := (iTaskIdx + 1) MOD 3; 
        iState := 0;

END_CASE
