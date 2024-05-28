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
    app.run(debug=True)
