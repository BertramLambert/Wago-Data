[中文版](Testing_Flow-zh.md)  | [English](Testing_Flow.md)

# ✅ 🎯 測試目標

確認三件事：

- PLC 是否能連外網

- HTTP POST 是否成功

- 是否正確收到回應資料

## ✅ 🧪 測試 SOP（一步一步）
###🔹 Step 1：設定測試 API

# 👉 使用公開測試服務（最穩）

- sURI := 'http://httpbin.org/post';
- sPostData := '{"test":123}';
###🔹 Step 2：確認程式最小化（避免干擾）


###🔹 Step 3：下載程式到 PLC

-👉 Codesys：

- Login

- Download

- Run

### 🔹 Step 4：手動觸發（關鍵）

- 👉 在 Watch 視窗：

- 設：

- xTrigger = TRUE

- 等 1 秒

改回：

- xTrigger = FALSE
⚠️ 重點

👉 一定要做「脈波」
（不能一直 TRUE）

### 🔹 Step 5：觀察變數（核心）

你只需要看這 5 個：

- ① xBusy
- TRUE → 傳送中
- FALSE → 已完成
- ② xError
- TRUE → 失敗
- FALSE → 成功
- ③ uiResponceCode（最重要）
- 值	意義
- 200	✅ 成功
- 0	❌ 沒連上
- 400	請求錯
- 500	Server錯
- ④ udiRxIndex
- > 0 → 有收到資料 ✅
- = 0 → 沒收到 ❌
- ⑤ sStatus

👉 錯誤或狀態訊息

### 🔹 Step 6：結果判讀
✅ 成功（你現在就是這個）
- xError = FALSE
- uiResponceCode = 200
- udiRxIndex > 0

👉 ✔ API 完全打通

❌ DNS 問題
uiResponceCode = 0
sStatus = Could not resolve host

👉 PLC 沒 DNS

❌ 網路問題
sStatus = Connection refused

👉 防火牆 / port 被擋

❌ Timeout
sStatus = Timeout

👉 網路不通 / server 無回應

### 🔹 Step 7：驗證回應內容（進階）

👉 把回傳資料轉字串：

sResponse : STRING(1023);

MEMCPY(ADR(sResponse), ADR(aRxBuffer), udiRxIndex);

👉 你會看到 JSON（httpbin 回傳）

### 🔹 Step 8：PC 交叉測試（很重要）

在你電腦跑：

curl -X POST http://httpbin.org/post -d '{"test":123}'

👉 判斷：

結果	意義
PC OK / PLC 不行	PLC 網路問題
兩邊都不行	API問題
