from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from web.manager import ConnectionManager
from web.connector_api import Connector
from config import (
    API_URL
)


router = APIRouter()
manager = ConnectionManager()
c_api = Connector("http://localhost:8000")


@router.websocket("/chat")
async def chat(websocket: WebSocket):
    await manager.connect(websocket)

    messages = await c_api.get_messages()
    await manager.send_message(websocket, messages)
    try:
        while True:
            data = await websocket.receive_text()
            await c_api.create_message(data)
            await manager.broadcast([{"text": data}], sender=websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
