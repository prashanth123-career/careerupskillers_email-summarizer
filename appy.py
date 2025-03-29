import streamlit as st
from transformers import pipeline
import docx2txt
import PyPDF2

# Set Streamlit config
st.set_page_config(page_title="AI Email Summarizer", page_icon="📩")

# Load summarization model
@st.cache_resource
def load_model():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_model()

# UI Layout
st.title("📩 AI Email Summarizer")
st.write("Paste your email below or upload a PDF/DOCX file to get a concise summary!")

# --- Input Options ---
option = st.radio("Choose input type:", ["📝 Paste Text", "📄 Upload PDF or DOCX"])

email_text = ""

# Paste Text Option
if option == "📝 Paste Text":
    email_text = st.text_area("✉️ Enter Email Content:")

# File Upload Option
else:
    uploaded_file = st.file_uploader("Upload PDF or DOCX file", type=["pdf", "docx"])
    
    if uploaded_file:
        file_type = uploaded_file.name.split(".")[-1]

        try:
            if file_type == "pdf":
                reader = PyPDF2.PdfReader(uploaded_file)
                email_text = ""
                for page in reader.pages:
                    email_text += page.extract_text()
            elif file_type == "docx":
                email_text = docx2txt.process(uploaded_file)
        except Exception as e:
            st.error(f"❌ Error reading file: {e}")

# --- Summarize Button ---
if st.button("Summarize Email"):
    if email_text.strip():
        with st.spinner("Generating summary..."):
            summary = summarizer(email_text, max_length=50, min_length=10, do_sample=False)
            st.subheader("📌 AI Summary:")
            st.success(summary[0]['summary_text'])
    else:
        st.warning("Please paste text or upload a file.")

# Footer
st.markdown("---")
st.caption("🚀 Powered by AI | Developed by CareerUpskillers")
