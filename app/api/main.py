from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, tasks
from app.models.base import Base
from app.db.session import engine
from app.core.config import Settings
from app.core.redis import redis_client
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

app = FastAPI()

# Подключение сервера redis для хранения кэша
FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")

# Подключение маршрутов    
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Task API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)