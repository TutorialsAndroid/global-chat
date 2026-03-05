from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import uvicorn
import json
import sqlite3

app = FastAPI()

conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    text TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


class ConnectionManager:

    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):

        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    cursor.execute(
        "SELECT name, text FROM messages ORDER BY id DESC LIMIT 50"
    )

    rows = cursor.fetchall()

    for name, text in reversed(rows):
    await websocket.send_text(json.dumps({
        "name": name,
        "text": text
    }))

    # tell client history is finished
    await websocket.send_text(json.dumps({
        "type": "history_end"
    }))

    try:

        while True:

            data = await websocket.receive_text()

            message = json.loads(data)

            name = message.get("name")
            text = message.get("text")

            cursor.execute(
                "INSERT INTO messages (name, text) VALUES (?, ?)",
                (name, text)
            )

            conn.commit()

            await manager.broadcast(json.dumps(message))

    except WebSocketDisconnect:

        manager.disconnect(websocket)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)