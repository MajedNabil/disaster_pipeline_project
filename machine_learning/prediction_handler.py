# import section
import os

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pickle as pk
import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger', 'stopwords'])
import re


# the tokenization function to be used, in order to tokeinze the message inputted.
def tokenize(text):
    """
    Input
    A sentence (string)

    Output
    A list of tokenized string
    """
    # normalize the text
    preprocessed_text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    # tokenize sentence
    tokens = word_tokenize(preprocessed_text)
    # remove the
    tokens = [w for w in tokens if w not in stopwords.words("english")]
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
    return clean_tokens


# This function takes care of fetching the prediction from
# the ML model, then forwards it back to the UI
def prediction_handler(message):
    """
    Input
    A message inputted by the user

    Output
    A dictionary that contains the values associated with 36 categories
    """
    # load the model from the pickle file
    loaded_model = pk.load(open("finalized_model.pkl", 'rb'))
    # tokenize the message
    tokenized_message = tokenize(message)
    # generate the prediction
    prediction = loaded_model.predict(tokenized_message)[0]
    # the 'prediction' variable contains a vector of 36 element. we need to return its corresponding nominal category
    return convert_to_dictionary(prediction)


# This function receives a list, and it converts it to a dictionary, to return it to the js file
def convert_to_dictionary(list):
    """
    Input
    A list of numbers

    Output
    The data of the list is represented in a form of dictionary,
    so that it can be returned to the js file
    """
    # this list holds the number of indices of the dictionary
    m = []
    for i in range(len(list)):
        m.append(i)
    it = iter(list)
    res_dct = dict(zip(m, it))
    print(res_dct[0])
    return res_dct

