# 📄 DocQuery — RAG-Based PDF QnA System

DocQuery is a **Retrieval-Augmented Generation (RAG)** based web application that allows users to upload PDF documents and ask natural-language questions to get **accurate, document-grounded answers**.

The system is designed for **students and learners** who want to interactively explore textbooks, notes, research papers, and other long PDFs using Generative AI.

---

## Features

* Upload any PDF document (lecture notes, textbooks, research papers)
* Ask questions and get answers **strictly based on the uploaded PDF**
* Uses **RAG (Retrieval-Augmented Generation)** for high accuracy
* Handles **large PDFs (1000+ pages)** efficiently
* Chat-style interface similar to ChatGPT
* Semantic chunking + vector search
* Vector stores saved locally and reused across requests
* Session-based isolation (each user gets their own document context)

---

## How DocQuery Works (High-Level)

```
PDF Upload
   ↓
PDF Text Extraction
   ↓
Semantic Chunking
   ↓
Embeddings Generation
   ↓
Vector Store (FAISS)
   ↓
User Query
   ↓
Relevant Chunk Retrieval
   ↓
LLM Generates Answer
```

This approach ensures:

* Minimal hallucination
* Accurate, context-aware responses
* Scalable handling of large documents

---

## Tech Stack

### Backend

* **Flask** — Web framework
* **LangChain** — RAG pipeline orchestration
* **FAISS** — Vector database
* **Google Gemini / Open-Source Embeddings** — Text embeddings
* **Python** — Core language

### Frontend

* **HTML5**
* **CSS (Bootstrap)**
* **JavaScript (Fetch API)**

---

## Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/DocQuery.git
cd DocQuery
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
SECRET_KEY=your_flask_secret_key
```

---

### 5️⃣ Run the Application

```bash
python run.py
```

Open browser at:

```
http://127.0.0.1:5000
```

---

## Chat Workflow

1. User uploads a PDF
2. Backend extracts text and builds vector store
3. Vector store is saved locally
4. User asks questions via chat UI
5. Each question:

   * Retrieves relevant chunks
   * Passes them to the LLM
   * Returns an answer as JSON
6. Frontend updates chat UI dynamically

---

## RAG Design Choices

### Chunking Strategy

* Chunk size: ~800 tokens
* Overlap: ~120 tokens

### Vector Storage

* FAISS stored locally on disk
* Vector store path saved in session
* Reloaded on each query (no re-embedding)

---

## Session Handling

* PDF path and vector store path stored in Flask session
* Each user session is isolated
* On session reset, vector store and uploaded PDF are deleted

---

## Known Limitations (Current)

* Single PDF per session
* Local vector storage (not cloud-based yet)
* No streaming responses (planned)

---

## Future Enhancements

* External vector databases (Pinecone / Qdrant)
* Source citations with page numbers
* Multi-PDF support
* Streaming responses
* Cloud deployment
* Authentication & user profiles

---

## Who Is This Project For?

* Students preparing for exams
* Learners reading large PDFs
* Developers learning RAG systems
* Recruiters evaluating real-world GenAI projects

---

## Key Learning Outcomes

* RAG system design
* Vector database lifecycle management
* Chunking strategies for long documents
* Frontend–backend chat architecture
* Production-ready Flask patterns


