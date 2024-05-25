from flask import Flask, request, jsonify
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
    app.run(debug=True)

