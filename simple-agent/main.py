# Basic setup from the instructions at https://docs.langchain.com/oss/python/integrations/chat/ollama

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
    # other params...
)

if __name__ == "__main__":
    messages = [
        SystemMessage(
            "You are a helpful assistant that translates English to Spanish. Translate the user sentence.",
        ),
        HumanMessage("I love programming."),
    ]
    ai_msg = llm.invoke(messages)
    print(ai_msg.content)
