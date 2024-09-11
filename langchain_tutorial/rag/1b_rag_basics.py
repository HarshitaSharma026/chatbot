"""
In this program, the basic rag is taken forward to get the relevant documents (that matched well with the user query) from already created vector stores . 
"""

import os 
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"


# define the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_dir, "books", "os.txt")
persistent_directory = os.path.join(current_dir, "db","chroma_db_os")

# define embedding model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# load the existing vector store with the embedding function
db = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embeddings)

# defining user question
query = "What are device drivers?"

# retrieve relevant documents based on the query
retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k":10, "score_threshold":0.9},
)
relevant_docs = retriever.invoke(query)

# IMP POINT ********
# while building rag documents, if we are not getting results even after everything is working fine, it means we are getting too strict in retrieving the relevant documents 

# display documents relevant to the query
print("\n --- Relevant documents --- ")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}: \n{doc.page_content}")
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")