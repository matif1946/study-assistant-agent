from agents import Agent, Runner, SQLiteSession
import asyncio
from tools import WebSearchTool

agent = Agent(
    name="Study Assistant",
    instructions="You are a helpful study assistant.",
    tools=[
        WebSearchTool()
           ]
    )

session = SQLiteSession("Study Assistant")

async def main():
    while True:
        user_message=input("User: ")
        if user_message == "exit":
            break
        else:
            result = await Runner.run(
                agent,
                user_message,
                session=session
            )
            print(f"Agent: {result.final_output}")

asyncio.run(main())