from agents import Agent, Runner ,AsyncOpenAI , OpenAIChatCompletionsModel , function_tool
from dotenv import load_dotenv
import os
import requests

load_dotenv()

@function_tool
def get_joke():
    """
    Fetches Joke from the api.
    """
    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return {"error": "Failed to fetch Asharib information"}

# Load the environment variable for the Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize the OpenAIChatCompletionModel with the Gemini API key
provider = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# configure the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client = provider,
)

# creating a greeting agent
Greeting_agent =Agent(
    name="Greeting Agent",
    instructions="You are a greeting agent. ONLY reply with Islamic greetings like 'Salam' when the user says hello or similar words with (salam how may i help you). Do NOT answer any other kind of question.",
    model=model,
)

Joke_agent = Agent(
    name="Get joke Agent",
    instructions="you are an agent that give joke on user request."
    "You will always use the get_joke function to fetch the information.",
    model=model,
    tools=[get_joke]
)

corrdinator_agent = Agent(
    name="Coordinator Agent",
    instructions="You are  a coordinator  agent. you will decide which agent to use based on the user's query.",
    handoffs = [Greeting_agent, Joke_agent],
    model=model,
)

# Getting user input
user_input = input("Enter your question: ")

# Running the agent with the user inpu
agent_result = Runner.run_sync(corrdinator_agent, user_input)

print(agent_result.final_output)