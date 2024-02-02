from pydantic import BaseModel


class MessageCreateSchema(BaseModel):
    text: str
