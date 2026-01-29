import numpy as np
from app.vector_store import index

def retrieve(query_embedding, chunks, top_k=5):
    D, I = index.search(np.array([query_embedding]), top_k)
    return [chunks[i] for i in I[0]]
