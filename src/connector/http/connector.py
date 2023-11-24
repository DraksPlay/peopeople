from httpx import AsyncClient, Response
from typing import Any

class HTTPConnector:

    def __init__(self,
                 base_url: str = ""
                 ):
        self.base_url = base_url

    async def request(self,
                      method: str,
                      url: str,
                      json: Any | None = None,
                      params: dict | None = None
                      ) -> Response:
        async with AsyncClient() as client:
            response = await client.request(method, self.base_url + url, json=json, params=params)
            return response

    async def get_request(self,
                          url: str
                          ) -> Response:
        response = await self.request("GET", url)
        return response

    async def post_request(self,
                           url: str,
                           json: Any | None = None,
                           params: dict | None = None
                           ) -> Response:
        response = await self.request("POST", url, json=json, params=params)
        return response
