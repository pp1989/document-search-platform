"""
Mapper between Domain Document entity and SQLAlchemy DocumentModel.
"""

from __future__ import annotations

from app.domain.entities.document import Document
from app.infrastructure.persistence.models.document_model import (
    DocumentModel,
)


class DocumentMapper:
    """
    Converts between Domain Entity and ORM Model.

    Domain <-------> Infrastructure
    """

    @staticmethod
    def to_model(
        entity: Document,
    ) -> DocumentModel:
        """
        Convert Domain Entity
        into SQLAlchemy ORM model.
        """

        return DocumentModel(
            id=entity.id,
            filename=entity.filename,
            original_filename=entity.original_filename,
            mime_type=entity.mime_type,
            size=entity.size,
            checksum=entity.checksum,
            storage_path=entity.storage_path,
            status=entity.status,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    @staticmethod
    def to_entity(
        model: DocumentModel,
    ) -> Document:
        """
        Convert SQLAlchemy model
        into Domain Entity.
        """

        return Document(
            id=model.id,
            filename=model.filename,
            original_filename=model.original_filename,
            mime_type=model.mime_type,
            size=model.size,
            checksum=model.checksum,
            storage_path=model.storage_path,
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
