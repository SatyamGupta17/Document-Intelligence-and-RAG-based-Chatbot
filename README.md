# 📄 Document Intelligence & RAG-based Chatbot

An end-to-end **Document Intelligence** platform that enables users to upload documents and interact with them using natural language. The application leverages **Retrieval-Augmented Generation (RAG)**, transformer embeddings, semantic vector search, and Large Language Models (LLMs) to provide accurate, context-aware responses from unstructured documents.

---

## 🚀 Features

- 📄 Upload and process PDF documents
- ✂️ Intelligent document chunking
- 🧠 Semantic embeddings using Sentence Transformers
- 🔍 Vector similarity search with FAISS
- 🤖 Context-aware question answering using Groq Llama 3
- 📚 Metadata-aware document indexing
- ⚡ FastAPI backend with REST APIs
- 🎨 Streamlit frontend for interactive document chat
- 🔒 Grounded responses (answers only from uploaded documents)

---

## 🏗️ System Architecture

```text
                +--------------------+
                |   Upload PDF       |
                +---------+----------+
                          |
                          ▼
                +--------------------+
                |  Text Extraction   |
                |   (PyMuPDF)        |
                +---------+----------+
                          |
                          ▼
                +--------------------+
                | Intelligent        |
                | Text Chunking      |
                +---------+----------+
                          |
                          ▼
                +--------------------+
                | Sentence           |
                | Transformer        |
                | Embeddings         |
                +---------+----------+
                          |
                          ▼
                +--------------------+
                | FAISS Vector Index |
                +---------+----------+
                          |
                          ▼
                +--------------------+
                | Similarity Search  |
                +---------+----------+
                          |
                          ▼
                +--------------------+
                | Groq LLM           |
                | (Llama 3)          |
                +---------+----------+
                          |
                          ▼
                +--------------------+
                | Natural Language   |
                | Response           |
                +--------------------+
```

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| Language | Python |
| Document Parsing | PyMuPDF |
| Chunking | LangChain RecursiveCharacterTextSplitter |
| Embeddings | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Database | FAISS |
| LLM | Groq (Llama 3) |
| API Testing | Swagger UI |
| Environment | Python Virtual Environment |

---

# 📁 Project Structure

```
Document-RAG
│
├── app
│   ├── api
│   │   ├── chat.py
│   │   └── upload.py
│   │
│   ├── services
│   │   ├── extractor.py
│   │   ├── chunking.py
│   │   ├── embeddings.py
│   │   ├── ingestion.py
│   │   ├── retrieval.py
│   │   └── rag.py
│   │
│   ├── database
│   │   └── vector_store.py
│   │
│   ├── main.py
│   └── __init__.py
│
├── frontend
│   └── app.py
│
├── uploads
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/document-rag.git

cd document-rag
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a **.env** file in the project root.

```env
GROQ_API_KEY=your_api_key
```

---

# ▶️ Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger API

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Frontend

```bash
streamlit run frontend/app.py
```

---

# 📚 API Endpoints

## Upload Document

```
POST /upload
```

Uploads a PDF and indexes it for semantic retrieval.

---

## Chat with Document

```
POST /chat
```

Example

```
What are React Hooks?
```

Returns

```json
{
    "answer":"React provides useState, useEffect, useContext..."
}
```

---

# 🔍 Retrieval-Augmented Generation (RAG) Pipeline

```text
User Upload
      │
      ▼
Document Extraction
      │
      ▼
Chunk Generation
      │
      ▼
Embedding Creation
      │
      ▼
Vector Storage (FAISS)
      │
      ▼
Semantic Retrieval
      │
      ▼
Prompt Construction
      │
      ▼
Groq LLM
      │
      ▼
Context-aware Response
```

---

# 📊 Key Features

✅ End-to-End Document Intelligence

✅ Semantic Search

✅ Retrieval-Augmented Generation (RAG)

✅ Context-aware Prompt Engineering

✅ Vector Similarity Search

✅ Metadata-aware Retrieval

✅ PDF Parsing

✅ FastAPI REST APIs

✅ Streamlit UI

✅ Modular Backend Architecture

---

# 🚀 Future Enhancements

- Azure AI Search Integration
- Azure Document Intelligence
- Qdrant Cloud Vector Database
- MongoDB Atlas Metadata Storage
- Cloudinary File Storage
- OCR Support
- Multi-document Search
- Chat History
- Authentication
- Docker Deployment
- Kubernetes Deployment
- CI/CD Pipeline
- Azure OpenAI Integration

---

# 📈 Resume Highlights

- Developed an end-to-end Document Intelligence platform enabling semantic document search and conversational AI over unstructured PDFs.
- Designed a scalable Retrieval-Augmented Generation (RAG) pipeline integrating document extraction, vector embeddings, semantic retrieval, and LLM-powered reasoning.
- Implemented metadata-aware indexing and prompt engineering to deliver grounded, context-aware responses with high retrieval accuracy.

---

# 📸 Demo

| Upload Document | Ask Questions |
|-----------------|---------------|
| 📄 Upload PDFs | 💬 Natural Language Chat |

*(Add screenshots here after deployment.)*

---

# 🤝 Contributing

Contributions, feature requests, and improvements are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Satyam Gupta

LinkedIn: https://www.linkedin.com/in/satyam-g-7a5a85232/

GitHub: https://github.com/your-github
