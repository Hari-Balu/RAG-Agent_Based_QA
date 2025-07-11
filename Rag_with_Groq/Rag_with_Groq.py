

import os
import time
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain


# Load environment variables from .env file

from dotenv import load_dotenv
load_dotenv()


# Set up the Groq API key

groq_api_key = os.getenv("GROQ_API_KEY")

if "vector_store" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings()
    st.session_state.loader = WebBaseLoader("https://docs.smith.langchain.com/")
    st.session_state.documents = st.session_state.loader.load()
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.split_docs = st.session_state.text_splitter.split_documents(st.session_state.documents[:50])
    st.session_state.vector_store = FAISS.from_documents(st.session_state.split_docs, st.session_state.embeddings)

st.title("Chat Groq Demo")

LLM = ChatGroq(groq_api_key = groq_api_key, model_name="Gemma-7b-It")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that answers questions based on the provided context.")
    , ("Question", "{context}\n\n{question}")
])




chain = create_stuff_documents_chain(llm=LLM,prompt=prompt)

retriever = st.session_state.vector_store.as_retriever()

retrieval_chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=chain)

prompt = st.text_input("Enter your promt here:")


if prompt:

    start = time.process_time()
    Response = retrieval_chain.invoke({"question": prompt})
    print("Response Time :", time.process_time() - start)
    st.write(Response["answer"])



