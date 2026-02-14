from pathlib import Path
import re

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DOCS_DIR = Path(__file__).parent / "docs"
DB_DIR = Path(__file__).parent / "chroma_db"


def clean_answer(query, docs):
    query_lower = query.lower()

    for doc in docs:
        sentences = doc.page_content.split(".")
        for sentence in sentences:
            s = sentence.strip()
            if not s:
                continue

            # If question asks "stand for", prioritize that sentence
            if "stand for" in query_lower and "stands for" in s.lower():
                return s + "."

            # Otherwise match by keyword overlap
            if any(word in s.lower() for word in query_lower.split()):
                return s + "."

    # fallback
    return docs[0].page_content.strip()


def main():
    print("Step2 Offline RAG Starting...")

    txt_files = list(DOCS_DIR.glob("*.txt"))
    if not txt_files:
        print("No .txt files found in docs folder.")
        return

    docs = []
    for f in txt_files:
        d = TextLoader(str(f), encoding="utf-8").load()
        for x in d:
            x.metadata["source"] = str(f)
        docs.extend(d)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vs = Chroma(
        collection_name="step2",
        persist_directory=str(DB_DIR),
        embedding_function=embeddings
    )

    vs.add_documents(chunks)
    vs.persist()

    query = input("\nType your question: ")

    results = vs.similarity_search(query, k=3)

    answer = clean_answer(query, results)

    print("\n=== Final Answer ===")
    print(answer)

    print("\n=== Source ===")
    print(results[0].metadata["source"])


if __name__ == "__main__":
    main()