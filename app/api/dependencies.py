from app.domain.services.health_service import HealthService
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database.session import get_db
from app.domain.repositories.interfaces.health_repository import (IHealthRepository)

def get_health_service( db: AsyncSession = Depends(get_db),):

       repository = IHealthRepository(db)
       return HealthService(repository)