from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from ..manager import ConnectionManager


router = APIRouter()
manager = ConnectionManager()


@router.websocket("/chat")
async def chat(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client # says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client # left the chat")
