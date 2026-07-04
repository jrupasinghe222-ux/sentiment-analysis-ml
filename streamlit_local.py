import streamlit as st

from app.predictor import predict_sentiment

st.set_page_config(
    page_title="Movie Sentiment Analyzer",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Sentiment Analyzer")

st.write(
    "Enter a movie review below and the model will predict "
    "whether the sentiment is Positive or Negative."
)

review = st.text_area(
    "Movie Review",
    height=250,
    placeholder="Type or paste a movie review here..."
)

if st.button("Analyze Sentiment"):

    if not review.strip():
        st.warning("Please enter a review.")
        st.stop()

    with st.spinner("Analyzing review..."):

        result = predict_sentiment(review)

    prediction = result["prediction"]
    confidence = result["confidence"]

    if prediction == "positive":
        st.success("😊 Positive Review")
    else:
        st.error("☹️ Negative Review")

    st.metric(
        "Confidence",
        f"{confidence:.2%}"
    )
