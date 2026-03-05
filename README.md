# 🌍 Global Chat Server

A lightweight real-time chat backend built with **FastAPI** and **WebSockets**.

This repository contains the **server implementation** for Global Chat.  
The desktop client is distributed separately via GitHub Releases.

---

# 📥 Download Desktop Application

You can download the Windows desktop chat client here:

## ⬇ Download Installer

[![Download](https://img.shields.io/badge/Download-Global%20Chat%20Installer-blue?style=for-the-badge)](https://github.com/TutorialsAndroid/global-chat/releases/download/v1.0.0/GlobalChatInstaller.exe)

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
```
---

# 📦 Installation (Server)

Install dependencies:

```
pip install -r requirements.txt

```
Run the server: python server.py
```

---

# ⚠ Notes

- Message history may reset after server redeploy if SQLite is used.
- Production deployments should use PostgreSQL or Redis.

---

# 📜 License

MIT License
