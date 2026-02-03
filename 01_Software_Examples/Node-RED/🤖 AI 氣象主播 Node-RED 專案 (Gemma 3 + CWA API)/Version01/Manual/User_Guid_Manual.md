# 🤖 AI 氣象主播服務 (Gemma 3 + CWA API)

[Ollama Technical Document](https://github.com/ollama/ollama?tab=readme-ov-file#community-integrations)

這是一個建立在 **Node-RED** 環境下的自動化氣象播報系統。透過整合**中央氣象署 (CWA) 開放資料**與**本地 AI 模型 (Ollama)**，使用者只需輸入縣市名稱，系統即可自動產出一段口語化、具生活建議的天氣摘要。

## 🌟 核心亮點
* **智能地名識別**：自動處理「台/臺」異體字，並將模糊輸入（如：台中）校正為標準 API 參數（如：臺中市）。
* **效能最佳化**：針對本地 AI (Ollama) 的運算瓶頸，將數萬字的原始 JSON 數據精簡為 100 字內的核心摘要，根除系統超時問題。
* **資料穩定性**：採用 `F-C0032-001` (36 小時預報) API，具備體積小、路徑層級簡單的優點，確保解析 100% 成功。

---

## 🏗️ 系統流程圖


1.  **Dashboard Input**：使用者輸入地名（如：台南）。
2.  **Function 1 (Pre-processing)**：
    * 進行字體標準化（台 ➔ 臺）。
    * 根據地名清單匹配標準縣市名（如補上市/縣）。
    * 構建帶有 `locationName` 過濾參數的 API URL，從源頭減少資料量。
3.  **HTTP Request**：向氣象署獲取 JSON 數據。
4.  **Function 2 (Data Cleaner)**：
    * 驗證 JSON 結構安全性。
    * 提取核心維度：天氣現象 (Wx)、最低溫 (MinT)、最高溫 (MaxT)、降雨機率 (PoP)。
    * 輸出 AI 格式化指令（System Prompt + 精簡數據）。
5.  **Ollama Chat Node**：使用本地模型執行推理（推薦使用 `gemma3:4b`）。
6.  **UI Output**：在 Dashboard 顯示 AI 生成的語音感播報內容。

---

## 🛠️ 技術故障排除 (Troubleshooting)

### 1. 解決解析報錯 `reading '0'`
* **問題**：氣象局不同 API 編號（如 `091` 一週預報 vs `073` 3小時預報）的 JSON 層級結構不互通。
* **解決**：本專案統一使用 `F-C0032-001` API，並將解析路徑鎖定在 `records.location[0]`。

### 2. 解決 `HeadersTimeoutError` (讀取超時)
* **問題**：原始 API 資料量過大（含經緯度、各種氣象細項），導致 Ollama 讀取與運算時間過長。
* **解決**：在傳送給 AI 前，將資料「減肥」，僅傳送未來 3 個時段（36 小時）的精華數據，讓 AI 回覆速度縮短至秒級。

---

## 📋 安裝指南
1.  **API 準備**：至 [中央氣象署開放資料平台](https://opendata.cwa.gov.tw/) 申請金鑰。
2.  **Ollama 環境**：啟動本地 Ollama 伺服器，並確認模型已下載（例如：`ollama run gemma3`）。
3.  **Node-RED 配置**：
    * 確保安裝 `node-red-node-http-request`。
    * `http request` 節點的 **Return** 必須設為 `a parsed JSON object`。

---

## 📜 聲明
本專案為開發測試使用，氣象數據來源為中央氣象署。AI 生成之播報內容僅供參考，請以政府發布之正式氣象通報為準。
