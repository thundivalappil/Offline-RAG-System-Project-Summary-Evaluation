yesbee4ai-offline-rag-chromadb
Offline Retrieval-Augmented Generation (RAG)
Using ChromaDB + Sentence-Transformers
Runs fully offline — No OpenAI key required.
Designed for privacy-first document retrieval and secure local AI workflows.
 
1. Overview
   
•	Loads .txt files from the ./docs/ directory
•	Splits text into manageable semantic chunks
•	Generates embeddings using sentence-transformers/all-MiniLM-L6-v2
•	Stores vectors in a persistent ChromaDB directory (./chroma_db/)
•	Retrieves top relevant matches for a question
•	Extracts the best answer sentence
•	Outputs Answer with Source citation

All processing happens locally.
2. Why Offline RAG?

•	No external API dependency
•	No data leakage risk
•	No usage-based costs
•	Suitable for MSMEs and internal knowledge systems
•	Fully CPU-compatible
3. Quickstart (Windows / PowerShell)
Step 1: Create and activate a virtual environment
Step 3: Add a document
Place a .txt file inside the docs/ directory.
Example: docs/test.txt
Step 4: Run the application
python main.py
Example query:
What does RAG stand for?
4. Repository Structure

yesbee4ai-offline-rag-chromadb/


│
├─ main.py
├─ src/offline_rag/
│   ├─ config.py
│   ├─ loaders.py
│   ├─ splitter.py
│   ├─ vectorstore.py
│   ├─ retriever.py
│   └─ answerer.py
│
├─ docs/
│   └─ test.txt
│
├─ requirements.txt
└─ .gitignore

5. Notes
   
•	On first run, the embedding model (~80MB) will download and cache locally.
•	chroma_db/ is generated automatically and excluded from Git via .gitignore.
7. Roadmap
•	Index-once logic (skip re-indexing if vectors already exist)
•	PDF support (pypdf) with page-level citations
•	Top-3 citation support with chunk identifiers
•	Evaluation script (eval/) for retrieval accuracy testing
•	Optional local LLM integration (future upgrade)
8. License
MIT


