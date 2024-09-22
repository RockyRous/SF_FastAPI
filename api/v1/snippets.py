from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from schemas.snippet import SnippetCreate
from services.snippet_service import create_snippet
from core.security import get_current_user

router = APIRouter()


@router.post("/snippets/")
async def create_snippet_endpoint(
        snippet: SnippetCreate,
        db: AsyncSession = Depends(get_db),
        current_user = Depends(get_current_user)
):
    # Эндпоинт доступен только авторизованным пользователям
    return await create_snippet(db, snippet, owner_id=current_user.id)
