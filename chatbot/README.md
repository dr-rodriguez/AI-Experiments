# Local LLM Chatbot

A simple CLI chatbot built with Python, [LangChain](https://python.langchain.com/), and [Ollama](https://ollama.com/).

## Features

-   **Local Inference**: Runs entirely on your machine using Ollama.
-   **Streaming Responses**: See the AI's output in real-time.
-   **Conversation History**: Maintains context throughout the session.

## Prerequisites

1.  **Install Ollama**: Download and install from [ollama.com](https://ollama.com/).
2.  **Pull the Model**: This project uses `llama3.2:3b`. Run the following command in your terminal:
    ```bash
    ollama pull llama3.2:3b
    ```
3.  **Start Ollama**: Ensure the Ollama service is running (usually `ollama serve` or via the desktop app).

## Installation

This project uses `uv` for dependency management.

1.  **Install dependencies**:
    ```bash
    uv sync
    ```

## Usage

Run the chatbot:

```bash
uv run main.py
```

Type your message and press Enter to chat. Type `exit` or `quit` to end the session.
