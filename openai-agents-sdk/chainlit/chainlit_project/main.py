import os
import chainlit as cl

from dotenv import load_dotenv, find_dotenv

from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")

# provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

# Convert RunConfig to dictionary format for mcp_config
mcp_config = {
    "model": model,
    "model_provider": provider,
    "tracing_disabled": True
}

agent = Agent(
    mcp_config=mcp_config,  # Fixed: use dictionary format
    instructions="You are a helpful assistant that can answer questions and provide support.",
    name="Panaversity Support Agent"
)

result = agent.run_sync(
    input="Hello, how can you help me today?"
)
print(result)

# @cl.on_message
# async def handle_message(message: cl.Message):
#     response = await agent.run(message.content)
#     await cl.Message(content=response).send()
