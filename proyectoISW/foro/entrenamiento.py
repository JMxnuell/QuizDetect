import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler
import nltk
from nltk.stem.porter import *

nltk.download('stopwords')
nltk.download('punkt')

stopwords = nltk.corpus.stopwords.words("spanish")
stemmer = PorterStemmer()

def tokenize(frase):
    tokens = nltk.word_tokenize(frase)
    tokens_cleaned = [token.lower() for token in tokens if token.isalpha()]
    tokens_stemm = [stemmer.stem(t) for t in tokens_cleaned]
    return tokens_stemm

df = pd.read_csv("C:\\Users\\J Suarez\\Documents\\PROYECTO_ISW\\proyectoISW\\foro\\dataset_2.csv")


# In[ ]:


df["Toxic/Not Toxic"][df["Toxic/Not Toxic"] == "Toxic"] = 1
df["Toxic/Not Toxic"][df["Toxic/Not Toxic"] == "Not Toxic"] = 0
texto = df["Message Text"]
label = df["Toxic/Not Toxic"]
dict = {"Texto":texto, "Label":label}
df_clean = pd.DataFrame(dict)


# In[ ]:


df_clean = df_clean.dropna()
df_clean = shuffle(df_clean)


# In[ ]:





# In[ ]:


vectorizer = TfidfVectorizer(
    tokenizer=tokenize,
    ngram_range=(1,3),
    stop_words=stopwords,
    )


# In[ ]:


tfidf = vectorizer.fit_transform(df_clean["Texto"]).toarray()


# In[ ]:


X = pd.DataFrame(tfidf)
y = df_clean['Label'].astype(int)


# In[ ]:


from sklearn.model_selection import KFold, GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline


# In[ ]:


param_grid = {'C': np.arange(0.1, 60, 50),
              'penalty': ['l2'] }
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)
kf = KFold(n_splits=6,shuffle = True, random_state=42)
lr = LogisticRegression()

scaler = StandardScaler()
steps = [('scaler', StandardScaler()),
         ('Logistic Regression', LogisticRegression())]

pipeline = Pipeline(steps)

grid_search = GridSearchCV(lr, param_grid, cv=kf)
model = grid_search.fit(X_train, y_train)


# In[ ]:


import joblib

joblib.dump(model, "model.pkl")


# In[ ]:


joblib.dump(vectorizer, 'tfidf.pkl')
