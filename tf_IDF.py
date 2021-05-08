import textCleaning
from gensim import models
from gensim import similarities

def get_closest_n(query, n, dictionary, index, tfidf, text_docs):
    '''get the top matching docs as per cosine similarity
    between tfidf vector of query and all docs'''
    query_document = textCleaning.cleaning_pipe(query)
    query_bow = dictionary.doc2bow(query_document)
    sims = index[tfidf[query_bow]]
    top_idx = sims.argsort()[-1*n:][::-1]
    answer = [text_docs[i] for i in top_idx]
    print([sims[i] for i in top_idx])
    return answer
