from fastapi import FastAPI

from src.config import API_URL

from config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASS


app = FastAPI(docs_url=API_URL)


@app.get("/user")
async def get_user():
    pass