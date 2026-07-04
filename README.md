# Movie Sentiment Analysis using Machine Learning

A complete end-to-end **Machine Learning + NLP project** that classifies movie reviews as **Positive** or **Negative** using a Logistic Regression model trained on TF-IDF features. The project includes both an **API-based architecture (FastAPI)** and a **standalone deployment version (Streamlit)**.

## Live Demo
https://sentiment-analysis-ml-ezouxrbvgwhftn5abssgrm.streamlit.app/

## Project Overview

This project analyzes movie reviews and predicts sentiment using classical NLP techniques.

It demonstrates:
- Text preprocessing
- Feature extraction using TF-IDF
- Model training using Logistic Regression
- REST API development using FastAPI
- Interactive UI using Streamlit
- Modular ML system design

## Tech Stack

- Python
- Scikit-learn
- Pandas
- FastAPI
- Streamlit

## How to Run Locally 
  ### With API
  Run FastAPI Backend
  ```bash
  uvicorn app.api:app
  ```
  Run Streamlit App (API Mode)
  ```bash
  streamlit run streamlit_api.py
  ```
  
  ### Without API
```bash
streamlit run streamlit_local.py
```

## Input
<img width="920" height="548" alt="image" src="https://github.com/user-attachments/assets/b6470077-50ad-4621-b5b5-98f03564d270" />

## Output
<img width="901" height="197" alt="image" src="https://github.com/user-attachments/assets/f59b9fcc-b80b-4ae3-8316-41bd8d19de52" />
