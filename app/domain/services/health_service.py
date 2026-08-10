from datetime import datetime, timezone
from app.domain.repositories.interfaces.health_repository import (IHealthRepository,)

class HealthService:
    
    def __init__(self, repository: IHealthRepository):
        self.repository = repository

    async def get_status(self):
        return {
            "status": "healthy",
            "time": datetime.now(timezone.utc),
            "service": "Document Search Platform",
        }