import asyncio
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import StructuredMessage
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import ExternalTermination, TextMentionTermination
import os

load_dotenv()
api_key = os.getenv("API_KEY")

async def web_search(query: str) -> str:
    """Find information on the web"""
    return "AutoGen is a programming framework for building multi-agent applications."

model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key=api_key # type: ignore
)
agent1 = AssistantAgent(
    name="agent1",
    model_client=model_client,
    tools=[web_search],
    system_message="Use tools to solve tasks. Collaborate with agent2. Provide constructive feedback. Say TERMINATE when done.",
)

agent2 = AssistantAgent(
    name="agent2",
    model_client=model_client,
    tools=[web_search],
    system_message="Use tools to solve tasks. Collaborate with agent1. Provide constructive feedback. Say TERMINATE when done.",
)
text_termination = TextMentionTermination("TERMINATE")

team = RoundRobinGroupChat([agent1, agent2], termination_condition=text_termination)

result = asyncio.run(Console(team.run_stream(task="Write a short poem about the fall season.")))
