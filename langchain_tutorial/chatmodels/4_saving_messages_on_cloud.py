# saving history on cloud - Google cloud + Firebase

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_firestore import FirestoreChatMessageHistory 
from google.cloud import firestore

load_dotenv()

PROJECT_ID = "langchain-tutorial-3e40b"
SESSION_ID = "user_session1"
COLLECTION_NAME = "chat_history"

# initializing firestore client
print("Initializing firestore client......")
client = firestore.Client(project=PROJECT_ID)

# Initilizing firestore chat message history
print("Initilizing firestore chat message history...")
chat_history = FirestoreChatMessageHistory(
    session_id = SESSION_ID,
    collection = COLLECTION_NAME,
    client = client,
)
print("Chat history initialized")
print("Current chat history: ", chat_history.messages)

# create model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

print("Start chatting with AI. Type exit to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break
    chat_history.add_user_message(human_input)
    
    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)
    print(f'AI: {ai_response.content}')


