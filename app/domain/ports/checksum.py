from abc import ABC
from abc import abstractmethod
from pathlib import Path


class IChecksumService(ABC):

    @abstractmethod
    async def calculate(
        self,
        file_path: Path,
    ) -> str:
        """
        Calculate checksum.
        """
