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
