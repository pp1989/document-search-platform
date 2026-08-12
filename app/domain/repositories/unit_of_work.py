"""
Unit of Work abstraction.

The Unit of Work coordinates one business transaction
across one or more repositories.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from app.domain.repositories.document_repository import (
    IDocumentRepository,
)


class IUnitOfWork(ABC):
    """
    Coordinates repositories participating in
    a single transaction.
    """

    @property
    @abstractmethod
    def documents(self) -> IDocumentRepository:
        """
        Access the document repository.
        """
        raise NotImplementedError

    @abstractmethod
    async def commit(self) -> None:
        """
        Commit the current transaction.
        """
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        """
        Roll back the current transaction.
        """
        raise NotImplementedError

    async def __aenter__(self) -> "IUnitOfWork":
        """
        Enter async context.
        """
        return self

    @abstractmethod
    async def __aexit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:
        """
        Exit async context.

        Implementations should commit on success
        and rollback on failure.
        """
        raise NotImplementedError
