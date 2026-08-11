from fastapi import FastAPI

from app.api.v1.router import router
from app.core.config import get_settings
from app.core.lifespan import lifespan
from app.middleware.request_id import RequestIDMiddleware
from app.core.exceptions import (
    AppException,
    app_exception_handler,
)


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)
app.include_router(router)
app.add_exception_handler(AppException,app_exception_handler,)
app.add_middleware(RequestIDMiddleware)