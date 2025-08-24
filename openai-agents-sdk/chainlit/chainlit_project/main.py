import os
import chainlit as cl

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Try to read API key from the environment; fallback to a placeholder string so
# the script can run in environments without credentials.
gemini_api_key = os.getenv("GEMINI_API_KEY", "GEMINI_API_KEY")

# Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)


@cl.on_chat_start
def start():
    # Store the agent in Chainlit's user_session (per-user storage)
    cl.user_session.set("agent", Agent(name="Assistant", instructions="You are a helpful assistant"))


@cl.on_message
def handle_message(message: str):
    agent: Agent = cl.user_session.get("agent")
    if agent is None:
        agent = Agent(name="Assistant", instructions="You are a helpful assistant")
        cl.user_session.set("agent", agent)

    result = Runner.run_sync(agent, message, run_config=config)
    cl.Message(content=result.final_output).send()