import streamlit as st
from transformers import pipeline

# Load the AI model for summarization
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Streamlit Web App
st.title("📩 AI Email Summarizer")
st.write("Paste your email below and get a concise summary!")

# Text Input for Email
email_text = st.text_area("✉️ Enter Email Content:")

if st.button("Summarize Email"):
    if email_text.strip():
        summary = summarizer(email_text, max_length=50, min_length=10, do_sample=False)
        st.subheader("📌 AI Summary:")
        st.success(summary[0]['summary_text'])
    else:
        st.warning("Please enter an email to summarize.")

# Footer
st.markdown("---")
st.write("🚀 Powered by AI | Developed by CareerUpskillers")

