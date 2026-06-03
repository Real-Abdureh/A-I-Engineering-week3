from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

#Load the API key from the .env file
load_dotenv()


#Setup the Model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

#System Message gives the chatbot it's personality
system_msg = SystemMessage(content="You are a helpful assistant ")

def chat(user_input):
    human_msg = HumanMessage(content=user_input)
    response = llm.invoke([system_msg, human_msg])
    return response.content

# 5 sample queries to test the chatbot

questions = [
    "What is the capital of France?",
    "Can you explain the theory of relativity in simple terms?",
    "What are the benefits of regular exercise?",
    "How does photosynthesis work?",
    "What is the meaning of life?"
]

print("=" * 50)
print("              LANGCHAIN CHATBOT - TEST RUN")
print("=" * 50)

for i, question in enumerate(questions, 1):
    print(f"\nQ{i}: {question}")
    print(f"A{i}: {chat(question)}")
    print("-" * 50)
