# 🤖 Simple AI Chatbot

A beginner-friendly chatbot built with **LangChain** and the **OpenAI API**. Ask it anything — it uses GPT-3.5-turbo under the hood to give you real, conversational answers.

---

## 📖 What This Does

This script sends a list of questions to OpenAI's chat model through LangChain and prints the answers to your terminal. It's a great starting point for understanding how LLM-powered apps are structured.

---

## 🗂️ Project Structure

```
langchain-chatbot/
├── chatbot.py       # Main chatbot script
├── .env             # Your API key (never shared/committed)
├── .gitignore       # Keeps .env and env/ out of Git
└── env/             # Virtual environment (not committed)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/langchain-chatbot.git
cd langchain-chatbot
```

### 2. Create and activate a virtual environment
```bash
python -m venv env

# Windows
env\Scripts\activate

# Mac/Linux
source env/bin/activate
```

### 3. Install the dependencies
```bash
pip install langchain langchain-openai langchain-core python-dotenv openai
```

### 4. Set up your API key
Create a `.env` file in the root of the project and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

> ⚠️ Never commit your `.env` file. It's already listed in `.gitignore` to keep it safe.

You can get your API key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys). A small amount of billing credit is required (a few dollars is enough to get started).

---

## ▶️ Running the Chatbot

```bash
python chatbot.py
```

You should see output like this:

```
==================================================
         LANGCHAIN CHATBOT - TEST RUN
==================================================

Q1: What is the capital of France?
A1: The capital of France is Paris.
--------------------------------------------------

Q2: Explain gravity in simple terms.
A2: Gravity is a force that pulls objects toward each other...
--------------------------------------------------
```

---

## 🧪 Sample Queries Tested

1. What is the capital of France?
2. Explain gravity in simple terms.
3. What is 15% of 200?
4. Give me 3 tips for better sleep.
5. What is the difference between a list and a tuple in Python?

---

## 🛠️ Built With

- [LangChain](https://www.langchain.com/) — Framework for building LLM-powered apps
- [OpenAI API](https://platform.openai.com/) — GPT-3.5-turbo as the language model
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Loads environment variables from `.env`

---

## 💡 Things to Try

- Change `temperature=0.7` to `0.0` for more precise answers
- Edit the `SystemMessage` to give the bot a different personality
- Add your own questions to the `questions` list

---

## 👤 Author

Made by **Abdoul Abbas** — learning AI development one project at a time.

---


