from pydantic import BaseModel
from typing import Optional


class UserUpdateSchema(BaseModel):
    login: Optional[str] = None
    password: Optional[str] = None
