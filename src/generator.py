def generate_response(top_chunks,user_query,model_name="phi3:mini"):
    import ollama
    context="\n".join(top_chunks)
    final_prompt= f"based on following context:\n{context}\nanswer the following questions:\n{user_query}"
    
    response = ollama.chat(
    model=model_name, #model
    messages=[{'role': 'user', 'content': final_prompt}],
    stream=True)
    for chunk in response:
        print(chunk)
        yield chunk["message"]["content"]