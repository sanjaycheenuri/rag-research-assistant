import chromadb


class VectorStore:
    """Store and search document embeddings using ChromaDB."""

    def __init__(self, collection_name: str = "research_papers"):
        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(
        self,
        ids: list[str],
        texts: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict]
    ):
        """Add document chunks and their embeddings."""

        self.collection.add(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(
        self,
        query_embedding: list[float],
        top_k: int = 5
    ):
        """Find the most relevant document chunks."""

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )