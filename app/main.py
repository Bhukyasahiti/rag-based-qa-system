from fastapi import FastAPI, UploadFile, BackgroundTasks
from app.schemas import QueryRequest
from app.ingestion import process_document, documents
from app.embeddings import embed_text
from app.retrieval import retrieve
from app.llm import generate_answer
import uuid

app = FastAPI()


@app.post("/upload")
async def upload_document(file: UploadFile, background_tasks: BackgroundTasks):
    text = (await file.read()).decode("utf-8")
    document_id = str(uuid.uuid4())
    background_tasks.add_task(process_document, document_id, text)
    return {"message": "Document ingestion started", "document_id": document_id}


@app.post("/query")
def query_document(request: QueryRequest):
    chunks = documents.get(request.document_id)

    if not chunks:
        return {"error": "Document not found or still processing"}

    query_embedding = embed_text([request.question])[0]
    relevant_chunks = retrieve(query_embedding, chunks)
    context = "\n".join(relevant_chunks)
    answer = generate_answer(context, request.question)

    return {"answer": answer}
