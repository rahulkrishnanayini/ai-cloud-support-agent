from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

# Load data
loader = TextLoader("data.txt")
documents = loader.load()

# Split
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Embeddings + FAISS
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_documents(docs, embeddings)
retriever = db.as_retriever(search_kwargs={"k": 2})

# LLM
pipe = pipeline("text-generation", model="google/flan-t5-base", max_length=200)

def llm(query):
    return pipe(query)[0]['generated_text']

# RAG
def rag_answer(query):
    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a cloud support engineer.

Explain the issue and suggest fix.

Context:
{context}

Question: {query}

Answer:
"""
    answer = llm(prompt)
    return answer, context

# Tool
def troubleshoot_tool(query):
    query = query.lower()
    if "network" in query:
        return "Check NSG, firewall, IP config."
    elif "dns" in query:
        return "Check DNS server and resolution."
    else:
        return "Check logs and restart services."

# Agent
def main_agent(query):
    answer, context = rag_answer(query)
    tool = troubleshoot_tool(query)

    return f"""
AI Explanation:
{answer}

Context:
{context}

Fix:
{tool}
"""

# Test
if __name__ == "__main__":
    while True:
        q = input("Enter query: ")
        print(main_agent(q))