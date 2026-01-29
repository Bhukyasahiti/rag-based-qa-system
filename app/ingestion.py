from app.chunking import chunk_text
from app.embeddings import embed_text
from app.vector_store import add_embeddings

documents = {}

def process_document(document_id, text):
    chunks = chunk_text(text)
    embeddings = embed_text(chunks)
    add_embeddings(embeddings)
    documents[document_id] = chunks
