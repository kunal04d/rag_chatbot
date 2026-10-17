from pathlib import Path

from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

BASE_DIR = Path(__file__).resolve().parent.parent
QDRANT_PATH = BASE_DIR / "qdrant_data"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    path=str(QDRANT_PATH),
    collection_name="notes",
)

retriever = vector_store.as_retriever(search_kwargs={"k": 4})

PROMPT = """Answer the question using ONLY the context below.
If the answer is not in the context, say "I couldn't find this in the notes."

Context:
{context}

Question: {question}
Answer:"""


def ask(question: str, llm):
    docs = retriever.invoke(question)

    context = "\n\n".join(d.page_content for d in docs)

    answer = llm.invoke(
        PROMPT.format(context=context, question=question)
    )

    sources = [
        (d.metadata["source"], d.metadata["page"] + 1)
        for d in docs
    ]

    return answer.content, sources