class RAGGenerator:
    """Generate answers using retrieved research context."""

    def build_prompt(
        self,
        query: str,
        retrieved_chunks: list[dict]
    ) -> str:
        context_parts = []

        for chunk in retrieved_chunks:
            page = chunk["metadata"].get("page", "unknown")

            context_parts.append(
                f"[Page {page}]\n{chunk['text']}"
            )

        context = "\n\n".join(context_parts)

        prompt = f"""
You are a research assistant.

Answer the user's question using ONLY the provided context.

If the context does not contain enough information,
clearly say that the answer cannot be determined
from the provided research papers.

Always mention the supporting page numbers.

Context:
{context}

Question:
{query}

Answer:
"""

        return prompt.strip()