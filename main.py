from fastapi import FastAPI
from db.database import init_db
from api import router as api_router  # Импортируйте роутер
import uvicorn

app = FastAPI()

# Подключение к базе данных при запуске приложения
@app.on_event("startup")
async def startup():
    await init_db()

# Добавляем маршруты
app.include_router(api_router, prefix="/api/v1")  # Добавьте префикс, если нужно

# Тестовый эндпоинт для проверки работы приложения
@app.get("/")
async def read_root():
    return {"message": "Snippet API is running"}

# Точка входа в приложение
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
