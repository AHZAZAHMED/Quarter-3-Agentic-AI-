# Gemini-Powered Chatbot using Chainlit UI

This project is an AI-powered chatbot built with [OpenAI Agent SDK](https://github.com/openai/openai-agents), integrated into a [Chainlit](https://docs.chainlit.io/) interface and powered by Gemini-2.0-Flash.

---

## ✨ Features

- Gemini model integration via Google Generative Language API.
- Clean UI with Chainlit.
- Chat history tracking in session.
- Asynchronous agent execution using `Runner.run()`.

---

## 🛠️ Setup Instructions

### Step 1: Initialize Project

```bash
uv init chatbot-gemini-ui
```

### Step 2: Install Required Packages

```bash
uv add chainlit
uv add openai-agents
uv add python-dotenv
```

### Step 3: Test Chainlit Installation

```bash
uv run chainlit hello
```

### Step 4: Activate Virtual Environment (Windows)

```bash
.venv\Scripts\activate
```

### Step 5: Add `.env` File

Create a `.env` file in the root folder and add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 🚀 Running the Chatbot

Create a file `chatbot.py` and write the chatbot logic. Then run it using:

```bash
uv run chainlit run chatbot.py
```

---


## 🧩 Technologies Used

- Chainlit
- OpenAI Agents SDK
- Gemini 2.0 Flash
- Python `dotenv`
- `uv` (Universal Package Manager)

