from gensim import corpora
import textCleaning


# Defining text corpus
def create_dictionary(docs):
    'create dictionary of words in preprocessed corpus'
    pdocs = [textCleaning.cleaning_pipe(doc) for doc in docs]
    dictionary = corpora.Dictionary(pdocs)
    dictionary.save('DS.dict')
    return dictionary, pdocs


# Transform complete corpus as BoW
def transform_corpus(pdocs, dictionary):
    bow_corpus = [dictionary.doc2bow(text) for text in pdocs]
    return bow_corpus
