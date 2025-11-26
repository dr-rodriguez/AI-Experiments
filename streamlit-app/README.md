# Streamlit Chatbot App

This is a simple chatbot application built with Streamlit and LangChain, using a local Ollama model (Llama 3.2).

## Features
- **Local AI**: Uses Ollama to run Llama 3.2 locally.
- **Chat Interface**: Simple and clean chat interface provided by Streamlit.
- **Streaming Responses**: Real-time streaming of AI responses.
- **History**: Maintains conversation history within the session.

## Prerequisites
- [Ollama](https://ollama.com/) installed and running.
- `llama3.2:3b` model pulled (`ollama pull llama3.2:3b`).
- [uv](https://github.com/astral-sh/uv) installed (recommended for dependency management).

## How to Run

1.  Ensure Ollama is running:
    ```bash
    ollama serve
    ```

2.  Run the Streamlit app:
    ```bash
    uv run streamlit run main.py
    ```

The app will open in your default browser at `http://localhost:8501`.
