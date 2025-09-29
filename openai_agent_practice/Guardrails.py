from agents import Agent , Runner , OpenAIChatCompletionsModel , AsyncOpenAI , RunContextWrapper , enable_verbose_stdout_logging , function_tool,Handoff,GuardrailFunctionOutput,InputGuardrailTripwireTriggered,input_guardrail,set_tracing_disabled ,output_guardrail,OutputGuardrailTripwireTriggered
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()
set_tracing_disabled(True)
enable_verbose_stdout_logging()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=provider
)

class MathContext(BaseModel):
    is_math_problem: bool
    reasoning: str

class mathoutput(BaseModel):
    response: str

check_Agent = Agent(
    name="CheckAgent",
    instructions="Determine if the input is a math problem.",
    model=model,
    output_type=MathContext
)



@input_guardrail()
async def guardrial_function(ctx: RunContextWrapper , agent:Agent , input:str)->GuardrailFunctionOutput:

    result = await Runner.run(
        check_Agent, input
    )
    return GuardrailFunctionOutput(
        output_info= result.final_output,
        tripwire_triggered = result.final_output.is_math_problem 
    )  


@output_guardrail()
async def output_guardrail(ctx: RunContextWrapper , agent:Agent , output:any)->GuardrailFunctionOutput:

    result = await Runner.run(
        check_Agent , output.response
    )

    return GuardrailFunctionOutput(
        result.final_output,
        result.final_output.is_math_problem
    )

python_agent = Agent(
    name="PythonAgent",
    instructions="You are a helpful assistant that can write and execute python code.",
    model=model,
    # input_guardrails=[guardrial_function],
    output_guardrails=[output_guardrail],
    output_type=mathoutput
)

try:
    Result=Runner.run_sync(
        python_agent, "what is 2+2?"
    )
    print("Result:",Result.final_output)
# except InputGuardrailTripwireTriggered:
#     print("You can only question regarding python.")
except OutputGuardrailTripwireTriggered:
    print("The output is not relevant to python programming.")
