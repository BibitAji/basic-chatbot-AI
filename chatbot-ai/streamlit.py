import streamlit as st
import json

# Load FAQs from JSON
with open('data/faqs.json', 'r') as file:
    faqs = json.load(file)["faqs"]

# Function to get response from chatbot
def get_response(user_input):
    # Implement your chatbot logic here
    for question, answer in faqs.items():
        if user_input.lower() in question.lower():
            return answer
    return "I'm sorry, I don't understand your question."

# Streamlit UI
def main():
    st.title('Basic AI Chatbot')

    # User input box
    user_input = st.text_input('You:', '')

    # Respond to user input
    if st.button('Send'):
        if user_input:
            bot_response = get_response(user_input)
            st.text('Bot:', bot_response)

if __name__ == '__main__':
    main()
