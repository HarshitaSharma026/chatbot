# asking multiple questions - understanding how history is saved manually.


from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
# load env variable
load_dotenv()

# create model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# giving previous conversations to the model manually
messages = [
    SystemMessage(content="Solve the following maths problem"),
    HumanMessage(content="what is 81 * 9?"),
    AIMessage(content="81 * 9 = 729"),
    HumanMessage(content="Is 729 square of some number?if yes give me the number")
]

# invoke chat model
result = model.invoke(messages)
print(result.content)