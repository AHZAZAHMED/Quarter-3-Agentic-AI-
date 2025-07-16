# Coordinated Multi-Agent System 🤖

This project demonstrates a simple **multi-agent system** using the OpenAI Agent SDK and third-party LLMs like Gemini. It is designed as a learning exercise to explore how agents are created, how they interact, and how coordination and handoff between them works.

## 🧠 Project Overview

The system contains **three agents**:

1. **Coordinator Agent**  
   - Acts as the central decision-maker.  
   - Interprets user input and decides which sub-agent should handle the request.  
   - Uses the concept of `handoff` to delegate tasks to either the Joke Agent or Greeting Agent.

2. **Greeting Agent**  
   - Responds to greetings like "hi", "hello", "salam", etc.  
   - Sends back a friendly Islamic greeting like `Assalamu Alaikum`.

3. **Joke Agent**  
   - Activated when the user's prompt is asking for a joke.  
   - Uses a custom **tool** that connects to an external **Joke API** to fetch and return a joke dynamically.

---

## 🧩 Key Concepts

### ✅ Agents
- Built using the `Agent` class from OpenAI Agent SDK.
- Each agent is an instance with a defined purpose and behavior.

### ✅ Coordination & Handoff
- The `Coordinator Agent` takes input and delegates tasks using the `handoff()` method.
- Based on the user's intent, the task is routed to either the Joke or Greeting agent.

### ✅ Tools
- The Joke Agent uses a **Tool** that integrates with a third-party Joke API.
- Demonstrates how agents can call tools to fetch real-time data or perform tasks.

---

## 🛠 Technologies Used

- **OpenAI Agent SDK** – for building and running agents
- **Third-party LLM (Gemini)** – for understanding natural language prompts
- **API Integration** – for dynamic joke retrieval

---

## 🧪 Classes and Components

| Class | Purpose |
|-------|---------|
| `Agent` | Used to create agents with specific behavior |
| `AsyncOpenAI` | Connects the agent with the Gemini LLM backend |
| `OpenAIChatCompletionModel` | Converts Gemini model into OpenAI-style model for compatibility |
| `Runner` | Executes the agent instance and manages the event loop |

---

## 🚀 How to Run (using `uv`)

1. **Install [uv](https://github.com/astral-sh/uv)** if not already installed:
   ```bash
   pip install uv
   ```

2. **Create a virtual environment and install dependencies**:
   ```bash
   uv venv .venv
   uv pip install -r requirements.txt
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Run the coordinator agent**:
    ```
    uv run main.py
    ```
5. **Interact with the system**:
   - Input: `"hi"` → Greeting Agent replies with `Assalamu Alaikum`.
   - Input: `"tell me a joke"` → Joke Agent calls the Joke API and replies.

---

## 👨‍💻 Author

**Ahzaz Ahmed**  
Project for Quarter-3 Agentic AI Learning

---