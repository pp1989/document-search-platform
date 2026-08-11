from abc import ABC
from abc import abstractmethod


class DocumentParser(ABC):

    @abstractmethod
    async def parse(self, file_path: str):

        """
        Parse a document and return
        structured content.
        """