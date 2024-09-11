from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableSequence
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

messages = [
    ("system", "You are a comedian who tells jokes about {topic}"),
    ("human", "Tell me {jokes_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)

upper_case = RunnableLambda(lambda x : x.upper())
word_count = RunnableLambda(lambda x : f"Word Count: {len(x.split())} \n {x}")

chain = prompt_template | model | StrOutputParser() | upper_case | word_count

# running the chain
response = chain.invoke({"topic": "lawyers", "jokes_count": 3})

print(response)