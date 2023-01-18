import nltk
from nltk.stem.porter import *
#nltk.download('stopwords')
#nltk.download('punkt')

stopwords = nltk.corpus.stopwords.words("spanish")
stemmer = PorterStemmer()

def tokenize(frase):
    tokens = nltk.word_tokenize(frase)
    tokens_cleaned = [token.lower() for token in tokens if token.isalpha()]
    tokens_stemm = [stemmer.stem(t) for t in tokens_cleaned]
    return tokens_stemm