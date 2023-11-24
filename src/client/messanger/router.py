from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()

templates = Jinja2Templates(directory="client/templates")


@router.get("/")
async def messanger_main(request: Request):
    return templates.TemplateResponse("messanger_main.html", {"request": request})
