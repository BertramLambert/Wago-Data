# WAGO PLC HTTP Client Integration (WagoAppHTTP)

[中文](Readme-zh.md) | [English](Readme.md)

![WAGO](https://img.shields.io/badge/Hardware-WAGO%20PFC200%20%2F%20CC100-green)
![CODESYS](https://img.shields.io/badge/Software-CODESYS%20V3.5-blue)
![Library](https://img.shields.io/badge/Library-WagoAppHTTP-orange)

This project demonstrates how to use the `WagoAppHTTP` library within the WAGO CODESYS environment to communicate with Web Services (RESTful APIs). It is ideal for IIoT applications, cloud data telemetry, and cross-system integration.

## 📖 Table of Contents
* [Key Features](#key-features)
* [System Requirements](#system-requirements)
* [Quick Start](#quick-start)
* [Implementation Logic](#implementation-logic)
* [Troubleshooting & Debugging](#troubleshooting--debugging)

---

## ✨ Key Features
- **HTTP Method Support**: Full support for GET, POST, PUT, and DELETE.
- **Flexible Header Configuration**: Easily implement API Key, Bearer Token authentication, and custom Content-Type.
- **JSON Data Integration**: Examples for transmitting and handling standard JSON payloads.
- **HTTPS Security**: Secure data transmission via WAGO’s certificate management mechanism.

## 🛠 System Requirements
- **IDE**: CODESYS V3.5 (or e!COCKPIT)
- **Controller**: WAGO PFC200 Series or CC100 (Firmware FW23 or higher recommended)
- **Library**: `WagoAppHTTP` (Ensure it is added via the Library Manager)

## 🚀 Quick Start

### 1. Library Installation
In your CODESYS project, open the **Library Manager**, click **Add Library**, search for `WagoAppHTTP`, and add it to your project.

### 2. Variable Declaration (GVL or POU VAR)
```pascal
VAR
    fbHttpClient    : WagoAppHTTP.FbHttpClient;
    stRequest       : WagoAppHTTP.WAGO_STRUCT_HTTP_REQUEST;
    stResponse      : WagoAppHTTP.WAGO_STRUCT_HTTP_RESPONSE;
    xTrigger        : BOOL;    // Trigger for the HTTP request
    sPostData       : STRING(511) := '{"sensor": "temp", "value": 24.5}';
END_VAR
