
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv


# Load environment variables

load_dotenv()



# Set OpenAI API Key 

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")



# Langsmith Tracking - To Capture all monitoring results

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")




# Define the Prompt Template

prompt = ChatPromptTemplate.from_messages([

    ("system", "You are a helpful assistant. Please respond to the user's query."),
    ("User", "Question:{question}")
    
])




# Streamlit Framework

st.title("LangChain Demo with OpenAI")
input_text = st.text_input("Search the topic you want to know about:")





# Define the LLM

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.75, max_tokens=1000)

# Define the Output Parser

output_parser = StrOutputParser()

# Define the Chain

chain = prompt | llm | output_parser


if input_text:

    st.write(chain.invoke({"question": input_text}))


