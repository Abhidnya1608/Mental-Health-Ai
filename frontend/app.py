import streamlit as st

st.set_page_config(
    page_title = "Mental Wellness Ai",
    page_icon = "🧠"
)

st.title("Mental Wellness Ai")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your message...")


if prompt:
    st.session_state.messages.append(
        {
            'role':'user',
            'content': prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = "Hello! I am your Mental Wellness Ai"

    st.session_state.messages.append(
    {
        'role':'assistant',
        'content': response
    }
)

    with st.chat_message("assistant"):
        st.markdown(response)


# user_input = st.chat_input("Type ur message")

# if user_input:
#     st.chat_message("user").write(user_input)
#     st.chat_message("assistant").write("Hey i am your assistent")