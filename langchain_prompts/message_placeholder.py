from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate([
    ("system","You are helpful customer support assistant that provides concise and accurate answers to user questions."),
    MessagesPlaceholder(variable_name = "chat_history"), # this will be used to load the chat history, we can use the same variable name as the one we will use to load the chat history
    ("human","{query}"), #but rn the ai does not know how to use the {query} variable, we need to add a placeholder for it
])

chat_history = []
# load chat history 
with open("chat_history.txt","r") as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "What is my refund?"
})

print(prompt)