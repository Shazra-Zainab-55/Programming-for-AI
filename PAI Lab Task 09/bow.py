import nltk
import re 
import numpy as np
# Download necessary tokenizer
nltk.download('punkt')
# Sample text
text = """My name is Shazra Zainab"""
# Tokenize into sentences
dataset = nltk.sent_tokenize(text)
# Preprocess each sentence
for i in range(len(dataset)): 
	dataset[i] = dataset[i].lower()                      # convert to lowercase
	dataset[i] = re.sub(r'\W', ' ', dataset[i])          # remove non-word characters
	dataset[i] = re.sub(r'\s+', ' ', dataset[i])         # remove extra spaces
# Print the final cleaned text
print("Preprocessed Sentences:")
print(dataset)
