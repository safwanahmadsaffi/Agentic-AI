import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Load environment variables from .env if present
load_dotenv()

# Reference: https://ai.google.dev/gemini-api/docs/openai
async def main() -> None:
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please define it in your .env file or environment.")

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

    agent = Agent(
        name="Gemini Assistant",
        instructions="A helpful CLI agent powered by Google Gemini via the OpenAI-compatible API.",
        model=model,
    )

    result = await Runner.run(agent, "Tell me about recursion in programming.", run_config=config)
    print(result.final_output)


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run()