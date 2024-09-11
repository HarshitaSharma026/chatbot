# Chatbot Docs

Main components of a llm-powered chatbot
1. Chat models - prefered beacuse they work around messages and not just plain text, also it has more conversational tone and natively supports a message interface
2. PromptTemplate
3. Chat history
4. Retrievers - which are useful if you want to build a chatbot that can use domain-specific, up-to-date knowledge as context to augment its responses.


### HumanMessage
HumanMessages are messages that are passed in from a human to the model.
HumanMessage(content="string to be passed as a message")

### AIMessage
AIMessage is returned from a chat model as a response to a prompt.

### ChatPromptTemplate
This is a prompt template for chatmodel. Here we specify what we want our chat model to do.
Each chat message is associated with content, and an additional parameter called role.

### ChatPromptTemplate.from_messages 
static method accepts a variety of message representations and is a convenient way to format input to chat models with exactly the messages you want.
Tuple representation : (type, content)

### MessagePlaceholder
A placeholder which can be used to pass in a list of messages.

### ChatMessageHistory
wrapper that provides convenience methods for saving HumanMessages, AIMessages, and other chat messages and then fetching them.

### RecursiveCharacterTextSplitter
utility designed to break down large blocks of text into smaller, manageable chunks while preserving meaning and coherence as much as possible. It does this by recursively attempting to split the text using different types of delimiters (like paragraphs, sentences, and words), starting with broader splits and narrowing down as needed.

### create_stuff_documents_chain
Create a chain for passing a list of Documents to a model.

### temperature 
is a measure of the amount of randomness the model uses to generate responses.

### StrOutputParser()
Parses the result into a string, (just like how result.content will print)


## ERRORS I ENCOUNTERED

#### USER_AGENT environment variable not set
- got this while trying to get the website using WebBaseLoader() (basically while scraping a website)
- User-agent is a key component of the header that is being sent along with the HTTP request. It contains important information that will be used by the server to frame the responses.
- reason:
    - When you try to scrape a website using WebBaseLoader(), the website likely detected that the request came from a bot or an unidentified source. Websites often block such requests to prevent automated scraping.
- solution: found on this blog : https://www.zenrows.com/blog/python-requests-user-agent#what-is
