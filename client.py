
import requests
import streamlit as st



# Function to get response from OpenAI & Ollama API for essay generation

def get_openai_response(input_text):

    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={ "input": { "topic" :input_text }})
    
    return response.json()['output']['content']


def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={ "input": { "topic" :input_text }})
    
    return response.json()['output']['content']



# Streamlit app to interact with the API

st.title("LangChain OpenAI API & Gemma")

input_text1 = st.text_input("Enter a topic for the essay:")
input_text2 = st.text_input("Enter a topic for the poem:")


if input_text1:
    st.write(get_openai_response(input_text1))


if input_text2:
    st.write(get_ollama_response(input_text2))    