import streamlit as st
import PyPDF2
import docx
from transformers import pipeline
from groq import Groq
from dotenv import *
import os

api_key = os.getenv("GROQ_API_KEY")

# API Configuration (Replace with your actual API key)
client = Groq(api_key=api_key)

# Load NER model for entity recognition
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

def summarize_text(text):
    if not text.strip():
        return "No text found for summarization."
    
    if len(text.split()) < 50:
        return "Text is too short for summarization."
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": f"Summarize the following text concisely in paragraph: {text}"}],
        model="llama-3.3-70b-versatile",
    )
    
    return chat_completion.choices[0].message.content.strip()