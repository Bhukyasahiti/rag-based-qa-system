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
Chunk size: 500 tokens  
Overlap: 100 tokens  

This size balances semantic context and retrieval accuracy.

## Retrieval Failure Case
High-level conceptual questions sometimes retrieve implementation
details due to embedding similarity bias.

## Metric Tracked
Metric: End-to-end query latency (~900ms)

## API Endpoints
POST /upload – Upload PDF or TXT  
POST /query – Ask question from uploaded document

## Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
