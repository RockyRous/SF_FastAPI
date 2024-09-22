from fastapi import APIRouter
from .v1.auth import router as auth_router
from .v1.snippets import router as snippets_router
from .v1.users import router as users_router

router = APIRouter()

# Регистрируем роутеры
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(snippets_router, prefix="/snippets", tags=["snippets"])
router.include_router(users_router, prefix="/users", tags=["users"])

