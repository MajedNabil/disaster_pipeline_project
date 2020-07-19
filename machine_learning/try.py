import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger', 'stopwords'])

import re
import numpy as np
import pandas as pd
import pickle as pk
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_multilabel_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sqlalchemy import create_engine
from nltk.corpus import stopwords


def tokenize(text):
    x = 0
    # normalize the text
    preprocessed_text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    # tokenize sentence
    tokens = word_tokenize(preprocessed_text)
    # remove the
    x = x + 1
    tokens = [w for w in tokens if w not in stopwords.words("english")]
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
    return clean_tokens


loaded_model = pk.load(open("finalized_model.pkl", 'rb'))



# use for prediction

string = tokenize("A Comitee in Delmas 19, Rue ( street ) Janvier, Impasse Charite #2. We have about 500 people in a temporary shelter and we are in dire need of Water, Food, Medications, Tents and Clothes. Please stop by and see us.")
print(string)
print("-------")
res = loaded_model.predict(string)[0]
print(str(res))
