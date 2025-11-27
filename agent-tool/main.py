import asyncio
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_ollama import ChatOllama

async def chat_loop():
    """Async chatbot that maintains conversation history."""
    model = ChatOllama(model="llama3.2:3b", base_url="http://localhost:11434")
    
    messages = []  # Maintain conversation history
    
    print("Chat with Llama (type 'exit' to quit):\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["exit", "quit"]:
            break
        
        # Add user message to history
        messages.append(HumanMessage(content=user_input))
        
        # Stream the response and accumulate chunks
        full_response = None
        async for chunk in model.astream(messages):
            # Sum chunks to reconstruct full message
            if full_response is None:
                full_response = chunk
            else:
                full_response = full_response + chunk  # Chunks are designed to be added
            
            # Print streaming output in real-time
            print(chunk.content, end="", flush=True)
        
        print()  # Newline after response
        
        # Store the complete accumulated response
        messages.append(AIMessage(content=full_response.content))

if __name__ == "__main__":
    asyncio.run(chat_loop())
