import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix)
from app.preprocessing import preprocess_text
import joblib

df = pd.read_csv("data/imdb_dataset.csv")

X = df["review"]
y = df["sentiment"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

X_train = X_train.apply(preprocess_text)
X_test = X_test.apply(preprocess_text)

pipeline = Pipeline ([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.4f}")


# Classification Report
print("\nClassification Report")
print(classification_report(y_test, predictions))


# Confusion Matrix
print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

joblib.dump(
    pipeline,
    "models/sentiment_pipeline.pkl"
)

print("Model saved successfully!")