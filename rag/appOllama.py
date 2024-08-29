import streamlit as st
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.documents import Document

load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

# -------------------- EXTRACTING TEXT FROM PDF
def get_md_text(doc_path):
    text = ""
    loader = UnstructuredMarkdownLoader(doc_path)
    data = loader.load()

    for doc in data:
        text += doc.page_content
    return text

# --------------------- CREATING CHUNKS OF THE PDF TEXT
def get_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

# -------------------- TIME TO CONVERT TEXT INTO VECTORS - embedding
def get_vector_store(chunks):
    embeddings = OllamaEmbeddings(model="llama2")

    # creating vector store using FAISS
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)

    # # save the vector store locally 
    # vector_store.save_local("faiss_index")
    return vector_store

# -------------------- DEVELOPING Q/A CHAIN, prompt,model,output
def get_chain():
    prompt_template = """Answer the question as detailed as possible from the provided context, make sure to provide all the details,
    if the answer is not in the provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:{context}\n
    Question:{question}\n

    Answer:"""

    model = Ollama(model="llama2")
    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain = load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)
    return chain

# ------------------- TAKE USER INPUT
def user_input(user_question, db_vectors):
    docs = db_vectors.similarity_search(user_question)

    # obtain conversational question-answering chain
    chain = get_chain()

    # use the conversational chain to get a response based on the user question and retrieved documents
    response = chain(
        {"input_documents": docs, "question": user_question}, return_only_outputs=True
    )
    # print the response to the console
    print(response)

    # display the response in streamlit app
    st.write("Answer: ", response["output_text"])

def main():
    st.set_page_config("RAG Q/A chatbot")
    st.header("Chat with PDF")

    user_question = st.text_input("Ask a question")

    markdown_path = "/Users/harshitawork/Desktop/chatbot/pdfParser/academic_calender.md"
    raw_text = get_md_text(markdown_path)
    text_chunks = get_chunks(raw_text)
    get_vectors = get_vector_store(text_chunks)

    if user_question:
        user_input(user_question, get_vectors)

    


if __name__ == "__main__":
    main()
    
