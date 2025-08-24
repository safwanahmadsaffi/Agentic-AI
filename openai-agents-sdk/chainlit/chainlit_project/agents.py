from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class RunConfig:
    model: Any = None
    model_provider: Any = None
    tracing_disabled: bool = False


class AsyncOpenAI:
    def __init__(self, api_key: str, base_url: Optional[str] = None):
        self.api_key = api_key
        self.base_url = base_url

    async def chat(self, *args, **kwargs):
        # Placeholder async interface.
        return {"choices": [{"message": {"content": "(simulated async response)"}}]}


class OpenAIChatCompletionsModel:
    def __init__(self, model: str, openai_client: AsyncOpenAI):
        self.model = model
        self.client = openai_client

    def generate(self, prompt: str):
        # Simulate a model response based on prompt.
        return f"Simulated response to: {prompt}"


class Agent:
    def __init__(self, name: str, instructions: str = ""):
        self.name = name
        self.instructions = instructions

    def act(self, message: str, run_config: Optional[RunConfig] = None):
        # Very small behavior: echo the message with a prefix.
        model = run_config.model if run_config and run_config.model else None
        if model:
            output = model.generate(message)
        else:
            output = f"{self.name} (no model): {message}"
        return SimpleResult(final_output=output)


class Runner:
    @staticmethod
    def run_sync(agent: Agent, message: str, run_config: Optional[RunConfig] = None):
        # Provide a synchronous runner that returns the agent's output
        return agent.act(message, run_config=run_config)


@dataclass
class SimpleResult:
    final_output: str
