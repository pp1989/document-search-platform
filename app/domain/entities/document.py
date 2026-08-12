from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.domain.enums.document_status import DocumentStatus


@dataclass(slots=True)
class Document:

    id: UUID

    filename: str

    original_filename: str

    mime_type: str

    size: int

    checksum: str

    storage_path: str

    status: DocumentStatus

    created_at: datetime

    updated_at: datetime
