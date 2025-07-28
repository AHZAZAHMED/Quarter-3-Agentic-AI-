from agents import Agent , AsyncOpenAI , OpenAIChatCompletionsModel , Runner
from dotenv import load_dotenv
import os
import chainlit as cl

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("Gemini_API_KEY is not set in the environment variables.")

provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url ="https://generativelanguage.googleapis.com/v1beta/openai"
)


# configure the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client = provider,
)

# creating a greeting agent
agent =Agent(
    name=" Agent",
    instructions= "You are an assistant agent that replies to the user prompt. "
        "Use the entire conversation history to answer contextually. "
        "If the user asks about their previous question, refer to the chat history."
    ,
    model=model,
)

@cl.on_chat_start
async def start_chat():
    await cl.Message(content="Assalamualikum! How can I assist you today?").send()
    cl.user_session.set("history", [])

@cl.on_message
async def reply(message : cl.Message):
    history = cl.user_session.get("history")
    history.append({"role":"user", "content": message.content})

    response = await Runner.run(agent, history)

    history.append({"role":"assistant", "content": response.final_output})
    cl.user_session.set("history", history)
    print(history)
    await cl.Message(content=response.final_output).send()
    
