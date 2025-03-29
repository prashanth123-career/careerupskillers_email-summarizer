import streamlit as st
from transformers import pipeline

# Load the AI model for summarization
@st.cache_resource
def load_model():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_model()

# Streamlit Web App UI
st.set_page_config(page_title="AI Email Summarizer", page_icon="📩")
st.title("📩 AI Email Summarizer")
st.write("Paste your email below and get a concise summary!")

# Text Input for Email
email_text = st.text_area("✉️ Enter Email Content:")

# Summarize Button
if st.button("Summarize Email"):
    if email_text.strip():
        with st.spinner("Generating summary..."):
            summary = summarizer(email_text, max_length=50, min_length=10, do_sample=False)
            st.subheader("📌 AI Summary:")
            st.success(summary[0]['summary_text'])
    else:
        st.warning("Please enter an email to summarize.")

# Footer
st.markdown("---")
st.caption("🚀 Powered by AI | Developed by CareerUpskillers")
