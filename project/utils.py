import nltk
import pickle
import re
import numpy as np

nltk.download('stopwords')
from nltk.corpus import stopwords

# Paths for all resources for the bot.
RESOURCE_PATH = {
    'INTENT_RECOGNIZER': 'data/intent_recognizer.pkl',
    'TAG_CLASSIFIER': 'data/tag_classifier.pkl',
    'TFIDF_VECTORIZER': 'data/tfidf_vectorizer.pkl',
    'THREAD_EMBEDDINGS_FOLDER': 'data/thread_embeddings_by_tags',
    'WORD_EMBEDDINGS': 'data/word_embeddings.tsv',
    'CHATTER_BOT': 'data/chatterbot.sqlite3',
}


def text_prepare(text):
    """Performs tokenization and simple preprocessing."""
    
    replace_by_space_re = re.compile('[/(){}\[\]\|@,;]')
    bad_symbols_re = re.compile('[^0-9a-z #+_]')
    stopwords_set = set(stopwords.words('english'))

    text = text.lower()
    text = replace_by_space_re.sub(' ', text)
    text = bad_symbols_re.sub('', text)
    text = ' '.join([x for x in text.split() if x and x not in stopwords_set])

    return text.strip()


def load_embeddings(embeddings_path):
    """Loads pre-trained word embeddings from tsv file.

    Args:
      embeddings_path - path to the embeddings file.

    Returns:
      embeddings - dict mapping words to vectors;
      embeddings_dim - dimension of the vectors.
    """
    embeddings = { a[0]: np.array(a[1:], dtype=np.float32) \
                   for a in [line.strip().split('\t') \
                              for line in open(embeddings_path)] } 
    vect = next (iter (embeddings.values()))
    return embeddings, len(vect)


def question_to_vec(question, embeddings, dim):
    """
        question: a string
        embeddings: dict where the key is a word and a value is its' embedding
        dim: size of the representation

        result: vector representation for the question
    """    
    vec = np.zeros(dim)
    n = 0
    for word in question.split():
        if word in embeddings:
            vec += embeddings[word]
            n += 1
    if n > 1:
        vec /= n
    return vec


def unpickle_file(filename):
    """Returns the result of unpickling the file content."""
    with open(filename, 'rb') as f:
        return pickle.load(f)
