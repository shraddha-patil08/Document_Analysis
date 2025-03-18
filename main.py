import streamlit as st
import PyPDF2
import docx
from transformers import pipeline
from groq import Groq
from text_extraction import *
from summarization import *
from question_answering import *
from comparison import *
import os


import streamlit as st

# ---- Streamlit UI ----
st.set_page_config(page_title="📄 Smart Document Assistant", layout="wide")

st.title("📄 Smart Document Assistant")
st.write("Upload a document (PDF, DOCX, TXT) to extract insights, summarize, interact with Q&A, and compare documents.")

# File uploader
uploaded_file = st.file_uploader("📂 Upload a Document", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    file_type = uploaded_file.name.split(".")[-1]

    # Extract metadata and text
    metadata, text = extract_features(uploaded_file, file_type)
    title, text = extract_title_and_text(uploaded_file, file_type)

    # Display extracted metadata
    st.subheader("📌 Extracted Document Metadata & Structure:")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Title:** {metadata['Title']}")
        st.write(f"**Author:** {metadata['Author']}")
        st.write(f"**Creation Date:** {metadata['Creation Date']}")
    # with col2:
    #     st.write(f"**Tables Found:** {metadata['Tables']}")
    #     st.write(f"**Images Found:** {metadata['Images']}")

    if metadata["Headings"]:
        st.write(f"**Headings:** {', '.join(metadata['Headings'])}")

    # Display text preview
    st.subheader("📃 Extracted Text Preview:")
    st.text_area("", text[:1500], height=200)

    # Interactive analysis options
    st.subheader("🛠️ Choose an Analysis Feature:")
    option = st.radio("", ["Summarization", "Q&A", "Key Insights"], horizontal=True)

    if option == "Summarization":
        if st.button("✨ Summarize Document"):
            summary = summarize_text(text)
            st.subheader("📝 Summary:")
            st.write(summary)

    elif option == "Q&A":
        user_question = st.text_input("❓ Ask a question about the document:")
        if st.button("🔍 Get Answer") and user_question:
            answer = answer_question(text, user_question)
            st.subheader("💡 Answer:")
            st.write(answer)

    # elif option == "Named Entities":
        #  st.button("🧐 Extract Named Entities"):
        #     entities = extract_entities(text)
        # if  st.subheader("🔍 Named Entities:")
        #     for category, words in entities.items():
        #         st.write(f"**{category}:** {', '.join(set(words))}") if words else st.write(f"**{category}:** None found")

    elif option == "Key Insights":
        if st.button("🔎 Extract Key Insights"):
            key_elements = extract_key_elements(text)
            st.subheader("📌 Key Findings & Recommendations:")
            st.write(key_elements)

# ---- Document Comparison Section ----
st.title("📑 Document Comparison")
st.write("Upload two PDFs to compare differences in content.")

col1, col2 = st.columns(2)
uploaded_file1 = col1.file_uploader("📂 Upload First PDF", type=["pdf"], key="pdf1")
uploaded_file2 = col2.file_uploader("📂 Upload Second PDF", type=["pdf"], key="pdf2")

if uploaded_file1 and uploaded_file2:
    text1 = extract_text_from_pdf(uploaded_file1)
    text2 = extract_text_from_pdf(uploaded_file2)

    if st.button("🔍 Compare Documents"):
        differences = compare_documents(text1, text2)
        st.subheader("📝 Document Differences:")
        st.write(differences)

# st.write("📌 *Built with AI-powered NLP models for accurate text analysis.*")
