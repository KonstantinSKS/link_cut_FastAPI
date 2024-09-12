from fastapi import FastAPI
from contextlib import asynccontextmanager

import uvicorn

from app.endpoints import router
from app.config import settings
from app.db import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan,
              title=settings.app_title)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=True
    )
