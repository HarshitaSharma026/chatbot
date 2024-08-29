from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.chat_message_histories import ChatMessageHistory
import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro", convert_system_message_to_human=True)

history = ChatMessageHistory()
history.add_user_message("Hi")
history.add_ai_message("whats up?")
print(history.messages)
history.add_user_message("Translate this sentence from English to French: I love programming.")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
chain = prompt | llm

result = chain.invoke({
    "messages": history.messages
})

history.add_ai_message(result)

history.add_user_message("What did you just say?")

response = chain.invoke({"messages": history.messages})
print(response.content)