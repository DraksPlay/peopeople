from fastapi import FastAPI

from src.config import API_URL
from api.users.router import router as users_router

app = FastAPI(docs_url=API_URL, openapi_url="")

app.include_router(users_router, prefix=API_URL, tags=["User"], include_in_schema=False)
