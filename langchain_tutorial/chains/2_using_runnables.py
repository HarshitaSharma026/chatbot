from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

messages = [
    ("system", "You are a comedian who tells jokes about {topic}"),
    ("human", "Tell me {jokes_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)

# creating runnables
format_prompt = RunnableLambda(lambda x : prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

chain = RunnableSequence(first=format_prompt, middle = [invoke_model], last=parse_output)

# running the chain
response = chain.invoke({"topic": "lawyers", "jokes_count": 3})

print(response)