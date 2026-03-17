# WAGO PLC HTTP Client Integration (WagoAppHTTP)

![WAGO](https://img.shields.io/badge/Hardware-WAGO%20PFC200%20%2F%20CC100-green)
![CODESYS](https://img.shields.io/badge/Software-CODESYS%20V3.5-blue)
![Library](https://img.shields.io/badge/Library-WagoAppHTTP%201.7.3.5-orange)

This project demonstrates how to implement HTTP POST requests on a WAGO Compact Controller 100 using the `WagoAppHTTP` library. It is designed for IIoT applications, such as sending sensor data to a RESTful API or a Next.js backend.

## 📖 Table of Contents
* [Key Features](#key-features)
* [System Requirements](#system-requirements)
* [Quick Start](#quick-start)
* [Testing SOP](#-testing-sop-step-by-step)
* [Troubleshooting](#-troubleshooting)

---

## ✨ Key Features
- **Library Version 1.7.3.5**: Optimized for the latest WAGO firmware.
- **JSON Integration**: Demonstrates how to send JSON payloads to external servers.
- **Robust Status Monitoring**: Includes response code and error handling.

## 🛠 System Requirements
- **Hardware**: WAGO Compact Controller 100 (751-9402) or PFC200.
- **Software**: CODESYS V3.5.
- **Library**: `WagoAppHTTP` (v1.7.3.5).

## 🚀 Quick Start

### 1. Variable Declaration (VAR)
```pascal
PROGRAM PLC_PRG
VAR
    fbHttpPost      : WagoAppHTTP.FbHTTP_Post; 
    stConfig        : WagoAppHTTP.WAGO_STRUCT_HTTP_CONFIG; 
    stResponse      : WagoAppHTTP.WAGO_STRUCT_HTTP_RESPONSE;
    xTrigger        : BOOL; 
    sPostData       : STRING(511) := '{"test": 123}';
END_VAR
