from pydantic import BaseModel
from typing import Optional


class MessageUpdateSchema(BaseModel):
    text: Optional[str] = None
