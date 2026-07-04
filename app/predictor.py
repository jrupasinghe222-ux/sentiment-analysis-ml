import joblib

from app.preprocessing import preprocess_text

# Load the trained pipeline once when the application starts
pipeline = joblib.load("models/sentiment_pipeline.pkl")


def predict_sentiment(review: str):

    # Preprocess the review
    processed_review = preprocess_text(review)

    # Predict sentiment
    prediction = pipeline.predict([processed_review])[0]

    # Predict probabilities
    probabilities = pipeline.predict_proba([processed_review])[0]

    positive_probability = float(probabilities[1])
    negative_probability = float(probabilities[0])

    return {
        "prediction": prediction,
        "confidence": max(
            positive_probability,
            negative_probability
        ),
        "probabilities": {
            "positive": positive_probability,
            "negative": negative_probability
        }
    }