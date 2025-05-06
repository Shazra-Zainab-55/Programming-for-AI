import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import os

nltk.download('punkt')
nltk.download('stopwords')

def load_qa_data():
    with open("qa_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

qa_data = load_qa_data()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    return [word for word in tokens if word not in stop_words and word not in string.punctuation]

def get_response(user_input):
    user_tokens = set(preprocess(user_input))
    best_match = ""
    highest_overlap = 0

    for question, answer in qa_data.items():
        question_tokens = set(preprocess(question))
        overlap = len(user_tokens & question_tokens)
        if overlap > highest_overlap:
            highest_overlap = overlap
            best_match = answer

    return best_match if highest_overlap > 0 else "Sorry, I didn't understand that. Try asking something else."
