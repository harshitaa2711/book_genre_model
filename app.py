from flask import Flask, request, render_template
import pickle
import re
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

# Load model and vectorizer
with open('bookgenremodel.pkl', 'rb') as file:
    model = pickle.load(file)

with open('tfdifvector.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

# Preprocessing functions
def clean_text(text):
    text = re.sub("[^a-zA-Z]", " ", text).lower()
    return ' '.join(text.split())

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    return ' '.join([word for word in text.split() if word not in stop_words])

def lemmatize_text(text):
    lemma = WordNetLemmatizer()
    return ' '.join([lemma.lemmatize(word) for word in text.split()])

def stem_text(text):
    stemmer = PorterStemmer()
    return ' '.join([stemmer.stem(word) for word in text.split()])

def preprocess(text):
    text = clean_text(text)
    text = remove_stopwords(text)
    text = lemmatize_text(text)
    text = stem_text(text)
    return text

def predict_genre(text):
    processed_text = preprocess(text)
    text_vector = tfidf_vectorizer.transform([processed_text])
    predicted = model.predict(text_vector)
    genre_mapper = {0: 'Fantasy', 1: 'Science Fiction', 2: 'Crime Fiction',
                    3: 'Historical Novel', 4: 'Horror', 5: 'Thriller'}
    return genre_mapper.get(predicted[0], "Unknown")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get("summary", "")
        genre = predict_genre(text)
        return render_template('index.html', genre=genre, text=text, showresult=True)
    return render_template('index.html', showresult=False)

if __name__ == '__main__':
    app.run(debug=True)