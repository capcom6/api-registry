import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles

from .router import router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.debug("Lifespan started")
    yield
    logger.debug("Lifespan finished")


server = FastAPI(lifespan=lifespan)


server.add_middleware(GZipMiddleware)

server.include_router(router)

server.mount("/", StaticFiles(directory="static", html=False), name="static")

__all__ = ["server"]
