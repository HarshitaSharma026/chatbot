from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import os 
import user_agent as us

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)

# --------------- loading the document
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
data = loader.load()
# print(data)

# --------------- converting text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)


# -------------- convert chunks to vectors
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = FAISS.from_documents(documents=all_splits, embedding=embedding)

# ------------- retrieving appropriate embeddings
retriever = vectorstore.as_retriever(k = 4)
docs = retriever.invoke("how can langsmith help with testing?")
docs

# --------------- creating prompt
qa_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer the user's questions based on the below context:\n\n{context}"
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)
doc_chain = create_stuff_documents_chain(model, qa_prompt)


# --------------- retrieving these documents
history = ChatMessageHistory()
history.add_user_message("how can langsmith help with testing?")
result = doc_chain.invoke(
    {
        "messages": history.messages,
        "context": docs
    }
)

print(result)

