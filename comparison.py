import streamlit as st
import PyPDF2
import docx
from transformers import pipeline
from groq import Groq
import os

api_key = os.getenv("GROQ_API_KEY")

# API Configuration (Replace with your actual API key)
client = Groq(api_key=api_key)

# Load NER model for entity recognition
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

def extract_text_from_pdf(uploaded_file):
    text = ""
    reader = PyPDF2.PdfReader(uploaded_file)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()

# Function to compare two documents using Groq API
def compare_documents(text1, text2):
    if not text1 or not text2:
        return "One or both documents are empty."

    prompt = f"""
    Compare the two files and make comparison in tabular format. Make two columns doc1 and doc2 
    compare the two docs on the basis of features, diffence between information given in that file. just make 2 columns no need to add column of points to comparison
    """

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content.strip()
