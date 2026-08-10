from abc import ABC
from abc import abstractmethod

class IHealthRepository(ABC):
    @abstractmethod
    async def check_database(self):
        pass
    