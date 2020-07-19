import sqlite3

from flask import Flask, url_for, send_from_directory, request
# import section
import os

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pickle as pk
import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger', 'stopwords'])
import re
from machine_learning.prediction_handler import prediction_handler

app = Flask(__name__, static_url_path="/static", static_folder='/Users/majed/Documents/disaster_response/static')
import pandas
import plotly
app._static_folder = 'static'

# the tokenization function to be used, in order to tokeinze the message inputted.
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


@app.route('/')
def root():
    return app.send_static_file('index.html')



@app.route('/repl', methods=['GET', 'POST'])
def func():
    new_freq = request.get_data()
    conn = None

    try:
        conn = sqlite3.connect("DisasterResponse.db")
    except sqlite3.Error as e:
        print("ERROR:      "+e)
    cur = conn.cursor()
    cur.execute('SELECT * FROM "Message"')

    rows = cur.fetchall()
    list = []
    for row in rows:

        list.append(row)
        print(row)


    print("\n\n\n\n\n\n\n " + str(new_freq))
    return convert(list)


def convert(a):
    m = []
    for i in range(len(a)):
        m.append(i)
    print("LENGTH:   " + str(len(a)))
    it = iter(a)
    res_dct = dict(zip(m, it))
    print(res_dct[0])
    return res_dct


@app.route('/predict' , methods=['POST'])
# This function receives the input from the Ajax function, and passes it to the prediction_handler function
def serve_prediction():
    if request.method == "POST":
        print("POST REST    " + str(request.values['message']))
        # input the message received from the POST request to tbe prediction_handler function
        prediction_handler(request.values['message'])
    return "0"


if __name__ == '__main__':
    app.run(debug=True)