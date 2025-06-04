import asyncio
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import StructuredMessage
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
import os

load_dotenv()
api_key = os.getenv("API_KEY")

async def web_search(query: str) -> str:
    """Find information on the web"""
    return "AutoGen is a programming framework for building multi-agent applications."

model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key=api_key, # type: ignore
)
agent = AssistantAgent(
    name="assistant",
    model_client=model_client,
    tools=[web_search],
    system_message="Use tools to solve tasks.",
)

async def perform_agent_task(task: str):
    result = await agent.run(task=task)
    print(result.messages)

#The Autogen framework is asynchronous.
#Synchronous - one thing happens at a time, e.g. if we wait for a response from openai for 5 seconds, nothing else is being done.
#Asynchronous(async + await) - we can wait only on one task (not a thread!) and let others run in parallel - important for multi-agent systems
#asyncio still runs in the same thread, but can run tasks concurrently, not in parallel. It is managed by python's event loop
#all of it is due to how python itself handles threads due to Global Interpreter Lock (ensures only one thread executes python code at a time)
#and
#python event loop - manages and schedules the execution of asynchronous tasks, coroutines, and I/O events — one at a time, in a specific order.
result = asyncio.run(agent.run(task="Find information on AutoGen"))
print(result)