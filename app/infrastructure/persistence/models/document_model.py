"""
SQLAlchemy ORM model representing a document.
"""

from __future__ import annotations

import uuid

from sqlalchemy import BigInteger
from sqlalchemy import Enum
from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.domain.enums.document_status import DocumentStatus
from app.infrastructure.persistence.models.base import Base
from app.infrastructure.persistence.models.base import TimestampMixin


class DocumentModel(Base, TimestampMixin):
    """
    ORM model mapped to the documents table.
    """

    __tablename__ = "documents"

    __table_args__ = (
        Index("ix_documents_checksum", "checksum"),
        Index("ix_documents_status", "status"),
        Index("ix_documents_created_at", "created_at"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    mime_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    checksum: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=True,
    )

    storage_path: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    status: Mapped[DocumentStatus] = mapped_column(
        Enum(
            DocumentStatus,
            name="document_status",
        ),
        nullable=False,
    )