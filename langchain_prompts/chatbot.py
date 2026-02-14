from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

chat_history = [
    SystemMessage(content="You are a helpful assistant that provides concise and accurate answers to user questions.")
]

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

while True :
    user_input = input("Enter your question (or 'exit' to quit): ")
    if(user_input.lower() == "exit" or user_input.lower() == "quit"):
        print("Exiting the chatbot. Goodbye!")
        break
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Chatbot response:", result.content)  

print(type(chat_history))
print(chat_history)
