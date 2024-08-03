import requests
import streamlit as st

def get_llm1_response(input_text):
    response=requests.post("http://localhost:8000/Neg/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_llm2_response(input_text):
    response=requests.post("http://localhost:8000/Pos/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

st.title("API BOT")
input_text1=st.text_input("Write Negatively")
input_text2=st.text_input("Write Positively")

if input_text1:
    st.write(get_llm1_response(input_text1))

if input_text2:
    st.write(get_llm2_response(input_text2))    
