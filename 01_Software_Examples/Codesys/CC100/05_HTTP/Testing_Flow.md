[中文版](Testing_Flow-zh.md) | [English](Testing_Flow.md)

# ✅ 🎯 Testing Objectives

Verify three key factors:
- **Internet Connectivity**: Can the PLC reach the external network?
- **HTTP POST Success**: Is the POST request transmitted successfully?
- **Response Validation**: Is the response data received and processed correctly?

## ✅ 🧪 Testing SOP (Step-by-Step)

### 🔹 Step 1: Configure Test API
**👉 Use a public testing service (Most Stable)**
- `sUrl := 'http://httpbin.org/post';`
- `sPostData := '{"test": 123}';`

### 🔹 Step 2: Minimize Code
Ensure the logic is isolated to prevent interference from other network-heavy tasks or POUs.

### 🔹 Step 3: Download to PLC
In CODESYS:
- **Login**
- **Download**
- **Run**

### 🔹 Step 4: Manual Trigger (Crucial)
**👉 In the Watch Window:**
1. Set `xTrigger := TRUE;`
2. Wait for 1 second.
3. Reset `xTrigger := FALSE;`

> **⚠️ Note**: You must use a **"Pulse"** trigger. Do not keep it `TRUE` indefinitely, as the Function Block initiates on a rising edge.

### 🔹 Step 5: Monitor Key Variables (Core)
Focus on these 5 indicators:

| Variable | Status | Meaning |
| :--- | :--- | :--- |
| **① xBusy** | TRUE / FALSE | TRUE = Transmitting / FALSE = Completed |
| **② xError** | TRUE / FALSE | TRUE = Failed / FALSE = Success |
| **③ uiResponseCode**| **200** | ✅ Success |
| | **0** | ❌ No Connection |
| | **400 / 500** | Client Error / Server Error |
| **④ udiRxIndex** | **> 0** | ✅ Data received |
| | **= 0** | ❌ No data received |
| **⑤ sStatus** | Text | Error or status message details |

### 🔹 Step 6: Result Interpretation

**✅ Success (Goal reached)**
- `xError = FALSE`
- `uiResponseCode = 200`
- `udiRxIndex > 0`
- **Conclusion**: API communication is fully established.

**❌ DNS Issue**
- `uiResponseCode = 0`
- `sStatus = "Could not resolve host"`
- **Conclusion**: PLC lacks valid DNS configuration in WBM.

**❌ Network Issue**
- `sStatus = "Connection refused"`
- **Conclusion**: Firewall blockage or port is closed.

**❌ Timeout**
- `sStatus = "Timeout"`
- **Conclusion**: Network is down or the server is unresponsive.

### 🔹 Step 7: Verify Response Content (Advanced)
**👉 Convert received data to String:**
```pascal
sResponse : STRING(1023);
// Copy raw buffer to string
MEMCPY(ADR(sResponse), ADR(aRxBuffer), udiRxIndex);
