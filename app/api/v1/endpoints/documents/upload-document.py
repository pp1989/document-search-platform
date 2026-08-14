from fastapi.params import Depends
from starlette.datastructures import UploadFile
from app.api.v1 import router
from app.domain.services.upload_service import UploadService

upload_service = UploadService()


@router.post(
    "/documents/upload",
    status_code=202,
)
async def upload(
    file: UploadFile, service: UploadService = Depends(lambda: upload_service)
):

    return await service.upload(file)
