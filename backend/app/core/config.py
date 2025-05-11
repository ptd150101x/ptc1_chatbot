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
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "root")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "123")
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

    # Chat Provider settings
    CHAT_PROVIDER: str = os.getenv("CHAT_PROVIDER", "openai")

    # Embeddings settings
    EMBEDDINGS_PROVIDER: str = os.getenv("EMBEDDINGS_PROVIDER", "openai")

    # MinIO settings
    MINIO_ENDPOINT: str = os.getenv("MINIO_ENDPOINT", "localhost:9000")
    MINIO_ACCESS_KEY: str = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
    MINIO_SECRET_KEY: str = os.getenv("MINIO_SECRET_KEY", "minioadmin")
    MINIO_BUCKET_NAME: str = os.getenv("MINIO_BUCKET_NAME", "documents")

    # OpenAI settings
    OPENAI_API_BASE: str = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "your-openai-api-key-here")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4")
    OPENAI_EMBEDDINGS_MODEL: str = os.getenv("OPENAI_EMBEDDINGS_MODEL", "text-embedding-ada-002")

    # DashScope settings
    DASH_SCOPE_API_KEY: str = os.getenv("DASH_SCOPE_API_KEY", "")
    DASH_SCOPE_EMBEDDINGS_MODEL: str = os.getenv("DASH_SCOPE_EMBEDDINGS_MODEL", "")

    # Vector Store settings
    VECTOR_STORE_TYPE: str = os.getenv("VECTOR_STORE_TYPE", "chroma")

    # Chroma DB settings
    CHROMA_DB_HOST: str = os.getenv("CHROMA_DB_HOST", "chromadb")
    CHROMA_DB_PORT: int = int(os.getenv("CHROMA_DB_PORT", "8000"))

    # Qdrant DB settings
    QDRANT_URL: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    QDRANT_PREFER_GRPC: bool = os.getenv("QDRANT_PREFER_GRPC", "true").lower() == "true"

    # Deepseek settings
    DEEPSEEK_API_KEY: str = ""
    DEEPSEEK_API_BASE: str = "https://api.deepseek.com/v1"  # 默认 API 地址
    DEEPSEEK_MODEL: str = "deepseek-chat"  # 默认模型名称

    # Ollama settings
    OLLAMA_API_BASE: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "deepseek-r1:7b"
    OLLAMA_EMBEDDINGS_MODEL: str = os.getenv(
        "OLLAMA_EMBEDDINGS_MODEL", "nomic-embed-text"
    )  # Added this line

    class Config:
        env_file = ".env"


settings = Settings()
