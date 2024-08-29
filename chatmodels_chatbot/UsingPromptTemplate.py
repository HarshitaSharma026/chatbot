from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

import os
load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro", convert_system_message_to_human=True)

# creating prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
chain = prompt | llm

result = chain.invoke(
    {
        "messages": [
            HumanMessage(
                content="Translate this sentence from English to French: I love programming."),
            AIMessage(content="J'adore la programmation."),
            HumanMessage(content="What did you just say?"),
        ],
    }
)
print(result.content)
