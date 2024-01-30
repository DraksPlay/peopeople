from fastapi import FastAPI

from .message import message_router


app = FastAPI()


app.include_router(message_router)
