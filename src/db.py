import os
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession as SQLAlchemyAsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from .config import settings

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker




Base = declarative_base()


engine = create_async_engine(
    settings.DATABASE.url,
    echo=settings.DEBUG,
    connect_args={"server_settings": {"jit": "off"}},
)
async_session_factory = async_sessionmaker(
    engine,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator[SQLAlchemyAsyncSession, None]:
    async_session = async_session_factory()
    async with async_session, async_session.begin():
        yield async_session
