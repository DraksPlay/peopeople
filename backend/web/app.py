from fastapi import FastAPI

from .message.router import router as message_router


app = FastAPI()


app.include_router(message_router)
