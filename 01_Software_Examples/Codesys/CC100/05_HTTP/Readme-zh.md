# WAGO PLC HTTP Client Integration (WagoAppHTTP)

[中文](./Readme-zh.md) | [English](Readme.md)

![WAGO](https://img.shields.io/badge/Hardware-WAGO%20PFC200%20%2F%20CC100-green)
![CODESYS](https://img.shields.io/badge/Software-CODESYS%20V3.5-blue)
![Library](https://img.shields.io/badge/Library-WagoAppHTTP-orange)

此專案展示如何在 WAGO 控制器環境下使用 `WagoAppHTTP` 函式庫與 Web 服務（RESTful API）進行通訊。這對於 IIoT 應用、雲端數據上傳以及跨系統整合非常實用。

## 📖 專案目錄
* [功能特色](#功能特色)
* [環境需求](#環境需求)
* [快速開始](#快速開始)
* [程式邏輯說明](#程式邏輯說明)
* [常見問題與調試](#常見問題與調試)

---

## ✨ 功能特色
- **HTTP 方法支持**：支援 GET, POST, PUT, DELETE。
- **靈活的 Header 設定**：支援 API Key、Token 驗證與 Content-Type 自定義。
- **JSON 資料串接**：示範如何傳送與處理標準 JSON 格式。
- **HTTPS 支援**：透過 WAGO 證書管理機制實現安全傳輸。

## 🛠 環境需求
- **IDE**: CODESYS V3.5 (或 e!COCKPIT)
- **控制器**: WAGO PFC200 系列或 CC100 (韌體版本 FW23+)
- **函式庫**: `WagoAppHTTP` (請確認已在 Library Manager 搜尋並加入)

## 🚀 快速開始

### 1. 安裝函式庫
在 CODESYS 專案的 **Library Manager** 中，點擊 `Add Library`，輸入關鍵字 `WagoAppHTTP` 並安裝。

### 2. 變數宣告 (GVL 或 POU VAR)
```pascal
VAR
    fbHttpClient    : WagoAppHTTP.FbHttpClient;
    stRequest       : WagoAppHTTP.WAGO_STRUCT_HTTP_REQUEST;
    stResponse      : WagoAppHTTP.WAGO_STRUCT_HTTP_RESPONSE;
    xTrigger        : BOOL;    // 觸發 HTTP 請求
    sPostData       : STRING(511) := '{"sensor": "temp", "value": 24.5}';
END_VAR
