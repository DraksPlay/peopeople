from fastapi import FastAPI

from src.config import API_URL
from api.users.router import router as users_router

app = FastAPI(docs_url=API_URL, title="PeoPeoPle API")

app.include_router(users_router, prefix=API_URL, tags=["User"])
