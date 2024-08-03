from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("langchain_key")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

prompt1=ChatPromptTemplate.from_template("Write Negatively about {question} ")
prompt2=ChatPromptTemplate.from_template("Write Positively about {question} ")

llm1=Ollama(model="llama2")
llm2=Ollama(model="mistral")

add_routes(
    app,
    prompt1|llm1,
    path="/Neg"
)

add_routes(
    app,
    prompt2|llm2,
    path="/Pos"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)