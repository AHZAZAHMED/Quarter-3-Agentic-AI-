from agents import Agent , Runner , OpenAIChatCompletionsModel , AsyncOpenAI , RunContextWrapper
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=provider
)

class UserContext(BaseModel):
    user: str
    is_admin: bool

def dynamic_instruction(ctx: RunContextWrapper[UserContext] , agent: Agent[UserContext]) -> str:
    return f"The current user is {ctx.context.user}. Answer the question accordingly."



agent = Agent(
    name = "Assistant",
    instructions = dynamic_instruction,
    model = model
    tools=[]
)

# class CalendarEvent(BaseModel):
#     title: str
#     date:str

# calendar = Agent(
#     name ="Calendar extractor",
#     instructions = "Extract any event dates mentioned in the input.", 
#     model = model,
#     output_type = CalendarEvent
# )

result= Runner.run_sync(
    agent,"What is the capital of France?"
)

# result1 = Runner.run_sync(
#     calendar, "tell me about defence day of pakistan"
# )

print(result.final_output)

# print(result1.final_output)
