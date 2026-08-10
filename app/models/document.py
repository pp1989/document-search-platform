from datetime import datetime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.infrastructure.database.base import Base

class Document(Base):

    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)

    filename: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    mime_type: Mapped[str]

    checksum: Mapped[str]

    size: Mapped[int]

    status: Mapped[str]

    created_at: Mapped[datetime]

    updated_at: Mapped[datetime]
