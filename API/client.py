import requests
import streamlit as st

def get_openai_response(input_text):
    response= requests.post("http://localhost:8000/essay/invoke", json={'input':{'topic': input_text}})
    return response.json()['output']['content']

def get_llama_response(input_text):
    response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']


st.title('demo')
input_text = st.text_input("openAi api call with essay")
input_text1 = st.text_input("llama api call with poen")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_llama_response(input_text1))

