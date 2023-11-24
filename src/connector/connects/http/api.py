from httpx import Response

from connector.http import HTTPConnector
from config import API_HOST, API_PORT, API_URL


class APIHTTPConnector(HTTPConnector):

    def __init__(self):
        base_url = f"http://{API_HOST}:{API_PORT}"
        super().__init__(base_url)

    async def create_user(self,
                          login: str,
                          password: str
                          ) -> Response:
        params = {"login": login, "password": password}
        response = await self.post_request(f"{API_URL}/user", params=params)
        return response
