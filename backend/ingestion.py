from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore


BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENTS_DIR = BASE_DIR / "data" / "documents"
QDRANT_PATH = BASE_DIR / "qdrant_data"

COLLECTION_NAME = "notes"


# 1. Initialize the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# 2. Configure the text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)


def ingest_all_pdfs():

    # Store chunks from every PDF in this list
    all_chunks = []

    # 3. Find every PDF in the documents folder
    pdf_files = list(DOCUMENTS_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found!")
        return

    # 4. Process each PDF
    for pdf_path in pdf_files:

        print(f"Processing: {pdf_path.name}")

        # Load the PDF
        pages = PyPDFLoader(str(pdf_path)).load()

        # Add metadata to identify the source
        for page in pages:
            page.metadata["source"] = pdf_path.name
            page.metadata["subject"] = pdf_path.stem

        # Split the PDF into chunks
        chunks = splitter.split_documents(pages)

        # Add these chunks to the combined list
        all_chunks.extend(chunks)

        print(f"Created {len(chunks)} chunks")

    # 5. Store all chunks in Qdrant
    if all_chunks:

        QdrantVectorStore.from_documents(
            documents=all_chunks,
            embedding=embeddings,
            path=str(QDRANT_PATH),
            collection_name=COLLECTION_NAME,
        )

        print(f"Successfully processed {len(pdf_files)} PDFs")
        print(f"Total chunks stored: {len(all_chunks)}")


if __name__ == "__main__":
    ingest_all_pdfs()



