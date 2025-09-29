from agents import Agent , Runner , OpenAIChatCompletionsModel , AsyncOpenAI , RunContextWrapper , enable_verbose_stdout_logging , function_tool,Handoff
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from agents.extensions import handoff_filters


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


@function_tool
def get_weather(location: str) -> str:
    # Dummy implementation for example purposes
    return f"The weather in {location} is sunny with a high of 25°C."

weather_agent = Agent(
    name = "weather_agent", # Use this as the instructions argument for your Agent
    instructions = (
    "You are a helpful assistant. "
    "just give the location to the get_weather tool and return its stored string response."
    ),
    model = model,
    handoff_description = "you use the tool to get the weather of a location",
    tools = [get_weather]
)

@function_tool
def get_student() -> str:
  data={
        "101": "Ahzaz"
    }
  
  for key in data:
    data[key] == input
    answer = data[key]
  return answer

student_finder_agent = Agent(
    name = "student_finder",
    instructions = "you are a helpful assistant that deal with student related quries and always use the get_student tool",
    model = model,
    handoff_description = "you are an agent that help in student related quries",
    tools=[get_student]
)

async def handoff_invoke(ctx : RunContextWrapper , input : str):
  print("Context:", ctx)
  print("context context:", ctx.context)
  print("usage:",  ctx.usage)
  print("Handoff invoked with input:", input)
  return student_finder_agent


student_handsoff = Handoff(
              tool_name = "student_finder_agent",
              tool_description = "Handle all student related quiries",
               agent_name = "student_finder_agent",
               input_json_schema={
                   "type" : "object",
                   "properties" : {
                       "student_id" : {"type" : "string"}
                    },
                    "required" : ["student_id"]
               },
               on_invoke_handoff= handoff_invoke ,
                # input_filter = handoff_filters.remove_all_tools

                      )


triage_agent = Agent(
    name = "triage_agent",
    instructions = "you are a helpful assistant.just handle task to the student_finder_agent if the question is related to student ",
    model = model,
    handoffs = [student_handsoff]
    )


result = Runner.run_sync(
    triage_agent ,"what is the name 0f student with key 101"
)

print(result.final_output)