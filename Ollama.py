
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st



# Define the Prompt Template

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's query."),
    ("user", "Question: {question}")
])


# Streamlit Framework

st.title("LangChain Demo with Llama")
input_text = st.text_input("Search the topic you want to know about:")



# Define the LLM

llm = Ollama(model="Gemma")

# Define the Output Parser

output_parser = StrOutputParser()

# Define the Chain

chain = prompt | llm | output_parser


if input_text:
    st.write(chain.invoke({"question": input_text}))

