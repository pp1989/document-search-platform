"""
Database engine configuration.

This module owns the application's SQLAlchemy engine.
It is responsible only for creating and disposing the engine.
"""

from __future__ import annotations

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
)

from app.core.config import get_settings

settings = get_settings()


def build_database_url() -> str:
    """
    Build the SQLAlchemy async database URL.

    Returns:
        PostgreSQL async connection string.
    """

    return (
        "postgresql+asyncpg://"
        f"{settings.postgres_user}:"
        f"{settings.postgres_password}"
        f"@{settings.postgres_host}:"
        f"{settings.postgres_port}/"
        f"{settings.postgres_db}"
    )


DATABASE_URL = build_database_url()


engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    echo=settings.debug,
    future=True,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
)


async def dispose_engine() -> None:
    """
    Gracefully dispose all pooled connections.

    Called during application shutdown.
    """

    await engine.dispose()
