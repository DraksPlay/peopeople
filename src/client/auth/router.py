from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from connector.connects.http.server import ServerHTTPConnector
from schemas.server import auth as auth_schemas


router = APIRouter()

templates = Jinja2Templates(directory="client/templates")


@router.get("/signup")
async def sign_up_get(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@router.post("/signup")
async def sign_up_post(request: Request,
                       server_coon: ServerHTTPConnector = Depends(ServerHTTPConnector)):
    form_data = await request.form()
    login = form_data.get("login")
    password = form_data.get("password")
    new_user_data = auth_schemas.UserSignUp(login=login, password=password)
    await server_coon.auth_signup(new_user_data)
    return templates.TemplateResponse("signup.html", {"request": request})
