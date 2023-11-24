from fastapi import APIRouter, Depends

from schemas.server.auth import UserSignUp
from .service import get_password_hash
from connector.connects.http.api import APIHTTPConnector

router = APIRouter()


@router.post("/signup")
async def signup(new_user_data: UserSignUp,
                 api_coon: APIHTTPConnector = Depends(APIHTTPConnector)):
    password_hash = await get_password_hash(new_user_data.password)
    await api_coon.create_user(new_user_data.login, password_hash)
    return {'response': 1}
