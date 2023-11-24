from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.config import API_URL
from client.messanger.router import router as messanger_router
from client.auth.router import router as auth_router


app = FastAPI(docs_url=API_URL, openapi_url="")

app.mount("/static", StaticFiles(directory="client/static"), name="static")


app.include_router(messanger_router)
app.include_router(auth_router)
