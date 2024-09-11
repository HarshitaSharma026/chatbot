from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate

# loading env variable
load_dotenv()

# creating model =
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 1. Prompt with single value
print("--------- Prompt template for single value -----------")
template = "Tell me a joke about {topic}"
prompt_template = ChatPromptTemplate.from_template(template)
prompt = prompt_template.invoke({"topic":"cats"})      # we give value to these variables in the form of a dictionary
result = model.invoke(prompt)
print(result.content)



# 2. Prompt with multiple value
print("--------- Prompt template with multiple values -----------")
template_multiple = """You are a helpful assistant.
Human: Tell me a {adjective} story about a {animal}
Assistant: """
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "panda"})
result_multiple = model.invoke(prompt)
print(result_multiple.content)

# 3. Prompt with sytem and human messages
# when we want to do string interpolation: {topic}, we have to use tuples and we can't use HumanMessage(content="Tell me {jokes_count} on it"), this won't work
# it'll simply display the string as it is: Tell me {jokes_count} on it"
print("--------- Prompt template with system and human -----------")
messages = [
    ("system", "You are a comedian who tells jokes about {topic}"),
    ("human", "Tell me {jokes_count} jokes on it. ")
]
prompt_system = ChatPromptTemplate(messages)
prompt1 = prompt_system.invoke({"topic": "lawyers", "jokes_count":3})
result_system = model.invoke(prompt1)
print(result_system.content)
