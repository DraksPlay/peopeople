from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from .chat.router import router as chat_router


app = FastAPI()

app.add_middleware(SessionMiddleware, max_age=86400, secret_key="session_middleware")

app.include_router(chat_router)
