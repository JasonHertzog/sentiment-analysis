<<<<<<< HEAD
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

imdb_model = joblib.load('sentiment_model_imdb.joblib')
imdb_vectorizer = joblib.load('vectorizer_imdb.joblib')
combined_model = joblib.load('sentiment_model_combined.joblib')
combined_vectorizer = joblib.load('vectorizer_combined.joblib')

@app.route('/', methods=['GET', 'POST'])
def home():
    old_result = None
    combined_result = None
    if request.method == 'POST':
        review = request.form['review']
        
        review_vec_imdb = imdb_vectorizer.transform([review])
        prediction_imdb = imdb_model.predict(review_vec_imdb)
        sentiment_imdb = 'Positive' if prediction_imdb == 1 else 'Negative'
        
        review_vec_combined = combined_vectorizer.transform([review])
        prediction_combined = combined_model.predict(review_vec_combined)
        sentiment_combined = 'Positive' if prediction_combined == 1 else 'Negative'

        old_result = sentiment_imdb
        combined_result = sentiment_combined

    return render_template('index.html', old_result=old_result, combined_result=combined_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
from flask import Flask, render_template, request, jsonify
import joblib
import config

app = Flask(__name__)
dir = config.dir
model = joblib.load(dir+'sentiment_model.pkl')
vectorizer = joblib.load(dir+'vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data['review']
    transformed_review = vectorizer.transform([review])
    prediction = model.predict(transformed_review)[0]
    return jsonify({'sentiment': 'positive' if prediction == 1 else 'negative'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

>>>>>>> 1dba52abeb86358e14ad09c41672dfc8341ea0ac
