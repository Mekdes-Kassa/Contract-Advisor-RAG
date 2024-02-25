import streamlit as st
import sys 
sys.path.append('Contract-Advisor-RAG/utils/retr.py') 
from utils.retr import retrieval_augmented_qa_chain
chat=[]
st.container()
user_input=st.chat_input('Enter your question here:')

chat.append(user_input)

def final_result():
    question = user_input
    result = retrieval_augmented_qa_chain.invoke({"question" : question})
    return result['response'].content
# Display the chat history
for message in chat:
    st.text(message)
    final_result()