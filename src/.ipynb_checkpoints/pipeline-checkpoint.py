from .retriever import retrieve_top_chunks
from .generator import generate_response


def load_pipeline(index_path="vectordb/faiss.index",chunks_path="chunks/chunks.json"):
    import json
    #loading the chunks 
    with open(chunks_path,"r") as r:
        chunks=json.load(r)

    #loading the index 
    import faiss
    index = faiss.read_index(index_path)

    #load the embedding model
    from sentence_transformers import SentenceTransformer
    emb_model = SentenceTransformer("all-MiniLM-L6-v2")

    return emb_model,index,chunks

def run_rag_pipeline(user_query, emb_model, index, chunks, model_name="phi3:mini"):
    from src.generator import generate_response
    from src.retriever import retrieve_top_chunks
    
    top_chunks = retrieve_top_chunks(user_query, emb_model, index, chunks)
    return generate_response(top_chunks, user_query, model_name)
    
    