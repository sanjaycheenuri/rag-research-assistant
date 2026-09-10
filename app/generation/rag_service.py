from app.generation.generator import RAGGenerator
from app.generation.llm import LLM
from app.retrieval.retriever import Retriever


class RAGService:
    """Complete retrieval-augmented generation pipeline."""

    def __init__(self):
        self.retriever = Retriever()
        self.generator = RAGGenerator()
        self.llm = LLM()

    def answer(self, query: str, top_k: int = 5) -> dict:
        """Retrieve relevant context and generate an answer."""

        # 1. Retrieve relevant chunks
        retrieved_chunks = self.retriever.retrieve(
            query=query,
            top_k=top_k
        )

        # 2. Build the RAG prompt
        prompt = self.generator.build_prompt(
            query=query,
            retrieved_chunks=retrieved_chunks
        )

        # 3. Generate answer
        answer = self.llm.generate(prompt)

        # 4. Return answer and sources
        sources = [
            {
                "page": chunk["metadata"].get("page"),
                "distance": chunk["distance"]
            }
            for chunk in retrieved_chunks
        ]

        return {
            "answer": answer,
            "sources": sources
        }