import logging
from contextlib import asynccontextmanager

from app.api.api_v1.api import api_router
from app.api.openapi.api import router as openapi_router
from app.core.config import settings
from app.core.minio import init_minio
from app.startup.migarate import DatabaseMigrator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_minio()
    migrator = DatabaseMigrator(settings.get_database_url)
    migrator.run_migrations()
    logging.info("Startup event: MinIO initialized and migrations run.")
    yield
    logging.info("Shutdown event.")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả origins trong môi trường phát triển
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả methods
    allow_headers=["*"],  # Cho phép tất cả headers
)

# Include routers
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(openapi_router, prefix="/openapi")


@app.get("/")
def root():
    return {"message": "Welcome to RAG Web UI API"}


@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "version": settings.VERSION,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
