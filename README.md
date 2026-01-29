# rag-based-qa-system
# RAG-Based Question Answering System

## Objective
Build an API that allows users to upload documents and ask
questions using a Retrieval-Augmented Generation (RAG) approach.

## Architecture Overview
The system ingests documents asynchronously, chunks text,
generates embeddings, stores them in FAISS, retrieves relevant
chunks, and generates answers.

![Architecture](architecture.png)

## Chunking Strategy

**Chunk size chosen:** 500 tokens  
**Overlap:** 100 tokens

This chunk size was selected to balance semantic coherence and
retrieval accuracy. Smaller chunks improve recall but often lose
context, while very large chunks reduce retrieval precision.
A size of 500 tokens preserves paragraph-level meaning and fits
comfortably within LLM context limits. The overlap prevents loss
of information at chunk boundaries.



## Retrieval Failure Case

A retrieval failure was observed when asking high-level conceptual
questions such as “What is the motivation behind the algorithm?”
In such cases, the retriever returned implementation-focused chunks
instead of conceptual explanations.

This happened because embedding similarity favors technical terms
and keyword-rich sections. This issue can be improved by increasing
the top-k retrieval size or combining keyword-based (BM25) and
embedding-based retrieval.


## Metric Tracked
## Metric Tracked

**Metric:** End-to-end query latency

Latency was tracked to measure user-perceived performance.
On average:
- Query embedding took ~20 ms
- FAISS similarity search took ~5 ms
- LLM response generation took ~900 ms

Tracking latency helped identify that the LLM was the primary
bottleneck in the system.


## API Endpoints
POST /upload – Upload PDF or TXT  
POST /query – Ask question from uploaded document

## Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
