yesbee4ai-offline-rag-chromadb
Offline RAG (Retrieval-Augmented Generation) using ChromaDB and Sentence-Transformers embeddings.
Runs fully offline — no OpenAI key required.
Designed for privacy-first document retrieval and secure local AI workflows.
Overview
This repository implements a lightweight, modular Offline RAG system that:
• Loads .txt files from ./docs/
• Splits text into manageable chunks
• Generates embeddings using sentence-transformers/all-MiniLM-L6-v2
• Stores vectors in a persistent ChromaDB directory (./chroma_db/)
• Retrieves top relevant matches for a question
• Extracts the best answer sentence
• Outputs Answer + Source citation
All processing happens locally.
Why Offline RAG?
• No external API dependency
• No data leakage
• No usage costs
• Suitable for MSMEs and internal knowledge systems
• Fully CPU-compatible
Quickstart (Windows / PowerShell)
1) Create and activate a virtual environment
cd D:\Projects\RAG_Project
python -m venv .venv
.\.venv\Scripts\activate
2) Install dependencies
pip install -r requirements.txt
3) Add a document
Place a .txt file inside the docs/ directory.
Example provided: docs/test.txt
4) Run the application
python main.py
Example query:
What does RAG stand for?
Repository Structure
yesbee4ai-offline-rag-chromadb/
├─ main.py
├─ src/offline_rag/
│  ├─ config.py
│  ├─ loaders.py
│  ├─ splitter.py
│  ├─ vectorstore.py
│  ├─ retriever.py
│  └─ answerer.py
├─ docs/
│  └─ test.txt
├─ requirements.txt
└─ .gitignore
Notes
• On first run, the embedding model (~80MB) will be downloaded and cached locally.
• chroma_db/ is generated automatically and excluded from Git via .gitignore.
Roadmap
• Index-once logic (skip re-indexing if vectors already exist)
• PDF support (pypdf) with page-level citations
• Top-3 citation support with chunk identifiers
• Evaluation script (eval/) for retrieval accuracy testing
• Optional local LLM integration (future upgrade)
License
MIT

