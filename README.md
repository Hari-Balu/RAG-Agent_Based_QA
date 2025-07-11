# 🧠 Multi-Source Q&A system

An intelligent chatbot powered by LangChain Agents and Retrieval-Augmented Generation (RAG) that dynamically fetches context from **Wikipedia**, **ArXiv**, and **Web Pages**, then generates accurate, contextual responses using **Ollama**'s LLMs. 

### 📐 Architecture

```text
User Query ➜ Streamlit UI ➜ LangChain Agent
            ➜ Wikipedia / ArXiv / Web Loader
            ➜ FAISS Vector Store + Ollama Embeddings
            ➜ LLM Response Generated via RAG
```
---


### ✨ Features

- 🔍 **Multi-source Search**: Wikipedia, ArXiv, and live web pages
- 🤖 **LangChain Agentic Routing**: Dynamically picks tools based on user query
- 🧠 **Ollama + FAISS + RAG**: For fast, context-aware, LLM-powered responses
- ⚡ **End-to-End Pipeline**: From query to vector search to LLM response

##

### 📦 Tech Stack

- LangChain — Agents, Tools, VectorStores
- FAISS — Vector similarity search
- Ollama — Local lightweight LLM (llama3.2:3b)
- Streamlit — For UI/UX
- Python — Core logic
- Wikipedia + ArXiv APIs — External tools

##

### 🔮 Future Improvements

 - Add chat history & memory
 - Support PDF uploads as custom sources
 - Add Hugging Face remote model fallback
 - Switch to LangGraph for more control

##

### 🙌 Acknowledgements

- LangChain
- Ollama
- FAISS by Facebook
- Streamlit Team

##

### 📫 Connect with Me

- LinkedIn: [Hariharan Balasubramanian](https://www.linkedin.com/in/hariharan-balasubramanian97)
- Email: hariharanbalasubramanian4@gmail.com

##


### 🙏 Thank You...!!!
