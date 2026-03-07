# 🌍 Global Chat Server

A lightweight real-time chat backend built with **FastAPI** and **WebSockets**.

This repository contains the **server implementation** for Global Chat.  
The desktop client is distributed separately via GitHub Releases.

---

# 📥 Download Desktop Application

You can download the Windows desktop chat client here:

## ⬇ Download Installer

[![Download](https://img.shields.io/badge/Download-Global%20Chat%20Installer-blue?style=for-the-badge)](https://github.com/TutorialsAndroid/global-chat/releases)

Download the latest version and run the installer to start chatting.

---

# ✨ Features

- 🌍 Real-time global chat
- ⚡ WebSocket communication
- 💬 Multi-user messaging
- 🔗 Clickable links in chat
- 📋 Selectable and copyable messages
- 🪟 Minimal floating chat window
- 📌 Always-on-top interface
- ⚙ Settings menu with startup option
- 📜 Chat history loading

---

# 🏗 Server Technology

The backend server uses:

- **FastAPI**
- **WebSockets**
- **Uvicorn**

It broadcasts messages to all connected clients in real time.

---

# 🚀 Deployment

This server is designed to be deployed on platforms such as:

- Railway
- Render
- Fly.io
- VPS servers

Example Railway deployment command:

```
uvicorn server:app --host 0.0.0.0 --port 8000
```
---
# 🔌 WebSocket Endpoint
```
/chat
```
Example connection URL:
wss://your-server-url/chat

# 📦 Installation (Server)

Install dependencies:
```
pip install -r requirements.txt
```
Run the server: python server.py

---

# ⚠ Notes

- Message history may reset after server redeploy if SQLite is used.
- Production deployments should use PostgreSQL or Redis.

---

# 📜 License

MIT License

Copyright (c) 2026 Akshay

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.