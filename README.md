# 🧠 Chatbot Memory

A terminal-based AI chatbot with persistent memory using LangChain, Ollama, and PostgreSQL. The chatbot remembers your conversation across sessions — close the terminal and come back later, it still knows who you are.

## Features

- Persistent chat history stored in PostgreSQL (Supabase)
- Context-aware responses — the LLM receives full conversation history on every message
- Local LLM via Ollama — no API costs
- Clean separation of memory logic and chat logic

## Tech Stack

| Tool | Purpose |
|---|---|
| LangChain | Chain management + message history |
| Ollama (`gemma3:4b`) | Local LLM inference |
| PostgreSQL (Supabase) | Persistent chat history storage |
| `langchain-postgres` | `PostgresChatMessageHistory` (non-deprecated) |
| `psycopg` | PostgreSQL driver |
| `python-dotenv` | Environment variable management |

## Project Structure

```
chatbot_memory/
├── .env           # Environment variables
├── .gitignore
├── requirements.txt
├── main.py        # Entry point — chat loop
└── memory.py      # DB connection + chat history setup
```

## Setup

### 1. Clone and create virtual environment

```bash
git clone <your-repo-url>
cd chatbot_memory
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
POSTGRES_DB_URL=postgresql://your-user:your-password@your-host:5432/postgres?sslmode=require
```

> Get your connection string from Supabase → Settings → Database → Connection string → URI

### 4. Pull the Ollama model

```bash
ollama pull gemma3:4b
```

### 5. Run the chatbot

```bash
python main.py
```

## How It Works

```
User sends message
       ↓
Fetch chat history from PostgreSQL (for session)
       ↓
Build messages: system prompt + history + new message
       ↓
LLM responds with full context
       ↓
Save HumanMessage + AIMessage back to PostgreSQL
```

## Requirements

```
langchain-ollama
langchain-postgres
langchain-core
python-dotenv
psycopg[binary]
```

## Notes

- Session ID is derived from a fixed name using `uuid5` — so the same session persists across runs
- System prompt is not saved to DB — it is prepended to every request at runtime
- `PostgresChatMessageHistory` is from `langchain-postgres` package (not the deprecated `langchain_community` version)