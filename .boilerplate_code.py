from agents import Agent, Runner
from agentsdk_gemini_adapter import config

# Create an agent using Agent class 
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
)

# Pass the Gemini configuration in run_config to any Runner method
result = Runner.run_sync(agent, "What is 2 + 2?", run_config=config)

print("Result:", result.final_output)