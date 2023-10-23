from fastapi import FastAPI

from src.config import API_URL
from api.users.router import router as users_router
from api.friends.router import router as friends_router
from api.chats.router import router as chats_router
from api.chat_members.router import router as chat_members_router
from api.messages.router import router as messages_router

app = FastAPI(docs_url=API_URL, title="PeoPeoPle API")

app.include_router(users_router, prefix=API_URL, tags=["User"])
app.include_router(friends_router, prefix=API_URL, tags=["Friend"])
app.include_router(chats_router, prefix=API_URL, tags=["Chat"])
app.include_router(chat_members_router, prefix=API_URL, tags=["ChatMember"])
app.include_router(messages_router, prefix=API_URL, tags=["Message"])
