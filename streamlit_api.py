import requests
import streamlit as st

API_URL = "http://localhost:8000/predict"

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

    try:

        with st.spinner("Analyzing review..."):

            response = requests.post(
                API_URL,
                json={
                    "review": review
                },
                timeout=10
            )

        if response.status_code == 200:

            result = response.json()

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


        else:

            st.error(
                f"API returned status code {response.status_code}"
            )

            try:
                st.json(response.json())
            except Exception:
                st.write(response.text)

    except requests.exceptions.ConnectionError:

        st.error(
            "Could not connect to the API.\n\n"
            "Make sure FastAPI is running on http://localhost:8000."
        )

    except requests.exceptions.Timeout:

        st.error(
            "The request timed out."
        )

    except Exception as e:

        st.error(
            f"An unexpected error occurred:\n\n{e}"
        )