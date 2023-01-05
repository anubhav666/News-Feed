import streamlit as st
import requests
from transformers import pipeline


st.set_page_config(page_title='Short News App', layout='wide', initial_sidebar_state = 'expanded')
st.title('Welcome to Short News App')
summarizer = pipeline("summarization")
article_titles = []
article_texts = []
article_summaries = []
def run():
    url = "https://animi.p.rapidapi.com/name"
    querystring = {"name":"Levi"}
    headers = {
    "X-RapidAPI-Key": "258f942d2cmsh3f4752cc251327dp105b97jsnba19d0e454cf",
    "X-RapidAPI-Host": "animi.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
if __name__=='__main__':
    run()
