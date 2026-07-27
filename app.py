import streamlit as st

from graph.workflow import app

from memory.conversation_memory import ConversationMemory
import os

os.environ["LANGCHAIN_TRACING_V2"] = "false"
st.set_page_config(
    page_title="CrisisOps AI",
    page_icon="🚚"
)

with st.sidebar:
    st.title("🚚 CrisisOps AI")

    st.markdown("### Available Agents")
    st.success("📦 Shipment Agent")
    st.success("📦 Inventory Agent")
    st.success("🏭 Supplier Agent")
    st.success("🚨 Recovery Agent")
    st.success("📊 Reporting Agent")

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        if "memory" in st.session_state:
            st.session_state.memory.clear()

        st.rerun()

st.title("🚚 CrisisOps AI")
st.subheader(
    "Supply Chain Operations Assistant"
)



# Store conversation history

if "messages" not in st.session_state:

    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])



# User input

user_input = st.chat_input(
    "Ask about shipments, inventory, suppliers..."
)



if user_input:


    # Show user message

    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )
    st.session_state.memory.add_message(
        "user",
        user_input
    )


    with st.chat_message("user"):

        st.write(user_input)



    # Call LangGraph

    # result = app.invoke(
    #     {
    #         "user_input": user_input
    #     }
    # )
    try:
        with st.spinner("🤖 Thinking..."):

            history = st.session_state.memory.get_history()
            st.sidebar.subheader("Memory")
            st.sidebar.text(history)
            result = app.invoke(
                {
                    "user_input": user_input,
                    "history": history
                }
            )
            response=result['response']
    except Exception as e:
        response=f"❌ Error:\n\n{e}"




    # response = result["response"]



    # Show assistant response

    with st.chat_message("assistant"):

        # st.write(response)
        st.markdown(response)




    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )
    st.session_state.memory.add_message(
        "assistant",
        response
    )


    st.sidebar.write(
        "Last User:",
        st.session_state.memory.last_user_message()
    )
    st.sidebar.write(
        "Last Assistant:",
        st.session_state.memory.last_assistant_message()
    )

import json

chat = json.dumps(
    st.session_state.messages,
    indent=4
)

st.sidebar.download_button(
    "Download Chat",
    chat,
    "chat.json"
)
