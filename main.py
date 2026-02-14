from __future__ import annotations

from offline_rag.config import Settings
from offline_rag.loaders import load_txt_documents
from offline_rag.splitter import split_documents
from offline_rag.vectorstore import build_embeddings, build_vectorstore, index_documents
from offline_rag.retriever import retrieve
from offline_rag.answerer import extract_sentence_answer


def run() -> None:
    s = Settings()
    print("Offline RAG (Step-2) starting...")

    s.docs_dir.mkdir(parents=True, exist_ok=True)

    docs = load_txt_documents(s.docs_dir)
    if not docs:
        print(f"No .txt files found in: {s.docs_dir}")
        print("Create docs/test.txt and rerun.")
        return

    chunks = split_documents(docs, chunk_size=s.chunk_size, chunk_overlap=s.chunk_overlap)

    embeddings = build_embeddings(s.embedding_model)
    vs = build_vectorstore(embeddings=embeddings, persist_dir=s.db_dir, collection_name=s.collection_name)

    # v1: always index on run (simple). We'll enhance to 'index once' in next version.
    index_documents(vs, chunks)

    query = input("\nType your question: ").strip()
    results = retrieve(vs, query, k=s.top_k)

    answer = extract_sentence_answer(query, results)

    print("\n=== Final Answer ===")
    print(answer)

    if results:
        print("\n=== Source ===")
        print(results[0].metadata.get("source", "unknown"))


if __name__ == "__main__":
    run()
