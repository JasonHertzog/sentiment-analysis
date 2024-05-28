import pandas as pd

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
