from fastapi import WebSocket
from typing import Any, Callable, Optional
from json.decoder import JSONDecodeError

from .statements import Mode


class WebsocketManager:

    def __init__(self,
                 auth: Optional[Callable] = None,
                 auth_secret_key: str | None = None):
        self.active_connections: list[WebSocket] = []
        self.auth = auth
        self.auth_secret_key = auth_secret_key

    async def connect(self,
                      websocket: WebSocket
                      ) -> bool:
        if self.auth is not None:
            status = self.auth(websocket, self.auth_secret_key)
            if not status:
                return False

        await websocket.accept()
        self.active_connections.append(websocket)

        return True

    async def disconnect(self,
                         websocket: WebSocket
                         ) -> None:
        self.active_connections.remove(websocket)

    async def send_message(self,
                           receiver: WebSocket,
                           message: Any | str | bytes,
                           mode: Mode = Mode.JSON
                           ) -> None:
        match mode:
            case Mode.JSON:
                await receiver.send_json(message)
            case Mode.TEXT:
                await receiver.send_text(message)
            case Mode.BYTE:
                await receiver.send_bytes(message)
            case _:
                raise "Mode is invalid"

    async def send_message_all(self,
                               message: Any | str | bytes,
                               sender: WebSocket | None = None,
                               mode: Mode = Mode.JSON
                               ) -> None:
        for connection in self.active_connections:
            if connection == sender:
                continue
            await self.send_message(connection, message, mode=mode)

    async def wait_message(self,
                           sender: WebSocket,
                           mode: Mode = Mode.JSON,
                           validator: Optional[Callable] = None
                           ) -> Any | str | bytes | None:
        """

        :param sender:
        :param mode:
        :param validator:
        :return: Description return values:
        - Any:
        - str:
        - bytes:
        - None: Indication that the data has arrived and could not be converted to the desired type
        """
        match mode:
            case Mode.JSON:
                try:
                    message = await sender.receive_json()
                except JSONDecodeError:
                    return None
            case Mode.TEXT:
                message = await sender.receive_text()
            case Mode.BYTE:
                message = await sender.receive_bytes()
            case _:
                raise "Mode is invalid"

        if validator is not None:
            message = validator(message)

        return message
