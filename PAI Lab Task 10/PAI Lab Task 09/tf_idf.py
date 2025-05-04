from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "My name is Shazra Zainab",
    "I love learning machine learning",
    "Python is great for data science"
]

# Create and fit the vectorizer
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(documents)

# Now this will work:
print("Word indexes:")
print(tfidf.vocabulary_)
