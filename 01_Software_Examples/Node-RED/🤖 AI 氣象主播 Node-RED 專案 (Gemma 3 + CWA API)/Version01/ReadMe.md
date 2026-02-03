# 🤖 AI Weather Anchor Service (Gemma 3 + CWA API)

[Ollama Technical Document](https://github.com/ollama/ollama?tab=readme-ov-file#community-integrations)

---
**Language / 語言選擇**
> [繁體中文版本 (ReadMe-zh.md)](./ReadMe-zh.md) | **English Version**
---

This automated weather broadcasting system is built on **Node-RED**. By integrating **Central Weather Administration (CWA) Open Data** with a **local AI model (Ollama)**, the system generates a natural, conversational weather summary based on the city name entered by the user.

## 🌟 Core Highlights
* **Intelligent Location Recognition**: Automatically handles "台/臺" variant characters and calibrates vague inputs into standard API parameters.
* **Performance Optimization**: Streamlines raw JSON data into a core summary of under 100 words, eliminating system timeout issues for local AI.
* **Data Stability**: Uses the `F-C0032-001` (36-hour forecast) API for a 100% parsing success rate.

## 🏗️ System Architecture
1. **Dashboard Input**: User enters a location (e.g., Tainan).
2. **Function 1 (Pre-processing)**: Character standardization and filtered API URL construction.
3. **HTTP Request**: Fetches JSON data from CWA.
4. **Function 2 (Data Cleaning)**: Extracts core metrics (Wx, MinT, MaxT, PoP) and packages them as AI prompts.
5. **Ollama Chat Node**: Performs inference using a local model (Recommended: `gemma3:4b`).
6. **UI Output**: Displays conversational reports on the Dashboard.

## 🛠️ Troubleshooting
| Issue | Cause | Solution |
| :--- | :--- | :--- |
| **Parsing Error (`reading '0'`)** | Incompatible API JSON structures | Use `F-C0032-001` and lock path to `records.location[0]` |
| **Timeout (`HeadersTimeoutError`)** | Large data causing long AI compute | Slim down data in Function 2; send 36-hour core data only |

## 📋 Installation
1. **API**: Get your key from [CWA Open Data Platform](https://opendata.cwa.gov.tw/).
2. **Ollama**: Ensure local installation and download model (`ollama run gemma3`).
3. **Node-RED**: Set `http request` node **Return** to `a parsed JSON object`.

## 📜 Disclaimer
This project is for development/testing. Data sourced from CWA. AI content is for reference only.
