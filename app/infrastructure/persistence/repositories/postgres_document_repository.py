"""
PostgreSQL implementation of the document repository.
"""

from __future__ import annotations

from uuid import UUID

from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.document import Document
from app.domain.repositories.document_repository import (
    IDocumentRepository,
)
from app.infrastructure.persistence.mappers.document_mapper import (
    DocumentMapper,
)
from app.infrastructure.persistence.models.document_model import (
    DocumentModel,
)
from app.infrastructure.persistence.repositories.base_repository import (
    BaseRepository,
)


class PostgresDocumentRepository(
    BaseRepository[DocumentModel],
    IDocumentRepository,
):
    """
    PostgreSQL implementation of IDocumentRepository.
    """

    def __init__(
        self,
        session: AsyncSession,
    ) -> None:

        super().__init__(session)

    async def save(
        self,
        document: Document,
    ) -> None:
        """
        Persist a new document.
        """

        model = DocumentMapper.to_model(document)

        await self.add(model)

        await self.commit()

        logger.info(
            "Document persisted successfully. id={}",
            document.id,
        )

    async def get_by_id(
        self,
        document_id: UUID,
    ) -> Document | None:
        """
        Retrieve document by id.
        """

        statement = select(DocumentModel).where(DocumentModel.id == document_id)

        result = await self.session.execute(statement)

        model = result.scalar_one_or_none()

        if model is None:
            return None

        return DocumentMapper.to_entity(model)

    async def exists_by_checksum(
        self,
        checksum: str,
    ) -> bool:
        """
        Check whether a document already exists.
        """

        statement = select(DocumentModel.id).where(DocumentModel.checksum == checksum)

        result = await self.session.execute(statement)

        return result.scalar_one_or_none() is not None

    async def update(
        self,
        document: Document,
    ) -> None:
        """
        Update an existing document.
        """

        statement = select(DocumentModel).where(DocumentModel.id == document.id)

        result = await self.session.execute(statement)

        model = result.scalar_one()

        model.filename = document.filename
        model.original_filename = document.original_filename
        model.mime_type = document.mime_type
        model.size = document.size
        model.storage_path = document.storage_path
        model.status = document.status
        model.checksum = document.checksum

        await self.commit()

        logger.info(
            "Document updated successfully. id={}",
            document.id,
        )
