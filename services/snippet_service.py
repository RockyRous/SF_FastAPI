from sqlalchemy.ext.asyncio import AsyncSession
from models.snippet import Snippet
from schemas.snippet import SnippetCreate


async def create_snippet(db: AsyncSession, snippet: SnippetCreate, owner_id: int):
    db_snippet = Snippet(title=snippet.title, content=snippet.content, owner_id=owner_id)
    db.add(db_snippet)
    await db.commit()
    await db.refresh(db_snippet)
    return db_snippet
