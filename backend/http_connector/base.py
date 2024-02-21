import aiohttp
from typing import Any


class HTTPConnectorBase:

    def __init__(self,
                 base_url: str
                 ) -> None:
        self.base_url = base_url

    async def request(self,
                      method: str,
                      endpoint: str,
                      json: Any | None = None,
                      params: dict | None = None
                      ) -> Any:
        async with aiohttp.ClientSession() as session:
            async with session.request(method, f'{self.base_url}{endpoint}', json=json, params=params) as response:
                data = await response.json()
                return data
