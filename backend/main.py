from fastapi import FastAPI
from config import settings
from router.auth import router as auth_router
from router.knowledge_base import router as knowledge_base_router
import logging
from contextlib import asynccontextmanager
from migrate import DatabaseMigrator
from fastapi.middleware.cors import CORSMiddleware



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # init_minio()
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://10.6.0.42:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Bao gồm routers
app.include_router(auth_router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(knowledge_base_router, prefix=f"{settings.API_V1_STR}/knowledge-base", tags=["knowledge-base"])
@app.get("/")
def root():
    return {"message": "Chào mừng đến với API của ứng dụng chatbot"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)