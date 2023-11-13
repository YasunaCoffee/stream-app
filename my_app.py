import streamlit as st

st.set_page_config(
    page_title="My Great ChatGPT",
    page_icon="🤗"
)
st.header("My Great ChatGPT 🤗")
if user_input := st.chat_input("聞きたいことを入力してね！"):
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.spinner("ChatGPT is typing ..."):
        response = llm(st.session_state.messages)
