from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


def get_openai_response(question):
    
    llm=OpenAI(temperature=0.3)
    llm2=HuggingFaceHub(repo_id="google/flan-t5-large")
    response=llm.predict(question)
    return response

st.set_page_config(page_title="CHATBOT")

st.header("CHAT APP")

input=st.text_input("Question: ",key="input")
response=get_openai_response(input)

submit=st.button("Submit")


if submit:
    st.subheader("Response")
    st.write(response)
