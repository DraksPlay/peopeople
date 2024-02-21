from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect,
    Request,
    Depends
)
import jwt
import uuid
from datetime import datetime, timedelta
import hashlib

from web.websocket_manager import WebsocketManager
from web.websocket_manager.validators import message_validator
from web.websocket_manager.auth import auth
from http_connector import HTTPConnectorAPI
from config import AUTH_SECRET_KEY

router = APIRouter()
wm = WebsocketManager(auth=auth, auth_secret_key=AUTH_SECRET_KEY)
api = HTTPConnectorAPI("http://localhost:8000")


@router.websocket("/chat")
async def chat(websocket: WebSocket
               ):
    status = await wm.connect(websocket)
    if not status:
        return None

    messages = await api.get_messages()
    await wm.send_message(websocket, messages)
    try:
        while True:
            message: dict | None = await wm.wait_message(websocket, validator=message_validator)
            if message is None:
                continue

            token = websocket.session.get("token")
            username = hashlib.md5(token.encode("utf-8")).hexdigest()

            await api.create_message(message.get("text"), username)
            await wm.send_message_all([{"text": message.get("text")}], sender=websocket)
    except WebSocketDisconnect:
        await wm.disconnect(websocket)


@router.get("/login")
async def login(request: Request):
    payload = {"UUID": uuid.uuid4().hex, "exp": datetime.utcnow() + timedelta(seconds=1130)}
    token = jwt.encode(payload, AUTH_SECRET_KEY, algorithm="HS256")
    request.session.update({"token": token})
