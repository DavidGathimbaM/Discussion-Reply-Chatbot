import streamlit as st
from chatbot_model import ChatbotModel

# Initialize the chatbot model
chatbot = ChatbotModel()

# Streamlit App
st.title("AI Chatbot")

st.write("Welcome to the AI Chatbot! Type a message below to chat.")

# User Input
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input.strip():
        # Generate response
        response = chatbot.generate_response(user_input)
        
        # Display chatbot response
        st.text_area("Chatbot:", response, height=200)
    else:
        st.warning("Please enter a message.")
