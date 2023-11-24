from fastapi import FastAPI

from src.config import SERVER_URL
from server.users.router import router as users_router
from server.auth.router import router as auth_router

app = FastAPI(docs_url=SERVER_URL, openapi_url="")

app.include_router(users_router, tags=["User"])
app.include_router(auth_router, tags=["Auth"])
