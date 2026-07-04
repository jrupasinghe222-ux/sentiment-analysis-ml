from pydantic import BaseModel


class SentimentRequest(BaseModel):
    review: str