from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# initialize model
llm = OllamaLLM(model="phi3")

# create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple terms, like you are talking to a junior developer."
)

# create a chain
chain = prompt | llm

# ask about different topics
topics = ["Cloud Computing", "Artificial Intelligence", "Machine Learning", "Deep Learning"]

for topic in topics:
    print(f"\nExplaining {topic}: ")
    print(chain.invoke(topic))