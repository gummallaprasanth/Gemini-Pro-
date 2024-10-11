from dotenv import load_dotenv
load_dotenv() # loading all the enviorment vriables 

import streamlit as st
import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# functions to load gemini pro model and get responses

model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(question ):
    response=model.generate_content(question)
    return response.text

# initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini llm  Application")

input=st.text_input("input : ",key="input")

submit=st.button("ask the question")


# when  submit is called 


if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)