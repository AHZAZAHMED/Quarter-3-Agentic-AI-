# Gemini Chatbot with Chainlit

This project is an interactive AI chatbot built using Google's Gemini model and the Chainlit framework. The chatbot is designed to provide contextual, multi-turn conversations, remembering previous user queries and responding accordingly. It leverages asynchronous programming for efficient handling of user messages and API calls. The core logic uses `Runner.run`, which executes the agent asynchronously to ensure fast and responsive interactions.

## What You'll Learn

- **Chainlit:**  
  Chainlit is a Python framework for building conversational AI applications with ease. You'll learn how to use Chainlit to manage chat sessions, handle user messages, and maintain conversation history.

- **Asynchronous Programming:**  
  The project uses Python's `async` and `await` features, along with `Runner.run` to execute the agent asynchronously. This allows the chatbot to handle multiple user requests efficiently without blocking the main application.

- **Integrating Gemini API:**  
  You'll see how to connect to the Gemini language model using API keys and how to structure prompts and conversation history for context-aware responses.

## How to Run This Project

1. **Clone the Repository**
   ```sh
   git clone <repository-url>
   cd Gemini-Chatbot-with-Chainlit
   ```

2. **Set Up a Virtual Environment**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   - Create a `.env` file in the project root.
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

5. **Run the Chatbot**
   ```sh
   chainlit run chatbot.py
   ```
   - The app will be available at [http://localhost:8000](http://localhost:8000).

## Author

**AHZAZ AHMED**