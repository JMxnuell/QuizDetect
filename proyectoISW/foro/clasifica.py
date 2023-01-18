import joblib


mt = joblib.load('C:\\Users\\J Suarez\\Documents\\PROYECTO_ISW\\proyectoISW\\foro\\model_and_token.joblib')
tokenize = mt['tokenize_function']
tfidf = mt['model']
model = joblib.load('C:\\Users\\J Suarez\\Documents\\PROYECTO_ISW\\proyectoISW\\foro\\model.pkl')


def clasificaa(texto):

    tfidf.transform(texto).toarray()
    return model.predict([texto])[0]