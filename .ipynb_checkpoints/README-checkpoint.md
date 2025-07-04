# RAG-based PDF Chatbot (Streamlit + FAISS)

## Overview
This project implements a lightweight Retrieval-Augmented Generation (RAG) chatbot that can answer questions from a large PDF document (10k+ words). It uses:

-  Sentence-aware chunking
-  Pretrained embedding model (MiniLM)
-  FAISS for fast similarity search
-  Streamlit interface with real-time responses via Ollama

The chatbot processes a training document, retrieves relevant content using vector similarity, and answers queries using a small language model.

## Folder Structure

rag_chatbot/
├── app.py                   # Streamlit chatbot app
├── requirements.txt
├── README.md
├── data/                    # Raw input documents (PDFs)
│   └── AI_Training_Document.pdf
├── chunks/                  # Saved text chunks
│   └── chunks.json
├── vectordb/                # FAISS index file
│   └── faiss.index
├── notebooks/               # Preprocessing,rough work and embedding notebook
│   └── prepare_chunks_faiss.ipynb
├── screenshots/             # Output screenshots 

## Architecture and Flow

1. **PDF Preprocessing**  
   - Extracted text from the PDF using `pdfplumber`
   - Cleaned the text (removed URLs, whitespace, headers/footers)
   - Performed sentence-aware chunking (300 words per chunk) using `RecursiveCharacterTextSplitter`

2. **Embedding and Vector Indexing**  
   - Used the `all-MiniLM-L6-v2` model from `sentence-transformers` to generate 384-dimensional embeddings
   - Stored the chunk embeddings in a FAISS index (`IndexFlatL2`) for fast similarity search

3. **Retrieval-Augmented Generation (RAG)**  
   - Encoded the user query at runtime using the same embedding model
   - Retrieved top-k similar chunks using FAISS
   - Constructed a context-aware prompt combining retrieved chunks and user query

4. **Language Model Response**  
   - Passed the final prompt to a small language model (`phi-3-mini` via Ollama) for generation
   - Displayed the response in a Streamlit UI


## How to Run the Project

### 1. Install Dependencies

Create a virtual environment , then run:
pip install -r requirements.txt

### 2. Generate Chunks and FAISS Index (Preprocessing)

Run the preprocessing notebook:
processing_and_chunking.ipynb and faiss_chunks_preparation.ipynb

This will:
- Extract text from the PDF
- Clean and chunk the text
- Embed chunks
- Save outputs to `chunks/chunks.json` and `vectordb/faiss.index`

### 3. Launch the Streamlit Chatbot

Run this from the project root:
streamlit run app.py

Make sure:
- Ollama is installed and running(ollama serve in cmd)
- Your chosen model (e.g., `phi3:mini` or `mistral`) is available and pulled in Ollama

## Model and Embedding Choices

### Embedding Model

- **Model Used**: all-MiniLM-L6-v2 from `sentence-transformers`
- **Reason**: Lightweight (384-dim), fast, and effective for semantic similarity

### Language Model (LLM)

- **Model Used**: `phi3:mini` (via Ollama)
- **Reason**: Small, fast, open-source language model suitable for local inference
- **Use**: Generates the final response based on the retrieved context and user prompt

## Screenshots

Below are sample outputs from the chatbot interface.

![Screenshot 1](screenshots/streamlitUi.png)
![Screenshot 2](screenshots/query1.png)
![Screenshot 3](screenshots/query2.png)
![Screenshot 4](screenshots/chat_history.png)

## Notes and Limitations

- The project is designed for local deployment using lightweight models and FAISS.
- Streaming responses are supported, but may be slow on limited hardware.
- A video demo was not included due to hardware constraints.
- Sample screenshots are provided in the `screenshots/` folder.
