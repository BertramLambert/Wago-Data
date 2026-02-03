# 🤖 AI 氣象主播服務 (Gemma 3 + CWA API)

[Ollama 技術文件](https://github.com/ollama/ollama?tab=readme-ov-file#community-integrations)

---
**Language / 語言選擇**
> **繁體中文版本** | [English Version (README.md)](./README.md)
---

這是一個建立在 **Node-RED** 環境下的自動化氣象播報系統。透過整合 **中央氣象署 (CWA) 開放資料** 與 **本地 AI 模型 (Ollama)**，使用者只需輸入縣市名稱，系統即可自動產出一段口語化、具生活建議的天氣摘要。

## 🌟 核心亮點
* **智能地名識別**：自動處理「台/臺」異體字，並將模糊輸入（如：台中）校正為標準 API 參數（如：臺中市）。
* **效能最佳化**：針對本地 AI (Ollama) 的運算瓶頸，將數萬字的原始 JSON 數據精簡為 100 字內的核心摘要，根除系統超時問題。
* **資料穩定性**：採用 `F-C0032-001` (36 小時預報) API，路徑層級簡單，確保解析 100% 成功。

## 🏗️ 系統流程圖
1. **Dashboard Input**：使用者輸入地名（如：台南）。
2. **Function 1 (前處理)**：進行字體標準化與縣市匹配，構建過濾後的 API URL。
3. **HTTP Request**：向氣象署獲取 JSON 數據。
4. **Function 2 (資料清洗)**：提取核心維度（Wx, MinT, MaxT, PoP）並封裝為 AI 指令。
5. **Ollama Chat Node**：使用本地模型執行推理（推薦 `gemma3:4b`）。
6. **UI Output**：在 Dashboard 顯示語音感播報內容。

## 🛠️ 技術故障排除
| 問題 | 成因 | 解決方案 |
| :--- | :--- | :--- |
| **解析錯誤 (`reading '0'`)** | 不同編號 API 的 JSON 結構不互通 | 統一使用 `F-C0032-001` 並鎖定 `records.location[0]` |
| **超時 (`HeadersTimeoutError`)** | 資料過大導致 AI 運算過久 | 在 Function 2 進行資料「減肥」，僅傳送 36 小時精華數據 |

## 📋 安裝指南
1. **API**: 至 [中央氣象署開放資料平台](https://opendata.cwa.gov.tw/) 申請金鑰。
2. **Ollama**: 確保本地安裝並下載模型（`ollama run gemma3`）。
3. **Node-RED**: `http request` 節點的 **Return** 必須設為 `a parsed JSON object`。

## 📜 聲明
本專案為開發測試使用，氣象數據來源為中央氣象署。AI 生成之內容僅供參考。
