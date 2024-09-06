# creating a simple q/a system. (asking just one question)

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
# loading env variable
load_dotenv()

# creating model 
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# creating messages 
messages = [
    SystemMessage(content="You are going to solve a math problem"),
    HumanMessage(content="what is 81 * 9?")
]

# invoking the chat model
result = model.invoke(messages)
print(f'Full result: {result}')
print("Output: ")
print(result.content)