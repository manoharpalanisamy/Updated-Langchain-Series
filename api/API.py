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
## OpenAI gpt-turbo-3.5
llm_gpt=ChatOpenAI()
##ollama llama2
llm_llama3=Ollama(model="llama3")

prompt1_openai=ChatPromptTemplate.from_template("Write me an essay about {topic} with 50 words in creative way using emojis")
prompt2_llama3=ChatPromptTemplate.from_template("Write me an essay about {topic} with 50 words in creative way using emojis")

add_routes(
    app,
    prompt1_openai|llm_gpt,
    path="/essay_chatgpt"
)

add_routes(
    app,
    prompt2_llama3|llm_llama3,
    path="/essay_llama3"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)

