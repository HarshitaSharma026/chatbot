# Storing history locally in a list

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# load env variable
load_dotenv()

# create model 
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

chat_history = []        # a list to store messages

# setting initial system message (optional)
system_message = SystemMessage(content="You are an helpful AI assistant")
chat_history.append(system_message)

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    print("AI: ", result.content)
    chat_history.append(AIMessage(content=result.content))

print("---------- MESSAGE HISTORY----------")
print(chat_history)