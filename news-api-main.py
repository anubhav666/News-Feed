import streamlit as st
import json
import requests
from newspaper import Article
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
    response_dict = json.loads(response.text)
    links = [response_dict['articles'][i]['link'] for i in range(len(response_dict['articles']))]
    for link in links:
        news_article = Article(link, language = 'en')
        news_article.download()
        news_article.parse()
        article_titles.append(news_article.title)
        article_texts.append(news_article.text)
    for text in article_texts:
        article_summaries.append(summarizer(text)[0]['summary_text'])
    for i in range(len(article_texts)):
        st.header(article_titles[i])
        st.subheader('Summary of Article')
        st.markdown(article_summaries[i])
        with st.expander('Full Article'):
            st.markdown(article_texts[i])
if __name__=='__main__':
    run()
