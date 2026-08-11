from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logger import configure_logging


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger = configure_logging()

    logger.info("Starting Document Search Platform...")

    #
    # Future startup
    #
    # PostgreSQL
    # PGVector
    # Ollama
    # Phoenix
    # Redis
    #

    yield

    logger.info("Stopping application...")