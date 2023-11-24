from pydantic import BaseModel


class UserSignUp(BaseModel):
    login: str
    password: str
