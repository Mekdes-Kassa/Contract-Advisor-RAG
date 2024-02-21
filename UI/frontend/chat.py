import streamlit as st
from transformers import pipeline

# Load the model
chatbot = pipeline("conversational")

# Streamlit app title
st.title("Interactive Chatbot")

# User input
user_input = st.text_input("You:", "")

# Chatbot response
'''if st.button("Send"):
    if user_input:
        bot_response = chatbot(user_input)[0]['generated_text']
        st.text_area("Bot:", value=bot_response, height=100, max_chars=None, key=None)
    else:
        st.warning("Please enter something.")'''