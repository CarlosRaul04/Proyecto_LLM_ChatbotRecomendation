import chromadb
from loguru import logger

chroma_client = chromadb.Client()


class CollectionSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.collection = chroma_client.create_collection(
                name="sw_qa"
            )
            logger.info(f'Collection created!: {cls._instance.collection}')
        return cls._instance


collection = CollectionSingleton().collection
