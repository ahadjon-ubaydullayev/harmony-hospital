# RAG Chatbot

This Retrieval-Augmented Generation (RAG) chatbot uses Streamlit (frontend), FastAPI (backend), and ChromeDB (vector database) to deliver accurate, context-aware answers.

## Features
- **Retriever:** Fetches relevant documents.
- **Generator:** Produces context-based responses.
- **Frontend:** Built with Streamlit.
- **Backend:** REST API with FastAPI.

---

## Prerequisites
- Python 3.8+
- Docker (optional)
- ChromeDB setup
- `.env` file with credentials (API keys, DB URL).

---

## Setup and Run

### 1. Clone Repository
```bash
git clone https://github.com/your-repo/rag-chatbot.git
cd rag-chatbot
```

### 2. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment
Create `.env` in the root with:
```env
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000
STREAMLIT_HOST=0.0.0.0
STREAMLIT_PORT=8501
DATABASE_URL=<your_chromedb_url>
OPENAI_API_KEY=<your_openai_api_key>
```

### 4. Run Backend (FastAPI)
```bash
uvicorn backend.main:app --host $FASTAPI_HOST --port $FASTAPI_PORT
```
Access at: `http://localhost:8000`

### 5. Run Frontend (Streamlit)
```bash
streamlit run frontend/app.py --server.port $STREAMLIT_PORT
```
Access at: `http://localhost:8501`

---

## Docker (Optional)
1. Build images:
    ```bash
    docker-compose build
    ```
2. Start services:
    ```bash
    docker-compose up
    ```

---
