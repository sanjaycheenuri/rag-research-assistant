import fitz


def extract_text_from_pdf(file_path: str) -> list[dict]:
    """
    Extract text from a PDF while preserving page numbers.
    """

    document = fitz.open(file_path)
    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text("text").strip()

        if text:
            pages.append({
                "page": page_number,
                "text": text
            })

    document.close()

    return pages


if __name__ == "__main__":
    pdf_path = "data/documents/sample.pdf"

    pages = extract_text_from_pdf(pdf_path)

    print(f"Extracted {len(pages)} pages.")

    for page in pages[:2]:
        print(f"\n--- Page {page['page']} ---")
        print(page["text"][:1000])