from langchain_community.llms import Ollama
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os


load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

# giving instrcution to llm
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to user query"),
        ("user", "Question: {question}")
    ]
)

# designing ui using streamlit
st.title("Chatbot Basic Prototype")
input_text = st.text_input("Ask me anything...")

# setting up llm and output
llm = Ollama(model="llama2")
output_parse = StrOutputParser()

# chaining
chain = prompt|llm|output_parse

if input_text:
    st.write(chain.invoke({'question': input_text}))
