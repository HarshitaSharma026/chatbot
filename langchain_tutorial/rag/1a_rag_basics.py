"""
In this tutorial, a basic rag example is created in which, a text file is converted into embeddings and store in a vector database (vector store) locally. 
"""

import os 

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# define the directory containing text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "os.txt")
persistent_directory = os.path.join(current_dir, "db","chroma_db_os")

# check if chroma vector store already exists, if it does no need to create it again
if not os.path.exists(persistent_directory):
    print("Persisten directory does not exist. Initializing vector store....")

    # ensure the text file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please check the path."
        )

    # read the text content from the file. 
    loader = TextLoader(file_path)
    documents = loader.load()

    # split documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # display info about split document
    print("\n ---- document chunks information ----")
    print(f"Number of document chunks: {len(docs)}")
    print(f"Sample chunk: \n {docs[0].page_content}\n")

    # create embeddings 
    print("\n ---- Creating embeddings ----")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    print("\n ---- Finished creating embeddings ----")

    # create vector store and persist it automatically
    print("\n ---- Creating vector store ----")
    db = Chroma.from_documents(
        docs, embeddings, persist_directory=persistent_directory
    )
    print("\n ---- Finished creating vector stores ----")
else:
    print("Vector store already exists. No need to initialize it. ")
