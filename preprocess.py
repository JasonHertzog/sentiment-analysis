import pandas as pd
<<<<<<< HEAD

def preprocess_imdb():
    data = pd.read_csv('data/IMDB Dataset.csv')
    data['sentiment'] = data['sentiment'].map({'positive': 1, 'negative': 0})
    data = data[['review', 'sentiment']]
    data.columns = ['text', 'target']
    data.to_csv('data/imdb_preprocessed.csv', index=False)
    return data

def preprocess_sentiment140():
    data = pd.read_csv('data/sentiment140.csv', encoding='ISO-8859-1', header=None)
    data.columns = ['target', 'ids', 'date', 'flag', 'user', 'text']
    data = data[data['target'].isin([0, 4])]
    data['target'] = data['target'].map({0: 0, 4: 1})
    data = data[['text', 'target']]
    return data

def preprocess_all():
    imdb_data = preprocess_imdb()
    sentiment140_data = preprocess_sentiment140()
    combined_data = pd.concat([imdb_data, sentiment140_data])
    combined_data.to_csv('data/combined_preprocessed.csv', index=False)

if __name__ == "__main__":
    preprocess_all()
=======
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

>>>>>>> 1dba52abeb86358e14ad09c41672dfc8341ea0ac
