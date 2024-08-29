from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import os 


# -------------------- LOADING FROM WEBPAGE
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["USER_AGENT"]=os.getenv("USER_AGENT")


# loading the web source from where we want out data 
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
data = loader.load()
# print(data)

# converting text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)
# print(all_splits)

# converting into embeddings and storing it in vector stores
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = FAISS.from_documents(documents=all_splits, embedding=embedding)

# creating a retriver
retriever = vectorstore.as_retriever(k = 4)
docs = retriever.invoke("how can langsmith help with testing?")
print(docs)

