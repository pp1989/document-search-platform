from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import JSONB

from pgvector.sqlalchemy import Vector

from app.infrastructure.persistence.base import Base


class DocumentChunk(Base):

    __tablename__ = "document_chunks"

    id: Mapped[int] = mapped_column(primary_key=True)

    document_id: Mapped[int] = mapped_column(
        ForeignKey("documents.id")
    )

    chunk_index: Mapped[int]

    page_number: Mapped[int]

    content: Mapped[str]

    embedding: Mapped[list[float]] = mapped_column(
        Vector(768)
    )

    metadata: Mapped[dict] = mapped_column(
        JSONB
    )