from app.domain.repositories.document_repository import IDocumentRepository
from app.domain.repositories.unit_of_work import IUnitOfWork
from app.infrastructure.persistence.repositories.postgres_document_repository import (
    PostgresDocumentRepository,
)
from app.infrastructure.persistence.repositories.postgres_chunk_repository import (
    PostgresChunkRepository,
)
from sqlalchemy.ext.asyncio import AsyncSession


class PostgresUnitOfWork(IUnitOfWork):

    def __init__(self, session: AsyncSession, document_repository: IDocumentRepository = None, chunk_repository: PostgresChunkRepository = None):
        self.documents = document_repository or PostgresDocumentRepository(session)
        self.chunks = chunk_repository or PostgresChunkRepository(session)

        self._session = session
