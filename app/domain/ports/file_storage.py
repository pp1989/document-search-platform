from abc import ABC
from abc import abstractmethod
from pathlib import Path


class IFileStorage(ABC):

    @abstractmethod
    async def save(
        self,
        source_path: Path,
        destination_name: str,
    ) -> Path:
        """
        Store a file.
        """

    @abstractmethod
    async def delete(
        self,
        path: Path,
    ) -> None:
        """
        Delete file.
        """

    @abstractmethod
    async def exists(
        self,
        path: Path,
    ) -> bool:
        """
        Check existence.
        """
