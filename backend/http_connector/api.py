from http_connector.base import HTTPConnectorBase


class HTTPConnectorAPI(HTTPConnectorBase):

    async def get_messages(self):
        data = await self.request("GET", "/messages")
        return data

    async def create_message(self,
                             text: str,
                             username: str
                             ):
        data = await self.request("POST", "/message", json={"text": text, "username": username})
        return data
