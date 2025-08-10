from agents import Agent , Runner , OpenAIChatCompletionsModel , AsyncOpenAI , function_tool
from dotenv import load_dotenv
import os 
import chainlit as cl 
from  openai.types.responses import ResponseTextDeltaEvent
from dataclasses import dataclass

@dataclass

load_dotenv()               

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("Gemini api key is not set in the environment variable")

provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
)

@function_tool
def getweather(location : str) -> str:
    """ 
      Get the location form user input and return the location with the string defined
    """
    return f"Weather today in {location} is very hot"


model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = provider
)

Agent_with_Tools = Agent(
    name = "Agent_with_Tools",
    instructions = "You are a helpful assistant which response with the help  of tools.",
    model = model,
    tools=[getweather]
)

@cl.on_chat_start
async def startChat():
    await cl.Message(content="I am a helpful assistant how may i help you.").send()
    cl.user_session.set("history", [])

@cl.on_message
async def reply(message: cl.Message):
    history = cl.user_session.get("history")
    msg = cl.Message("")
    await msg.send()

    history.append({"role" :"user" , "content" : message.content })

    response = Runner.run_streamed(Agent_with_Tools, history)

    async for event in response.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data , ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)
            
    await msg.update()
    
    history.append({"role" : "assistant" , "content" : response.final_output})
    cl.user_session.set("history" , history)
