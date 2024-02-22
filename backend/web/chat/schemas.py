from pydantic import BaseModel


class Message(BaseModel):
    text: str
    username: str
