import aiohttp
from typing import Any


class Connector:

    def __init__(self,
                 base_url: str
                 ) -> None:
        self.base_url = base_url

    async def request(self,
                      method: str,
                      endpoint: str,
                      json: Any | None = None,
                      params: dict | None = None
                      ):
        async with aiohttp.ClientSession() as session:
            async with session.request(method, f'{self.base_url}{endpoint}', json=json, params=params) as response:
                data = await response.json()
                return data

    async def get_messages(self):
        data = await self.request("GET", "/messages")
        return data

    async def create_message(self, text: str):
        data = await self.request("POST", "/message", json={"text": text})
        return data
