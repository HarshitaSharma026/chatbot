from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain_core.messages import HumanMessage, AIMessage
import os
load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

llm = ChatGoogleGenerativeAI(model="gemini-pro")

# if we invoke out chat model, output will be an AIMessage
result = llm.invoke(
    [
        HumanMessage(
            content="Translate this sentence from English to French: I love programming."
        ),
        AIMessage(content="J'adore la programmation."),
        HumanMessage(content="What did you just say?"),
        AIMessage(content="Je viens de dire J'adore la programmation en français, ce qui signifie I love programming  en anglais."),
        HumanMessage(content="Tell everything in english. I don't understand a word")
    ]
)
print(result.content)





