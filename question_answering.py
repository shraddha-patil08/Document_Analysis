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

def answer_question(text, question):
    if not text.strip():
        return "No content available to answer the question."
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an AI assistant that answers questions based on given text."},
            {"role": "user", "content": f"Based on the following content, answer the question concisely:\n\n{text}\n\nQuestion: {question}"}
        ],
        model="llama-3.3-70b-versatile",
    )
    
    return chat_completion.choices[0].message.content.strip()
