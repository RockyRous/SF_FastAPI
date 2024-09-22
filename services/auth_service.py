from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user import User
from core.security import verify_password, create_access_token
from datetime import timedelta
from fastapi import HTTPException, status
from schemas.auth import Token


async def authenticate_user(db: AsyncSession, username: str, password: str):
    # Используем ORM-запрос для поиска пользователя по username
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalars().first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


async def login_user(db: AsyncSession, username: str, password: str) -> Token:
    user = await authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Создаем JWT-токен
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
