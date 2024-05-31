import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def train_model(file_path, model_path, vectorizer_path):
    data = pd.read_csv(file_path)
    X_train, X_test, y_train, y_test = train_test_split(data['text'], data['target'], test_size=0.2, random_state=42)

    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1500)
    model.fit(X_train_vec, y_train)
    accuracy = model.score(X_test_vec, y_test)
    print(f"Model Accuracy: {accuracy}")

    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)

if __name__ == "__main__":
    # Train and save IMDB model
    train_model('data/imdb_preprocessed.csv', 'sentiment_model_imdb.joblib', 'vectorizer_imdb.joblib')
    # Train and save Sentiment140 model
    train_model('data/sentiment140_preprocessed.csv', 'sentiment_model_sent140.joblib', 'vectorizer_sent140.joblib')
