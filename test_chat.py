# test_chat.py
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Point to Grok's API instead of OpenAI
llm = ChatOpenAI(
    model="grok-3",
    api_key=os.getenv("GROK_API_KEY"),
    base_url="https://api.x.ai/v1",   # ← This is the only difference!
    temperature=0.7
)

response = llm.invoke("Hello! Who are you?")
print(response.content)