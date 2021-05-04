from gensim.parsing import strip_tags, strip_numeric, \
    strip_multiple_whitespaces, strip_punctuation, \
    remove_stopwords, preprocess_string
import re

# Method does the filtering of all the unrelevant text elements


def cleaning_pipe(document):

    transform_to_lower = lambda s: s.lower()
    remove_single_char = lambda s: re.sub(r'\s+\w{1}\s+', '', s)

    # Filters to be executed in pipeline
    CLEAN_FILTERS = [strip_tags, strip_numeric, strip_punctuation, strip_multiple_whitespaces, transform_to_lower, remove_stopwords, remove_single_char]

    # Invoking gensim.parsing.preprocess_string method with set of filters
    processed_words = preprocess_string(document, CLEAN_FILTERS)
    return processed_words
