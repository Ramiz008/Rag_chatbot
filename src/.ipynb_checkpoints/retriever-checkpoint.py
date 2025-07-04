
def retrieve_top_chunks(user_query,emd_model,index,chunks,k=3):
    import faiss 
    query_vec =emd_model.encode([user_query])
    distance,indices = index.search(query_vec,k)
    top_chunks = []
    for i in indices[0]:
        top_chunks.append(chunks[i])
    return top_chunks