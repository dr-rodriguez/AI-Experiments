import asyncio
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

load_dotenv()


@tool
def get_weather(location: str) -> str:
    """Get the current weather in a given location."""
    return f"It's always sunny in {location}!"


# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
messages = []  # Maintain conversation history

# Bind tools to the model
model_with_tools = model.bind_tools([get_weather])


async def chatbot_loop(user_query: str):
    """Async chatbot that can call tools."""
    messages.append(HumanMessage(content=user_query))
    
    # Initial LLM call (async)
    response = await model_with_tools.ainvoke(messages)
    
    # Process tool calls if the model made any
    while response.tool_calls:
        tool_map = {"get_weather": get_weather}
        
        # Execute all tool calls (you can parallelize this)
        tool_results = []
        for tool_call in response.tool_calls:
            tool = tool_map[tool_call["name"]]
            result = tool.invoke(tool_call["args"])  # Tool execution itself
            tool_results.append(ToolMessage(
                content=result,
                tool_call_id=tool_call["id"]
            ))
        
        # Add model response and tool results to conversation
        messages.extend([response, *tool_results])
        
        # Call model again with tool results (async)
        response = await model_with_tools.ainvoke(messages)

    # Check if content is present in response
    if not response.content:
        output = response[0].text
    else:
        output = response.content

    # Return final response (no more tool calls)
    return output


async def main():

    print("Chat with Google Generative AI (type 'exit' or 'quit' to quit):\n")

    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["exit", "quit"]:
            break

        response = await chatbot_loop(user_input)
        print("Assistant:", response)

if __name__ == "__main__":
    asyncio.run(main())
