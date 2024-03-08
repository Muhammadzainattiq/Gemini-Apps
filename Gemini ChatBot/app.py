from dotenv import load_dotenv
load_dotenv() ##loading all the env variables.
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))


## here is a funciton to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Gemini Chatbot")

import streamlit as st

# Add custom CSS for styling the heading
st.markdown("""
    <style>
        .header {
            font-size: 36px;
            color: #1E90FF; /* Change the color as per your preference */
            text-align: center;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2); /* Add shadow effect */
        }
            .response {
            font-size: 24px;
            color: green; /* Change the color as per your preference */
            text-align: left;
            margin-bottom: 20px;
        }
           
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="header">My Custom Gemini ChatBot</h1>', unsafe_allow_html=True)

input_text = st.text_input("Input:", key="input")
submit = st.button("Ask the Question")

if submit:
    response = get_gemini_response(input_text)
    st.markdown('<h1 class="response">Response</h1>', unsafe_allow_html=True)
    st.write(response)

