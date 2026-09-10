def chunk_text(
    pages: list[dict],
    chunk_size: int = 1000,
    overlap: int = 200
) -> list[dict]:
    """
    Split extracted PDF text into overlapping chunks.
    """

    chunks = []

    for page in pages:
        text = page["text"]
        page_number = page["page"]

        start = 0

        while start < len(text):
            end = start + chunk_size

            chunk = text[start:end].strip()

            if chunk:
                chunks.append({
                    "page": page_number,
                    "text": chunk
                })

            start += chunk_size - overlap

    return chunks