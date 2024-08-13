import numpy as np
import pandas as pd
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer


# Load the logistic regression model and vectorizer
with open('model/logistic_model.pkl', 'rb') as file:
    lm = pickle.load(file)

with open('model/vectoriser.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Initialize stopwords and Porter Stemmer
stop_words = stopwords.words('english')
port_stem = PorterStemmer()

def stemming(content):
    """
    Perform stemming and remove stopwords from the content.
    """
    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if word not in stop_words]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content

def predict(content):
    """
    Predict the class of the content using the loaded model.
    """
    stemmed_content = stemming(content)
    vectorized_content = vectorizer.transform([stemmed_content])  # Use transform method
    output = lm.predict(vectorized_content)
    return output[0],stemmed_content

# Example usage
if __name__ == "__main__":
    # Test the prediction function with some example content
    test_content = "FLYNN: Hillary Clinton, Big Woman on Campus - Breitbart"
    if predict(test_content)[0]==1:
        prediction='Real'
    else:
        prediction='Fake'
    print(f"The prediction for the given content is: {prediction}\n {predict(test_content)[1]}")
