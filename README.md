# Task 5 – Sentiment-Aware Chatbot

## Overview
This project implements a **sentiment-aware chatbot** that dynamically adapts
its responses based on the **emotional tone** of user input. The chatbot
detects whether a message is **Positive, Negative, or Neutral** and responds
accordingly to improve user experience and customer satisfaction.

A pre-trained transformer-based sentiment analysis model is used, combined
with rule-based logic to reliably infer neutral sentiment.

---

## Features
- Real-time sentiment analysis
- Detection of Positive, Negative, and Neutral emotions
- Emotion-aware chatbot responses
- Interactive web interface using Streamlit
- Industry-style hybrid approach (model + logic)

---

## Technology Stack
- Python
- Streamlit
- Hugging Face Transformers
- PyTorch

---

## Sentiment Handling Logic
- A binary sentiment model (Positive / Negative) is used.
- **Neutral sentiment** is inferred using:
  - Confidence thresholds
  - Intent-based keyword detection
- This hybrid approach reflects real-world chatbot deployments.

---

## Project Structure
Task5-Sentiment-Aware-Chatbot/
│
├── app.py
├── requirements.txt
└── README.md


---

## How to Run the Project

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2.Run the chatbot:

streamlit run app.py

The application will open automatically in your browser.
