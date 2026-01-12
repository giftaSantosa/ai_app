# 🚀 AI Q&A API with FastAPI & Ollama

Here’s my **first attempt at building an AI chatbot**! 🤖  
This project combines **FastAPI**, **LangChain**, and **Ollama LLM** to create a **context-aware Q&A API** — basically a mini AI assistant you can chat with.  

---

## 💡 Concepts Learned

- 🧠 Creating a chatbot using `OllamaLLM`  
- 🔗 Using **LangChain** to manage memory and interactive conversation  
- 💻 Generating an API with **FastAPI** and **Uvicorn**  
- 📝 Maintaining conversation memory with `ChatMessageHistory`  

---

## ⚡ Getting Started

**Requirements:**  
- Python 3.9 or 3.10  
- Install dependencies:  
```bash
pip install fastapi uvicorn langchain-ollama
```
- Run locally:  
```bash
python3 qa_app.py
```
- Test the API
```bash
  curl "http://localhost:8000/ask?question=What+is+AI?&session_id=test123"
```
- Sample JSON response
```JSON
  {
  "question": "What is AI?",
  "answer": "Artificial Intelligence is ...",
  "session_id": "test123"
  }
```
