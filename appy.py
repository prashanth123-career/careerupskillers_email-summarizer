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
# --- Promotional Section ---
st.markdown("""
<div class="promo-section">
    <h2>Unlock Your Freelancer Success: Use AI Tools, Strategic Plans, and Free Learning Resources for a Career Transformation! 🚀✨</h2>
    <p>Discover More and Share Your Dreams!</p>
    <h3>3 Steps to Enhance Your Freelance Journey:</h3>
    <ul>
        <li>1. Use our AI Freelancer Kit for ready-to-use templates and tools.</li>
        <li>2. Get our Detailed Career Plan for market insights and strategies.</li>
        <li>3. Leverage our free video links to expand your skills.</li>
    </ul>
    <p><strong>Free Ready-to-Use Chatbot Script Included!</strong></p>
    <p>Join 3,000+ happy buyers around the globe! Get a ₹10,000 worth AI Starter Tool for just ₹499 and receive free AI career counseling. For detailed career counseling, pay only ₹199 to get market insights, skills to upskill, salary comparisons, and companies to apply to.</p>
    <p>Follow the kit and start earning – don’t only rely on jobs as it’s uncertain! Just spend 8 hours on a weekend and start a new earning stream. Half of our students have quit their jobs within six months of purchasing!</p>
</div>
""", unsafe_allow_html=True)

# Purchase Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Purchase AI Freelancer Kit (₹499)", key="emailpromo_freelancer"):
        st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/rzp/t37swnF">', unsafe_allow_html=True)
with col2:
    if st.button("Purchase Detailed Career Plan (₹199)", key="emailpromo_career"):
        st.markdown('<meta http-equiv="refresh" content="0;url=https://rzp.io/rzp/FAsUJ9k">', unsafe_allow_html=True)

# Testimonials
st.markdown("---")
st.markdown("### What Our Users Say")
st.markdown("""
<div class="testimonial">
    <p><i>“The AI Freelancer Kit helped me double my income in just 3 months!” – Ahmed, Freelancer, UAE</i></p>
</div>
<div class="testimonial">
    <p><i>“The Detailed Career Plan gave me a clear path to follow and free courses to upskill!” – Priya, Student, India</i></p>
</div>
""", unsafe_allow_html=True)

