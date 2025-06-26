from config import settings
from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_community.embeddings import DashScopeEmbeddings
# If you plan on adding other embeddings, import them here
from .flag_embedding import FlagEmbeddings




class EmbeddingsFactory:
    @staticmethod
    def create():
        """
        Factory method to create an embeddings instance based on .env config.
        """
        # Suppose your .env has a value like EMBEDDINGS_PROVIDER=openai
        embeddings_provider = settings.EMBEDDINGS_PROVIDER.lower()

        if embeddings_provider == "openai":
            return OpenAIEmbeddings(
                openai_api_key=settings.OPENAI_API_KEY,
                openai_api_base=settings.OPENAI_API_BASE,
                model=settings.OPENAI_EMBEDDINGS_MODEL
            )
        elif embeddings_provider == "dashscope":
            return DashScopeEmbeddings(
                model=settings.DASH_SCOPE_EMBEDDINGS_MODEL,
                dashscope_api_key=settings.DASH_SCOPE_API_KEY
            )
        elif embeddings_provider == "ollama":
            return OllamaEmbeddings(
                model=settings.OLLAMA_EMBEDDINGS_MODEL,
                base_url=settings.OLLAMA_API_BASE
            )

        # Extend with other providers:
        elif embeddings_provider == "flag":
            return FlagEmbeddings(
                model_name=getattr(settings, 'FLAG_EMBEDDINGS_MODEL', 'BAAI/bge-m3'),
                use_fp16=getattr(settings, 'FLAG_EMBEDDINGS_USE_FP16', True),
                device=getattr(settings, 'FLAG_EMBEDDINGS_DEVICE', None),
                batch_size=getattr(settings, 'FLAG_EMBEDDINGS_BATCH_SIZE', 64),
                max_length=getattr(settings, 'FLAG_EMBEDDINGS_MAX_LENGTH', 8192)
            )
        else:
            raise ValueError(f"Unsupported embeddings provider: {embeddings_provider}")