from typing import List
from langchain_core.embeddings import Embeddings
from FlagEmbedding import BGEM3FlagModel
import numpy as np


class FlagEmbeddings(Embeddings):
    """
    Custom embeddings class that uses FlagEmbedding BGEM3FlagModel directly
    """
    
    def __init__(
        self, 
        model_name: str = 'BAAI/bge-m3',
        use_fp16: bool = True,
        device: str = None,
        batch_size: int = 64,
        max_length: int = 8192
    ):
        self.model_name = model_name
        self.batch_size = batch_size
        self.max_length = max_length
        
        # Initialize the model
        if device == "cpu":
            self.model = BGEM3FlagModel(model_name, use_fp16=False, device="cpu")
        else:
            self.model = BGEM3FlagModel(model_name, use_fp16=use_fp16)
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of documents"""
        return self._embed_texts(texts)
    
    def embed_query(self, text: str) -> List[float]:
        """Embed a single query text"""
        result = self._embed_texts([text])
        return result[0] if result else []
    
    def _embed_texts(self, texts: List[str]) -> List[List[float]]:
        """Internal method to embed texts using BGEM3FlagModel"""
        try:
            # Use the model to encode texts
            embeddings = self.model.encode(
                texts,
                batch_size=self.batch_size,
                max_length=self.max_length,
                return_dense=True,
                return_sparse=False,
                return_colbert_vecs=False
            )
            
            # Extract dense vectors and convert to list
            dense_vecs = embeddings["dense_vecs"]
            return np.array(dense_vecs, dtype=np.float32).tolist()
            
        except Exception as e:
            raise RuntimeError(f"Failed to get embeddings from FlagEmbedding: {str(e)}")