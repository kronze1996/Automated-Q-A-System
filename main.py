# import textCleaning
import ir
import datasetMaker
import textCleaning
import tf_IDF
import streamlit as st

# Project Title
header = st.beta_container()
with header:
    st.title("Welcome to Automated Q&A bot")

# To fetch the query that is the question
question = st.text_input('Ask a question here:')
# if question:
#     st.write(my_model.predict(sentence))

# # Getting the raw corpus
# pdfList = ["Copy of Applied Data Science.pdf"]
# raw_corpus = datasetMaker.DM(pdfList)
# corpus = textCleaning.cleaning_pipe(raw_corpus)
# dictionary, pdoc = ir.create_dictionary(corpus)
# bow_corpus = ir.transform_corpus(pdoc, dictionary)
# index, tfidf = tf_IDF.tf_idf(bow_corpus, dictionary)
# answer = ''
# for d in tf_IDF.get_closest_n("What is Data Science", 2, dictionary, index, tfidf, raw_corpus):
#     answer += d


# To fetch the predicted result of the query
Answer = st.beta_container()
with Answer:
    st.title("The answer")
    # st.write(answer)
