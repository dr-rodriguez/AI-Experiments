import streamlit as st
import asyncio
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

async def main():
    st.title("Simple Ollama Chat")

    # Initialize ChatOllama
    # We use a function to cache the model instance if needed, but for simplicity here we just create it.
    # Streamlit re-runs the script on every interaction, so we need to be careful about resource creation if it's heavy.
    # However, ChatOllama client is lightweight.
    model = ChatOllama(model="llama3.2:3b", base_url="http://localhost:11434")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append(HumanMessage(content=prompt))
        
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Stream the response
            async for chunk in model.astream(st.session_state.messages):
                full_response += chunk.content
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
        
        # Add assistant response to chat history
        st.session_state.messages.append(AIMessage(content=full_response))

if __name__ == "__main__":
    asyncio.run(main())