from httpx import AsyncClient


class TestMessageRouter:

    async def test_create_message(self,
                                  ac: AsyncClient
                                  ):
        response = await ac.post("/message",
                                 json={"text": "text", "username": "test"})
        assert response.status_code == 200

    async def test_get_messages(self,
                                ac: AsyncClient
                                ):
        response = await ac.get("/messages")
        assert response.status_code == 200

        messages = response.json()
        assert len(messages) == 1
        message = messages[0]
        assert message.get("text") == "text"
        user = message.get("user")
        assert type(user) == dict
        assert user.get("name") == "test"
