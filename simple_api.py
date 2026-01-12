from fastapi import FastAPI
from langchain_ollama import OllamaLLM

app = FastAPI()
llm = OllamaLLM(model="phi3")

@app.get("/ask")
async def ask(question: str):
    response = llm.invoke(question)
    return {"answer": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)