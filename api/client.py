import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/essay_chatgpt/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/essay_llama3/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

    ## streamlit framework

st.title('Langchain Demo With ChatGPT and LLAMA3 API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a essay on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))
