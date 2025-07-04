import streamlit as st
from src.pipeline import load_pipeline, run_rag_pipeline

# setting page title
st.set_page_config(page_title="Chat Screen",layout="wide")

# app title
st.title("RAG-Powered Chatbot")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()
# Load embedding model, FAISS index, and chunks
emb_model, index, chunks = load_pipeline()
    
with st.sidebar:
    st.markdown("##  Info Panel")
    st.markdown(f"** Model in use:** Phi:3 mini by Microsoft")
    st.markdown(f"** Total Chunks Indexed:** `{len(chunks)}`")
#text input box
user_input =st.text_input("Ask your query")
    
#submit button
if st.button("submit") and user_input:
    
    # Run full pipeline
    answer, top_chunks = run_rag_pipeline(user_input, emb_model, index, chunks)

    # Save to session history
    st.session_state.chat_history.append(
    {"question": user_input, "answer": answer})
    # Show model answer
    st.markdown("###  Model Answer:")
    st.markdown(answer)
    
    # Show chat history
    st.markdown("##  Chat History")
    for item in st.session_state.chat_history:
        st.markdown(f"**You:** {item['question']}")
        st.markdown(f"**Bot:** {item['answer']}")