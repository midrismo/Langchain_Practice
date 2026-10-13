import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that explains things simply."),
    ("human", "{topic}"),
])

chain = prompt | model
response = chain.invoke({"topic": "What is LangSmith?" "What is gold rate today in Saudi" "What is the weather in chennai?"})
print(response.content)