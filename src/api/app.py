from fastapi import FastAPI

from src.config import API_URL


app = FastAPI(docs_url=API_URL)


@app.get("")
async def get_user():
    pass