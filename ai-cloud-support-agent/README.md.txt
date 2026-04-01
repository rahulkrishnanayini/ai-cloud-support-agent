# AI Cloud Support Agent 🚀

## Overview
This project is a RAG-based AI agent that helps troubleshoot cloud and networking issues.

## Features
- Retrieval Augmented Generation (RAG)
- FAISS Vector Database
- Multi-Agent Architecture
- Tool-based troubleshooting

## Tech Stack
- Python
- LangChain
- FAISS
- HuggingFace Transformers

## How it works
1. Loads knowledge base (data.txt)
2. Converts to embeddings
3. Stores in FAISS
4. Retrieves relevant context
5. Generates answer using LLM
6. Suggests fix using tools

## Run locally
```bash
pip install -r requirements.txt
python app.py