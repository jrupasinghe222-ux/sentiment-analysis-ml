import joblib
from app.preprocessing import preprocess_text

pipeline = joblib.load(
    "models/sentiment_pipeline.pkl"
)

review = "I absolutely loved this movie."

review = preprocess_text(review)

prediction = pipeline.predict([review])

print(prediction[0])

# print(pipeline.classes_)
probabilities = pipeline.predict_proba([review])

print(probabilities)