from typing import List, Any
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_community.vectorstores import PGVector
from config import settings

from .base import BaseVectorStore

class PostgresVectorStore(BaseVectorStore):
    """PostgreSQL vector store implementation using pgvector"""
    
    def __init__(self, collection_name: str, embedding_function: Embeddings, **kwargs):
        """Initialize PostgreSQL vector store"""
        connection_string = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
        
        self._store = PGVector(
            collection_name=collection_name,
            embeddings=embedding_function,
            connection_string=connection_string,
            **kwargs
        )
    
    def add_documents(self, documents: List[Document]) -> None:
        """Add documents to PostgreSQL"""
        self._store.add_documents(documents)
    
    def delete(self, ids: List[str]) -> None:
        """Delete documents from PostgreSQL"""
        self._store.delete(ids)
    
    def as_retriever(self, **kwargs: Any):
        """Return a retriever interface"""
        return self._store.as_retriever(**kwargs)
    
    def similarity_search(self, query: str, k: int = 4, **kwargs: Any) -> List[Document]:
        """Search for similar documents in PostgreSQL"""
        return self._store.similarity_search(query, k=k, **kwargs)
    
    def similarity_search_with_score(self, query: str, k: int = 4, **kwargs: Any) -> List[Document]:
        """Search for similar documents in PostgreSQL with score"""
        return self._store.similarity_search_with_score(query, k=k, **kwargs)

    def delete_collection(self) -> None:
        """Delete the entire collection"""
        self._store.delete_collection()