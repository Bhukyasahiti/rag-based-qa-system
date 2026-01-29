import faiss
import numpy as np

DIM = 384
index = faiss.IndexFlatL2(DIM)

def add_embeddings(embeddings):
    index.add(np.array(embeddings))
