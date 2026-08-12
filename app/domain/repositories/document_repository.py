from abc import ABC
from abc import abstractmethod
from uuid import UUID

from app.domain.entities.document import Document


class IDocumentRepository(ABC):

    @abstractmethod
    async def save(
        self,
        document: Document,
    ) -> None:
        """
        Persist a document.
        """

    @abstractmethod
    async def get_by_id(
        self,
        document_id: UUID,
    ) -> Document | None:
        """
        Fetch document by id.
        """

    @abstractmethod
    async def exists_by_checksum(
        self,
        checksum: str,
    ) -> bool:
        """
        Detect duplicate document.
        """

    @abstractmethod
    async def update(
        self,
        document: Document,
    ) -> None:
        """
        Update document.
        """
