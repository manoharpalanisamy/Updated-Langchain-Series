from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
llm_gpt=ChatOpenAI()
##ollama llama2
llm_llama3=Ollama(model="llama3")

prompt1_openai=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2_llama3=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    prompt1_openai|llm_gpt,
    path="/essay"


)

add_routes(
    app,
    prompt2_llama3|llm_llama3,
    path="/poem"


)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)

