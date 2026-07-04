from fastapi import FastAPI

from app.schemas import SentimentRequest
from app.predictor import predict_sentiment

app = FastAPI(
    title="Movie Sentiment Analysis API"
)


@app.post("/predict")
def predict(request: SentimentRequest):

    return predict_sentiment(
        request.review
    )