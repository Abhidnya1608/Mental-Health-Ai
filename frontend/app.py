import streamlit as st

st.set_page_config(
    page_title = "Mental Wellness Ai",
    page_icon = "🧠"
)

st.title("Mental Wellness Ai")

user_input = st.chat_input("Type your messages....")


if user_input:
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write("Backend is not connected")