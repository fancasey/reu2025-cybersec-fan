import logging

from autogen_core import EVENT_LOGGER_NAME

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(EVENT_LOGGER_NAME)
# logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

logger.info("Starting up...")

from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv

load_dotenv()

from autogen_core.models import UserMessage
import asyncio

async def fun():
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key=os.getenv("API_KEY"),
    )

    logger.info("ChatGPT 4o loaded!")
    
    result = await openai_model_client.create([UserMessage(content="What is the capital of France?", source="user")])
    print(result)
    await openai_model_client.close()

# asyncio.run(fun())

"""
text b/w agents
"""

from autogen_agentchat.messages import TextMessage

async def fun1():
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key=os.getenv("API_KEY"),
    )

    logger.info("ChatGPT 4o loaded!")

    text_message = TextMessage(content="Hello, world!", source="User") # TextMessage is for agent-to-agent
    logger.info(f"TextMessage type: {type(text_message)}")

    result = await openai_model_client.create([text_message])
    print(result)
    await openai_model_client.close()

# asyncio.run(fun1()) # ERROR: unknown message type!

"""
images b/w agents
"""

from io import BytesIO

import requests
from autogen_agentchat.messages import MultiModalMessage
from autogen_core import Image as AGImage
from PIL import Image

pil_image = Image.open(BytesIO(requests.get("https://picsum.photos/300/200").content))
img = AGImage(pil_image)
multi_modal_message = MultiModalMessage(content=["Can you describe the content of this image?", img], source="User")

"""
agents
"""
# NOTE: agents are stateful!
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import StructuredMessage
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Define a tool that searches the web for information.
# For simplicity, we will use a mock function here that returns a static string.
async def web_search(query: str) -> str:
    """Find information on the web"""
    return "AutoGen is a programming framework for building multi-agent applications."


async def fun3():
    # Use asyncio.run(agent.run(...)) when running in a script.
    # Doesn't seem too stateful...
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key=os.getenv("API_KEY"),
    )

    logger.info("ChatGPT 4o loaded!")

    # Create an agent that uses the OpenAI GPT-4o model.
    agent = AssistantAgent(
        name="assistant",
        model_client=openai_model_client,
        tools=[web_search],
        system_message="Use tools to solve tasks.",
        # reflect_on_tool_use=True, # ReActs (?)
    )

    # Without streaming:
    # result = await agent.run(task="Find information on AutoGen") 
    # for m in result.messages:
    #     print(m.content)

    # With streaming:
    # async for m in agent.run_stream(task="Find information on Autogen"):
    #     if hasattr(m, "type") and m.type == "TextMessage":
    #         print(m.content)
    #     elif hasattr(m, "type"):
    #         print(m.type)

    # With streaming (console):
    # await Console(
    #     agent.run_stream(task="Find information on AutoGen"),
    #     output_stats=True,  # Enable stats printing.
    # )

    # Multimodal:
    # async for m in agent.run_stream(task=multi_modal_message):
        # if hasattr(m, "type") and m.type == "TextMessage":
        #     print(m.content)
        # elif hasattr(m, "type"):
        #     print(m.type)

    pass

# asyncio.run(fun3())

"""
More tools
"""

from autogen_ext.tools.mcp import McpWorkbench, StdioServerParams

async def fun4():
    # Get the fetch tool from mcp-server-fetch.
    fetch_mcp_server = StdioServerParams(command="uvx", args=["mcp-server-fetch"])

    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key=os.getenv("API_KEY"),
    )

    logger.info("ChatGPT 4o loaded!")

    # Create an agent that uses the OpenAI GPT-4o model.
    agent = AssistantAgent(
        name="assistant",
        model_client=openai_model_client,
        tools=[web_search],
        system_message="Use tools to solve tasks.",
        # reflect_on_tool_use=True, # ReActs (?)
    )

    # Create an MCP workbench which provides a session to the mcp server.
    async with McpWorkbench(fetch_mcp_server) as workbench:  # type: ignore
        # Create an agent that can use the fetch tool.
        fetch_agent = AssistantAgent(
            name="fetcher", model_client=openai_model_client, workbench=workbench, reflect_on_tool_use=True
        )

        # Let the agent fetch the content of a URL and summarize it.
        logger.info("Sending message...")
        result = await fetch_agent.run(task="Summarize the content of https://en.wikipedia.org/wiki/Seattle")
        logger.INFO("Receieved response")
        assert isinstance(result.messages[-1], TextMessage)
        print(result.messages[-1].content)

        # Close the connection to the model client.
        await openai_model_client.close()

"""
structured output
"""
from typing import Literal

from pydantic import BaseModel

# The response format for the agent as a Pydantic base model.
class AgentResponse(BaseModel):
    thoughts: str
    response: Literal["happy", "sad", "neutral"]

async def fun5():
    # Create an agent that uses the OpenAI GPT-4o model.
    model_client = OpenAIChatCompletionClient(model="gpt-4o", api_key=os.getenv("API_KEY"))
    agent = AssistantAgent(
        "assistant",
        model_client=model_client,
        system_message="Categorize the input as happy, sad, or neutral following the JSON format.",
        # Define the output content type of the agent.
        output_content_type=AgentResponse,
    )

    result = await Console(agent.run_stream(task="I have mixed emotions. On one hand, I'm pissed that I have to leave. On the other hand, I'm excited for what's ahead."))

    # Check the last message in the result, validate its type, and print the thoughts and response.
    assert isinstance(result.messages[-1], StructuredMessage)
    assert isinstance(result.messages[-1].content, AgentResponse)
    print("Thought: ", result.messages[-1].content.thoughts)
    print("Response: ", result.messages[-1].content.response)
    await model_client.close()


"""
Another streaming option?
"""
async def fun6():
    model_client = OpenAIChatCompletionClient(model="gpt-4o", api_key=os.getenv("API_KEY"))

    streaming_assistant = AssistantAgent(
        name="assistant",
        model_client=model_client,
        system_message="You are a helpful assistant.",
        model_client_stream=True,  # Enable streaming tokens.
    )

    # Use an async function and asyncio.run() in a script.
    async for message in streaming_assistant.run_stream(task="Name two cities in South America"):  # type: ignore
        print(message)

    # result = await Console(streaming_assistant.run_stream(task="Name two cities in South America"))


asyncio.run(fun6())