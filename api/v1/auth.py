from schemas.auth import Login, Token
from services.auth_service import login_user
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/login", response_model=Token)
async def login_for_access_token(login_data: Login, db: AsyncSession = Depends(get_db)):
    # Вызовем сервис для логина
    return await login_user(db, login_data.username, login_data.password)



# Для Authorize
@router.post("/token", response_model=Token)
async def token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                db: AsyncSession = Depends(get_db)):
    return await login_user(db, form_data.username, form_data.password)




