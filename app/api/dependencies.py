from app.domain.services.health_service import HealthService
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database.session import get_db
from app.infrastructure.repositories.health_repository import HealthRepository


def get_health_service( db: AsyncSession = Depends(get_db),):
       print(f"db=====>: {db}")
       repository = HealthRepository(db)
       return HealthService(repository)