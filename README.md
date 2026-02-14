# yesbee4ai-offline-rag-chromadb

Offline **RAG (Retrieval-Augmented Generation)** using **ChromaDB** + **Sentence-Transformers** embeddings.  
No OpenAI key required — works fully offline.

## What this repo does
- Loads `.txt` files from `./docs/`
- Splits text into chunks
- Creates embeddings using `sentence-transformers/all-MiniLM-L6-v2`
- Stores vectors in a persistent **ChromaDB** folder (`./chroma_db/`)
- Retrieves top matches for a question and extracts the best answer sentence
- Prints **Answer + Source citation**

## Quickstart (Windows / PowerShell)

### 1) Create and activate a virtual environment (recommended)
```powershell
cd D:\Projects\RAG_Project
python -m venv .venv
.\.venv\Scripts\activate
```

### 2) Install dependencies
```powershell
pip install -r requirements.txt
```

### 3) Add a document
Put a `.txt` file in `docs/` (example provided: `docs/test.txt`).

### 4) Run
```powershell
python main.py
```

Ask:
```
What does RAG stand for?
```

## Repo structure
```
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
```

## Notes
- First run may download the embedding model once (~80MB) and cache it locally.
- `chroma_db/` is excluded from git via `.gitignore` (it’s generated output).

## Roadmap (next upgrades)
- Index-once (skip re-indexing when `chroma_db/` already has data)
- PDF support (`pypdf`) + page citations
- Top-3 citations & chunk ids
- Evaluation script (`eval/`) for accuracy checks

## License
MIT (add if you want)
