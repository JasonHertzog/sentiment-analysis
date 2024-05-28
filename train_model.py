<<<<<<< HEAD
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

    model = LogisticRegression(max_iter=500)
    model.fit(X_train_vec, y_train)
    accuracy = model.score(X_test_vec, y_test)
    print(f"Model Accuracy: {accuracy}")

    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)

if __name__ == "__main__":
    train_model('data/imdb_preprocessed.csv', 'sentiment_model_imdb.joblib', 'vectorizer_imdb.joblib')
=======
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import config

# Directory to the data
dir = config.dir

# Load the preprocessed data
X_train, X_test, y_train, y_test = joblib.load(dir+'data.pkl')

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))

# Save the model
joblib.dump(model, dir+'sentiment_model.pkl')
>>>>>>> 1dba52abeb86358e14ad09c41672dfc8341ea0ac
