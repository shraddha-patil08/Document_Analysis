# Intelligent Document Analysis

The main objective of this project is to create a document analysis application where users can upload different document types (PDF, DOCX, TXT) and extract key insights, summaries, and answers to questions from the content of documents. The application is powered by advanced NLP models for text summarization, entity recognition, and document comparison.

## 🏗️ Project Structure
```
├── main.py                    # Main execution file
├── text_extraction.py         # extrct text from the file uploaded
├── summarization              # summarize the text from file
├── question_answering.py      # answer the questions based on content in file
├── comparision.py             # compare two files
```

### Key Features
- **Text Extraction** (`text_extraction.py`): Extracts text from documents.
- **Summarization** (`summarization.py`): Generates concise summaries of text.
- **Question Answering** (`question_answering.py`): Answers questions based on provided text.
- **Comparison** (`comparison.py`): Compares different text inputs.
- **Main Script** (`main.py`): Runs the entire pipeline.

## Implementation Workflow
1.	User uploads a document.
2.	System detects the file format and extracts text accordingly.
3.	Extracted text is displayed with a metadata summary.
4.	User selects an action (Summarization, Q&A, Insights, Comparison).
5.	NLP models process the text and generate output.
6.	Results are displayed in a structured format

## 🚀 Workflow
1. Add your API ID in the `.env` file.
2. Execute `main.py` to see the result.


## 📌 Note
- Ensure you have the necessary API keys in the `.env` file before running the scripts.

---
## 📄 License
Intelligent Document Analysis is released under the [MIT License](LICENSE), allowing you to freely use, modify, and distribute the project.
