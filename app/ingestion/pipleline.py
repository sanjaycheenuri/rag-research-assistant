from app.ingestion.pdf_loader import extract_text_from_pdf
from app.retrieval.chunker import chunk_text
from app.retrieval.embedder import Embedder
from app.retrieval.vector_store import VectorStore


class IngestionPipeline:
    """Process a PDF and store its content for retrieval."""

    def __init__(self):
        self.embedder = Embedder()
        self.vector_store = VectorStore()

    def ingest(self, file_path: str):
        # 1. Extract text
        pages = extract_text_from_pdf(file_path)

        # 2. Create chunks
        chunks = chunk_text(pages)

        # 3. Generate embeddings
        texts = [chunk["text"] for chunk in chunks]
        embeddings = self.embedder.encode(texts)

        # 4. Prepare metadata and IDs
        ids = [
            f"chunk_{index}"
            for index in range(len(chunks))
        ]

        metadatas = [
            {"page": chunk["page"]}
            for chunk in chunks
        ]

        # 5. Store in vector database
        self.vector_store.add_documents(
            ids=ids,
            texts=texts,
            embeddings=embeddings,
            metadatas=metadatas
        )

        return {
            "pages": len(pages),
            "chunks": len(chunks)
        }