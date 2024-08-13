from flask import Flask, request, render_template
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__, template_folder='C:\\Users\\swapn\\Videos\\My projects\\Fake News\\templates')

# Load the logistic regression model and vectorizer
with open('model/logistic_model.pkl', 'rb') as file:
    lm = pickle.load(file)

with open('model/vectoriser.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Initialize stopwords and Porter Stemmer
stop_words = stopwords.words('English')
port_stem = PorterStemmer()

def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if word not in stop_words]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        content = request.form.get('news_content')
        stemmed_content = stemming(content)
        vectorized_content = vectorizer.transform([stemmed_content])
        output = lm.predict(vectorized_content)
        predicted_news = 'Real News' if output == 1 else 'Super Fake!!!'
        return render_template('index.html', predicted_news=predicted_news)

# Python main
if __name__ == "__main__":
    app.run(debug=True)
