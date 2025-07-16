\"\"\"Script to pull embeddings from Jina V4 API and push to Qdrant\"\"\"
from jina import Client
from qdrant_client import QdrantClient

def ingest():
    # TODO: call Jina API, transform responses to vectors, upsert to Qdrant
    pass

if __name__ == '__main__':
    ingest()
