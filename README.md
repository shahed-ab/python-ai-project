# 🤖 Personal AI Assistant with Memory

A personal AI assistant built with **Python**, **LangChain**, and **Grok API** that remembers your conversations and responds like a real assistant.

---

## ✨ Features

- 💬 Chat with an AI assistant in natural language
- 🧠 Short-term memory — remembers the full current conversation
- 🔑 Powered by **Grok API** (free trial credits)
- ⚡ Built with **LangChain** for easy AI pipeline management
- 🔒 Secure — API keys stored safely in `.env` file

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.9+ | Core programming language |
| LangChain | AI pipeline & memory management |
| Grok API (xAI) | Free LLM (Language Model) |
| python-dotenv | Secure API key management |

---

## 📁 Project Structure

```
python-ai-project/
├── main.py              ← Main assistant with memory & persona
├── test_chat.py         ← Simple test to check Grok API connection
├── .env                 ← API keys (NOT uploaded to GitHub)
├── .gitignore           ← Hides .env and other sensitive files
├── requirements.txt     ← All project dependencies
└── README.md            ← You are here!
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/python-ai-project.git
cd python-ai-project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Activate it:
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Your API Key

- Go to [console.x.ai](https://console.x.ai) and get your **Grok API key**
- Create a `.env` file in the project root:

```
GROK_API_KEY=your_grok_api_key_here
```

### 5. Run the Assistant

```bash
python main.py
```

---

## 💬 Example Conversation

```
You: Hi! My name is Rahul
Assistant: Hello Rahul! Great to meet you. How can I help you today?

You: What is my name?
Assistant: Your name is Rahul! You told me at the start of our conversation. 😊

You: Explain what Python is
Assistant: Python is a beginner-friendly, high-level programming language known
for its simple syntax and versatility...
```

---

## 🔐 Security Note

> ⚠️ **Never share your `.env` file or API key publicly.**
> The `.gitignore` file ensures your `.env` is never uploaded to GitHub.

---

## 📦 Dependencies

```
langchain
langchain-openai
langchain-community
python-dotenv
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🗺️ Roadmap / Future Features

- [ ] Add Streamlit web UI (chat interface in browser)
- [ ] Add long-term memory using a vector database
- [ ] Support file uploads (PDF Q&A)
- [ ] Deploy online so anyone can access it

---

## 🙋‍♂️ Author

**Shahed**
- GitHub: [@shahed-ab](https://github.com/shahed-ab)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
