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

        yield session