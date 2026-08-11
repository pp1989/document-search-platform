from abc import ABC, abstractmethod


class IDocumentRepository(ABC):

    @abstractmethod
    async def exists_by_checksum(self,

        checksum: str,

    ):

        pass

    @abstractmethod
    async def save_document(self,):

        pass