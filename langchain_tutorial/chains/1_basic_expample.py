from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

messages = [
    ("system", "You are a comedian who tells jokes about {topic}"),
    ("human", "Tell me {jokes_count} jokes on it. ")
]
prompt = ChatPromptTemplate.from_messages(messages)

chain = prompt | model | StrOutputParser()
result = chain.invoke({"topic":"lawyers", "jokes_count":3})
print(result)