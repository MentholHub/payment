import asyncio
import logging

from fastapi import FastAPI

from src.payment import router as payment_router

from .db import Base, engine

app = FastAPI(
    title="Async Wallet API",
    description="Digital wallet service with async support",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


# Инициализация базы данных
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def on_startup():
    await init_db()
    logging.info("Database initialized")


# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("app.log")],
)

# Подключение роутера
app.include_router(payment_router, prefix="/api/v1")


@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Async Wallet API is running"}
