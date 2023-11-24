from httpx import Response

from connector.http import HTTPConnector
from config import SERVER_HOST, SERVER_PORT, SERVER_URL
from schemas.server import auth as auth_schema


class ServerHTTPConnector(HTTPConnector):

    def __init__(self):
        base_url = f"http://{SERVER_HOST}:{SERVER_PORT}"
        super().__init__(base_url)

    async def auth_signup(self,
                          new_user_data: auth_schema.UserSignUp
                          ) -> Response:
        response = await self.post_request(f"/signup", json=dict(new_user_data))
        return response
