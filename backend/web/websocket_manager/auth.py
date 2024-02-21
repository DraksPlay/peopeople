from fastapi.websockets import WebSocket
import jwt


def auth(websocket: WebSocket,
         secret_key: str
         ) -> bool:
    token = websocket.session.get("token")

    if not token:
        return False
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        if not payload.get("UUID") or not payload.get("exp"):
            return False
    except (jwt.exceptions.InvalidSignatureError, jwt.exceptions.ExpiredSignatureError):
        return False

    return True
