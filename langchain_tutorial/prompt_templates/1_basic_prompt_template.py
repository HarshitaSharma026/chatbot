from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage


# 1. Prompt with single value
# template = "Tell me a joke about {topic}"
# prompt_template = ChatPromptTemplate.from_template(template)

# print("----- Prompt from template ------")
# prompt = prompt_template.invoke({"topic":"cats"})      # we give value to these variables in the form of a dictionary
# print(prompt)

# 2. Prompt with multiple value
# template_multiple = """You are a helpful assistant.
# Human: Tell me a {adjective} story about a {animal}
# Assistant: """
# prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
# prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "panda"})
# print(prompt)

# 3. Prompt with sytem and human messages
# when we want to do string interpolation: {topic}, we have to use tuples and we can't use HumanMessage(content="Tell me {jokes_count} on it"), this won't work
# it'll simply display the string as it is: Tell me {jokes_count} on it"
messages = [
    ("system", "You are a comedian who tells jokes about {topic}"),
    ("human", "Tell me {jokes_count} jokes on it. ")
]
prompt = ChatPromptTemplate.from_template(messages)
result = prompt.invoke({"topic": "lawyers", "jokes_count":3})
print(result)

# 4. This won't work
messages2 = [
    ("system", "You are a comedian who tells jokes about {topic}"),
    HumanMessage(content="Tell me {jokes_count} jokes on it.")       # this won't work, either use tuples, or directly give the value
]
prompt2 = ChatPromptTemplate(messages2)
result2 = prompt2.invoke({"topic": "lawyers", "jokes_count":3})
print(result2)