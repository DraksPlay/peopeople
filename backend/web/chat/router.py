from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect,
    Request
)
import jwt
import uuid
from datetime import (
    datetime,
    timedelta,
)
import hashlib

from web.websocket_manager import WebsocketManager
from web.websocket_manager.validators import event_validator
from web.websocket_manager.events import Event, NewMessageEvent, OpenEvent
from web.websocket_manager.auth import auth
from web.websocket_manager.exceptions import ValidationError
from http_connector import HTTPConnectorAPI
from config import (
    AUTH_SECRET_KEY,
    API_URL
)


router = APIRouter()
wm = WebsocketManager(auth=auth, auth_secret_key=AUTH_SECRET_KEY)
api = HTTPConnectorAPI(API_URL)


@router.websocket("/chat")
async def chat(websocket: WebSocket):
    status = await wm.connect(websocket)
    if not status:
        return None

    messages = await api.get_messages()
    messages = [{"text": message.get("text"), "username": message.get("user").get("name")} for message in messages]

    await wm.send_message(websocket, {"event": "messages",
                                      "body": {"messages": messages}
                                      })
    try:
        while True:
            message: dict | None = await wm.wait_message(websocket)
            if message is None:
                continue
            res_valid = event_validator(message)
            if not res_valid:
                continue
            event = Event(message).create()

            if isinstance(event, NewMessageEvent):
                await api.create_message(event.text, event.username)
                await wm.send_message_all({"event": "messages",
                                           "body": {"messages": [{"text": event.text, "username": event.username}]}
                                           },
                                          sender=websocket)
            elif isinstance(event, OpenEvent):
                await wm.send_message(websocket, {"event": "open", "body": {"username": websocket.session.get("username")}})
    except WebSocketDisconnect:
        await wm.disconnect(websocket)


@router.get("/login")
async def login(request: Request):
    payload = {"UUID": uuid.uuid4().hex, "exp": datetime.utcnow() + timedelta(seconds=3600)}
    token = jwt.encode(payload, AUTH_SECRET_KEY, algorithm="HS256")
    username = hashlib.md5(token.encode("utf-8")).hexdigest()
    request.session.update({"token": token, "username": username})
