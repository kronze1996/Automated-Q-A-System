import pickle
import ir
# import textCleaning
from gensim import models
from gensim import similarities
import streamlit as st
import tf_IDF
from gensim import corpora
from gensim.parsing import strip_tags, strip_numeric, \
    strip_multiple_whitespaces, stem_text, strip_punctuation, \
    remove_stopwords, preprocess_string
import QuesAns

# Project Title
header= st.beta_container()
with header:
    st.title("Welcome to Automated Q&A bot")

# To fetch the query that is the question  
question=st.text_input('Ask a question here:') 
if question:
  with open('clean_text (1).pkl', 'rb') as p:
    new_docs = pickle.load(p)
  text_docs=[]    
  for ele in new_docs:
    if len(ele) > 50:
      text_docs.append(ele)
    else:
      pass
  # Loading all pickle files
  #dictionary, pdoc = ir.create_dictionary(raw_corpus)
  
  with open('text_docs.pkl', 'rb') as p:
    t_docs = pickle.load(p)
  with open('dictionary (1).pkl', 'rb') as p:
    dictionary = pickle.load(p)
  with open('index (1).pkl', 'rb') as p:
    index = pickle.load(p)
  with open('tfidf (1).pkl', 'rb') as p:
    tfidf = pickle.load(p)
  
  answer=[]
  for d in tf_IDF.get_closest_n(question,5, dictionary, index, tfidf, t_docs):
      answer.append(d)
  Answer=st.beta_container()
  with Answer:
      st.title("The answer")
      st.write(answer)
      
  ans=QuesAns.QuesAnswer(question,answer)

  # To fetch the predicted result of the query
  Answer=st.beta_container()
  with Answer:
      st.title("The answer")
      st.write(ans)
