from fastapi import APIRouter, Depends
from app.api.dependencies import get_health_service
from app.schemas.base import ApiResponse
from app.domain.services.health_service import HealthService

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    response_model=ApiResponse,
)
async def health(service: HealthService = Depends(get_health_service)):

    result = await service.get_status()

    return ApiResponse(
        success=True,
        message="Health check successful",
        data=result,
    )
