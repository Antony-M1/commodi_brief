import streamlit as st
from cb_util import get_logger


logger_st = get_logger("Streamlit", "app.log")


logger_st.info("App Started Running")

st.title("Document Summarizer")

st.write("Upload a PDF document to extract and summarize key sections based on categories.")


uploaded_file = st.file_uploader("Upload PDF", type="pdf")
if uploaded_file:
    logger_st.info("File uploaded successfully")
    with st.spinner("Extracting and processing PDF..."):
        import time
        time.sleep(5)
