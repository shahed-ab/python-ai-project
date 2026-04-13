# main.py
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# Grok LLM setup
llm = ChatOpenAI(
    model="grok-3",
    api_key=os.getenv("GROK_API_KEY"),
    base_url="https://api.x.ai/v1",
    temperature=0.7
)

# Memory - remembers last 10 messages
memory = ConversationBufferWindowMemory(k=10)

# Custom persona
template = """You are a friendly personal AI assistant.
You remember everything from the conversation.
Keep answers short and clear.

Conversation history:
{history} """