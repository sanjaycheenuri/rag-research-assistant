from app.generation.rag_service import RAGService


def main():
    rag = RAGService()

    question = input("Ask a question: ")

    result = rag.answer(question)

    print("\n=== ANSWER ===")
    print(result["answer"])

    print("\n=== SOURCES ===")

    for source in result["sources"]:
        print(
            f"Page: {source['page']} | "
            f"Distance: {source['distance']:.4f}"
        )


if __name__ == "__main__":
    main()