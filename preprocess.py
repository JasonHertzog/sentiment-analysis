import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import config

# Get directory from config
dir = config.dir

# Load the dataset
data = pd.read_csv(dir + 'IMDB Dataset.csv')

# Preprocess the text data
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['review'])
y = data['sentiment'].apply(lambda x: 1 if x == 'positive' else 0)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the preprocessed data
joblib.dump((X_train, X_test, y_train, y_test),dir+'data.pkl')
joblib.dump(vectorizer, dir+'vectorizer.pkl')

