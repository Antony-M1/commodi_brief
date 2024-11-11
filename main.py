import google.generativeai as genai
import os
import streamlit as st
from cb_util import get_logger, get_hash, VectorDB, get_summary


logger_st = get_logger("Streamlit", "app.log")


logger_st.info("App Started Running")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Document Summarizer")

st.write("Upload a PDF document to extract and summarize key sections based on categories.")


uploaded_file = st.file_uploader("Upload PDF", type="pdf")
if uploaded_file:
    logger_st.info("File uploaded successfully")
    with st.spinner("Extracting and processing PDF..."):
        hash_value = get_hash(uploaded_file)
        vectordb = VectorDB(uploaded_file=uploaded_file)
        st.info("Data loaded successfully")
        query = st.text_input("Ask your Query")
        summary_btn = st.button("Get Summary", type='primary')
        if summary_btn:
            knn = vectordb.get_knn(query)
            response = get_summary(model, knn)
            st.write(response)
