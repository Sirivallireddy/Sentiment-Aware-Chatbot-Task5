import streamlit as st
from transformers import pipeline

# Load sentiment model
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Neutral intent keywords (very important)
neutral_keywords = [
    "check", "status", "information", "details", "help",
    "know", "tell", "order", "account", "query", "question"
]

st.title("Sentiment-Aware Chatbot")

user_input = st.text_input("Type your message")

if st.button("Send"):
    if user_input.strip():

        result = sentiment_analyzer(user_input)[0]
        label = result["label"]
        score = result["score"]

        user_lower = user_input.lower()

        # -------- NEUTRAL DETECTION LOGIC --------
        if any(word in user_lower for word in neutral_keywords):
            label = "NEUTRAL"
        elif score < 0.80:
            label = "NEUTRAL"
        # ---------------------------------------

        st.subheader("Detected Sentiment")
        st.write(f"{label} (confidence: {score:.2f})")

        st.subheader("Chatbot Response")

        if label == "POSITIVE":
            st.success(
                "😊 I'm glad to hear that! Thank you for your positive feedback. How else can I help you today?"
            )

        elif label == "NEGATIVE":
            st.error(
                "😔 I'm sorry to hear that. I understand your concern, and I'm here to help resolve it. Could you please tell me more?"
            )

        else:  # NEUTRAL
            st.info(
                "🙂 Thank you for your message. How can I assist you today?"
            )
