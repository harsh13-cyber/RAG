from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes

import uvicorn
import os
from langchain_community.llms import Ollama

from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title="Lanchain Server",
    version="1.0",
    description="A Simple API"
)

add_routes(app, ChatOpenAI(), path="/openai")

model = ChatOpenAI()

##ollama llama3.1
llm = Ollama(model = 'llama3.1')

prompt1 = ChatPromptTemplate.from_template("write a essay about {topic} with 100 words")

prompt2 = ChatPromptTemplate.from_template("write a poem about {topic} with 100 words")

add_routes(app, prompt1|model, path='/essay')

add_routes(app, prompt2|llm, path='/poems')

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)