#!/usr/bin/env python
# coding: utf-8

# In[1]:


from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="phi3")

response = llm.invoke("What is the difference between Ollama and OllamaLLM?")
print(response)


# In[ ]:




