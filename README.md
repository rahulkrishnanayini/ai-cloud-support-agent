# 🚀 AI Cloud Support Agent

## 📌 Overview

This project is a **Retrieval Augmented Generation (RAG) based AI agent** designed to troubleshoot cloud and networking issues.

It uses a **vector database (FAISS)** to retrieve relevant knowledge and combines it with an **LLM (Flan-T5)** to generate intelligent responses.

---

## 🔥 Features

* ✅ RAG (Retrieval Augmented Generation)
* ✅ FAISS Vector Database (semantic search)
* ✅ Multi-Agent System (Analyzer + Retriever + Executor)
* ✅ Tool-based troubleshooting suggestions
* ✅ Works with custom data (text/PDF)

---

## 🧠 How It Works

1. Load knowledge base (`data.txt`)
2. Split into chunks
3. Convert text → embeddings
4. Store in FAISS vector database
5. Retrieve relevant context
6. Generate answer using LLM
7. Suggest fix using tool logic

---

## 🛠️ Tech Stack

* Python
* LangChain
* FAISS
* HuggingFace Transformers
* Sentence Transformers

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py
```

---

## 💡 Example Queries

* VM not connecting
* DNS not resolving
* High CPU usage
* Firewall blocking application
* VPN connection issue

---

## 📊 Sample Output

* AI Explanation of issue
* Retrieved context (RAG)
* Suggested fix

---

## 🎯 Use Case

* Cloud troubleshooting assistant
* Networking issue diagnosis
* Learning RAG + AI Agents
* Interview project (AI/Cloud roles)

---

## 🚀 Future Improvements

* Streamlit UI (ChatGPT-like interface)
* PDF upload support
* Better LLM integration
* Real-time logs & monitoring

---
## 📸 Demo Output

![Output](Screenshot 2026-04-01 143801.png,
Screenshot 2026-04-01 143812,
Screenshot 2026-04-01 143825)


## 👤 Author

Rahul
