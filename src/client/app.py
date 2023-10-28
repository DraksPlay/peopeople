from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.config import API_URL
from client.messanger.router import router as messanger_router


app = FastAPI(docs_url=API_URL, openapi_url="")

# app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(messanger_router)
