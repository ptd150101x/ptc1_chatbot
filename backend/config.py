import os
from typing import List, Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "RAG Web UI"  # Project name
    VERSION: str = "0.1.0"  # Project version
    API_V1_STR: str = "/api"  # API version string

    # PostgreSQL settings
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "abc")
    POSTGRES_DATABASE: str = os.getenv("POSTGRES_DATABASE", "chatbot")
    SQLALCHEMY_DATABASE_URI: Optional[str] = None


    @property
    def get_database_url(self) -> str:
        if self.SQLALCHEMY_DATABASE_URI:
            return self.SQLALCHEMY_DATABASE_URI
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DATABASE}"
        )




    # JWT settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "10080"))

    # MinIO settings
    MINIO_ENDPOINT: str = os.getenv("MINIO_ENDPOINT", "localhost:9000")
    MINIO_ACCESS_KEY: str = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
    MINIO_SECRET_KEY: str = os.getenv("MINIO_SECRET_KEY", "minioadmin")
    MINIO_BUCKET_NAME: str = os.getenv("MINIO_BUCKET_NAME", "documents")




    # FLagEmbedding settings
    EMBEDDINGS_PROVIDER: str = os.getenv("EMBEDDINGS_PROVIDER", "flag")
    FLAG_EMBEDDINGS_MODEL: str = os.getenv("FLAG_EMBEDDINGS_MODEL", "BAAI/bge-m3")
    FLAG_EMBEDDINGS_USE_FP16: bool = os.getenv("FLAG_EMBEDDINGS_USE_FP16", "true").lower() == "true"
    FLAG_EMBEDDINGS_DEVICE: Optional[str] = os.getenv("FLAG_EMBEDDINGS_DEVICE", None)
    FLAG_EMBEDDINGS_BATCH_SIZE: int = int(os.getenv("FLAG_EMBEDDINGS_BATCH_SIZE", "64"))
    FLAG_EMBEDDINGS_MAX_LENGTH: int = int(os.getenv("FLAG_EMBEDDINGS_MAX_LENGTH", "8192"))
    
    
    
    # Chat Provider settings
    CHAT_PROVIDER: str = os.getenv("CHAT_PROVIDER", "openai")

    # OpenAI settings
    OPENAI_API_BASE: str = os.getenv("OPENAI_API_BASE", "https://localhost:8008/v1")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "api-key")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "AITeamVN/Vi-Qwen2-3B-RAG")
    
    # Vector Store settings
    VECTOR_STORE_TYPE: str = os.getenv("VECTOR_STORE_TYPE", "psql")

    # Chroma DB settings
    CHROMA_DB_HOST: str = os.getenv("CHROMA_DB_HOST", "http://localhost:8002")
    CHROMA_DB_PORT: int = int(os.getenv("CHROMA_DB_PORT", "8002"))

    # Qdrant DB settings
    QDRANT_URL: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    QDRANT_PREFER_GRPC: bool = os.getenv("QDRANT_PREFER_GRPC", "true").lower() == "true"

    # PSQL Vector Store settings
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "abc")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "chatbot")
    
    # FE settings
    NEXT_PUBLIC_API_URL: str = os.getenv("NEXT_PUBLIC_API_URL", "http://localhost:8000")
    class Config:
        env_file = ".env"


settings = Settings()
