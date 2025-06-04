import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
api_key = os.environ["API_KEY"]

# Round Robin
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import ExternalTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient

from autogen_agentchat.messages import TextMessage

async def rr():
    # Create an OpenAI model client.
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key=api_key, # type: ignore
    )

    # Create the primary agent.
    primary_agent = AssistantAgent(
        "primary",
        model_client=model_client,
        system_message="You are a helpful AI assistant.",
        model_client_stream=True, 
    )

    # Create the critic agent.
    critic_agent = AssistantAgent(
        "critic",
        model_client=model_client,
        system_message="Provide constructive feedback. Respond with 'APPROVE' to when your feedbacks are addressed.",
        model_client_stream=True,
    )

    # Define a termination condition that stops the task if the critic approves.
    text_termination = TextMentionTermination("APPROVE")

    # Create a team with the primary and critic agents.
    team = RoundRobinGroupChat([primary_agent, critic_agent], termination_condition=text_termination)

    # Use `asyncio.run(...)` when running in a script.
    # result = await team.run(task="Write a short poem about the fall season.")
    # print(result)
    # for m in result.messages:
    #     if isinstance(m, TextMessage):
    #         print(m.content)

    # When running inside a script, use a async main function and call it from `asyncio.run(...)`.
    # await team.reset()  # Reset the team for a new task.
    # async for message in team.run_stream(task="Write a short poem about the fall season."):  # type: ignore
    #     if isinstance(message, TaskResult):
    #         print("Stop Reason:", message.stop_reason)
    #     elif isinstance(message, TextMessage):
    #         print(message.content, end="")

    # # Another option
    # await team.reset()  # Reset the team for a new task.
    # await Console(team.run_stream(task="Write a short poem about the fall season."))  # Stream the messages to the console.

    # Explicit termination
    # Create a new team with an external termination condition.
    external_termination = ExternalTermination()
    team = RoundRobinGroupChat(
        [primary_agent, critic_agent],
        termination_condition=external_termination | text_termination,  # Use the bitwise OR operator to combine conditions.
    )

    # Run the team in a background task.
    run = asyncio.create_task(Console(team.run_stream(task="Write a short poem about the fall season.")))

    # Wait for some time.
    await asyncio.sleep(0.1)

    # Stop the team.
    external_termination.set()

    # Wait for the team to finish.
    await run

    # The new task is to translate the same poem to Chinese Tang-style poetry.
    # await Console(team.run_stream(task="将这首诗用中文唐诗风格写一遍。"))

    # Create a cancellation token.
    cancellation_token = CancellationToken()

    # Use another coroutine to run the team.
    run = asyncio.create_task(
        team.run(
            task="Translate the poem to Spanish.",
            cancellation_token=cancellation_token,
        )
    )

    # Cancel the run.
    cancellation_token.cancel()

    try:
        result = await run  # This will raise a CancelledError.
    except asyncio.CancelledError:
        print("Task was cancelled.")


    # await asyncio.sleep(1)

    # await Console(team.run_stream())  # Resume the team to continue the last task.

from autogen_agentchat.conditions import TextMessageTermination

# Create a tool for incrementing a number.
def increment_number(number: int) -> int:
    """Increment a number by 1."""
    return number + 1

async def single_agent_team():
    model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key=api_key,
    # Disable parallel tool calls for this example.
    parallel_tool_calls=False,  # type: ignore
)

    # Create a tool agent that uses the increment_number function.
    looped_assistant = AssistantAgent(
        "looped_assistant",
        model_client=model_client,
        tools=[increment_number],  # Register the tool.
        system_message="You are a helpful AI assistant, use the tool to increment the number.",
    )

    # Termination condition that stops the task if the agent responds with a text message.
    termination_condition = TextMessageTermination("looped_assistant")

    # Create a team with the looped assistant agent and the termination condition.
    team = RoundRobinGroupChat(
        [looped_assistant],
        termination_condition=termination_condition,
    )

    # Run the team with a task and print the messages to the console.
    async for message in team.run_stream(task="Increment the number 5 to 10."):  # type: ignore
        print(type(message).__name__, message)

    await model_client.close()


asyncio.run(single_agent_team())