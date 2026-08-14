"""
Database session factory.

Responsible for creating SQLAlchemy AsyncSession
instances for each unit of work.
"""

from __future__ import annotations

from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
)

from app.infrastructure.persistence.database import engine

# ----------------------------------------------------------------------
# Session Factory
# ----------------------------------------------------------------------

SessionFactory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


# ----------------------------------------------------------------------
# Session Provider
# ----------------------------------------------------------------------


async def create_session() -> AsyncIterator[AsyncSession]:
    """
    Create a database session.

    The caller owns the transaction.
    The session is automatically closed.
    """

    async with SessionFactory() as session:

        yield session