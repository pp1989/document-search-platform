from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import get_settings

settings = get_settings()

DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{settings.postgres_user}:"
    f"{settings.postgres_password}@"
    f"{settings.postgres_host}:"
    f"{settings.postgres_port}/"
    f"{settings.postgres_db}"
)
print(f"Database URL:=======================> {DATABASE_URL}")
engine = create_async_engine(
    DATABASE_URL,
    echo=settings.debug,
    future=True,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            # This ensures the session closes even if your API route crashes
            await session.close()
# async def get_db():

#     async with AsyncSessionLocal() as session:

#         yield session
