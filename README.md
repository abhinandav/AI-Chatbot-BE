# 🧠 News Chatbot Backend (FastAPI + Chroma + Gemini)

This is a RAG (Retrieval-Augmented Generation) powered chatbot backend that answers user queries using real-time news articles fetched via RSS feeds. It uses FastAPI, ChromaDB, Google Gemini, and Redis for chat history.

---

## 🚀 Features

- 🔍 Retrieves live news from multiple RSS feeds
- 🧠 Embeds content using SentenceTransformers
- 📦 Stores content in Chroma (vector DB)
- 💬 Answers questions using Gemini Pro / Flash
- 💾 Maintains session-based chat history in Redis
- 🧩 Easy to extend with more sources

---

## 🧱 Tech Stack

- **Backend**: FastAPI
- **Vector DB**: ChromaDB
- **Embeddings**: HuggingFace SentenceTransformers
- **LLM**: Google Gemini (via `google.generativeai`)
- **Redis**: Stores chat history by session
- **RSS**: Pulls live news from RSS feeds

---

## 📁 Project Structure

News-Chat-AI/
│
├── app/
│ ├── main.py # FastAPI app setup
│ ├── routers/
│ │ └── chat.py # /chat and history APIs
│ ├── services/
│ │ ├── embedder.py # Embedding function
│ │ ├── retriever.py # ChromaDB logic
│ │ └── gemini.py # Gemini API wrapper
│ ├── utils/
│ │ └── rss_parser.py # RSS feed loader
│ └── storage/
│ └── redis_client.py # Redis integration
│
├── scripts/
│ └── load_articles.py # Loads articles into Chroma
├── .env # API keys and config
└── requirements.txt # Python dependencies



---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/news-chatbot-backend.git
cd news-chatbot-backend
```

### 1. Clone the repository
``` bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### Install dependencies
```bash
pip install -r requirements.txt
```


### Setup env
```bash
GEMINI_API_KEY=your_google_generative_ai_key
```

### 🔁 Load News Articles (from RSS)

```bash
python -m app.scripts.load_articles
```

###  ▶️ Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

## 💬 API Endpoints

### POST /api/chat
Ask a question based on the latest news.

```json
{
  "message": "What is happening in Ukraine?",
  "session_id": "abhinand"
}
```

### GET /session/{session_id}
Get full Q&A history for a session.

### DELETE /session/{session_id}
Clear chat history for a session.



## 💾 In-Memory Caching (Redis)
This app uses Redis to cache user session history and chatbot conversations.

### ✅ Session Caching
Each session is stored in Redis under the session ID

Conversations are stored as JSON strings in a Redis list

### ⏳ Configuring TTL (Auto-Expiry)
To avoid storing unused sessions forever, a TTL (Time-To-Live) is applied:

``` bash
r.expire(session_id, 3600)  # Session auto-expires after 1 hour
```
You can change TTL by modifying the ttl parameter in add_to_history().