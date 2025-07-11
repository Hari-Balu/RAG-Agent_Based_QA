
from fastapi import FastAPI
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from langchain_community.llms import Ollama 
import os
from dotenv import load_dotenv
import uvicorn




# Load environment variables from .env file

load_dotenv()


# Set OpenAI API Key 

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# Initialize FastAPI app

app = FastAPI(

    title="LangChain OpenAI API",
    description="A simple API to interact with OpenAI using LangChain",
    version="1.0"

)

# Add routes to the FastAPI app

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

Model = ChatOpenAI()

llm = Ollama(model="Gemma")



# Define a simple prompt template

Prompt1 = PromptTemplate.from_template(
    "Write an essay about {topic} in 100 words.")

Prompt2 = PromptTemplate.from_template(
    "Write a poem about {topic} for a 5 year old child in 100 words.")




# Define a route to get the response from the LLM

add_routes(
    app,
    Prompt1| Model,              #-------> For Open AI
    path="/essay/{topic}",
   
)

add_routes(
    app,
    Prompt2 | llm,                #-------> For Ollama
    path="/poem/{topic}"

)    


# Run the FastAPI app using uvicorn

if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8000)


