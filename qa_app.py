from fastapi import FastAPI
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

app = FastAPI()

# initialize LLM
llm = OllamaLLM(model="phi3")

# using PromptTemplate library
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who explains things clearly and concisely. Always answer in 1-2 sentences unless the user asks for more detail."),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{question}")
])

# creating chain
chain = prompt | llm

# creating memory
memory_store = {}

def get_memory(session_id: str):
    # returns memory for a session. creates new memory if does not exist!
    if session_id not in memory_store:
        memory_store[session_id] = ChatMessageHistory()
    return memory_store[session_id]

# attach memory to chain
conversation = RunnableWithMessageHistory(
    chain,
    get_memory,
    input_messages_key="question",
    history_messages_key="history"
)

# API endpoint
@app.get("/ask")
async def ask(
    question: str,
    session_id: str = "default"
):
    response = conversation.invoke(
        {"question": question},
        config={"configurable": {"session_id": session_id}}
    )
    return{
        "question": question,
        "answer": response,
        "session_id": session_id,
    }

# add server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
