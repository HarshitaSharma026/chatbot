from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnableParallel
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

messages = [
    ("system", "You are an expert product reviewer."),
    ("human", "List down the features of the {product_name}"),
]
prompt_template = ChatPromptTemplate.from_messages(messages)

# defining pros anaysis step
def analyze_pros(features):
    pros_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            ("human", "Given these features: {features}, list down pros of the product."),
        ]
    )
    return pros_template.format_prompt(features = features)

# defining cons analysis step
def analyze_cons(features):
    pros_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            ("human", "Given these features: {features}, list down cons of the product."),
        ]
    )
    return cons_template.format_prompt(features = features)

# combine pros and cons into final review
def combine_pros_cons(pros, cons):
    return f"Pros:\n {pros}\n\n Cons:\n {cons}"

# simplify branches
pros_branch_chain = (
    RunnableLambda(lambda x : analyze_pros(x) | model | StrOutputParser())
)

cons_branch_chain = (
    RunnableLambda(lambda x : analyze_cons(x) | model | StrOutputParser())
)

chain = (
    prompt_template
    | model
    | StrOutputParser()
    | RunnableParallel(branches={"pros": pros_branch_chain, "cons": cons_branch_chain})
    | RunnableLambda(lambda x : combine_pros_cons(x["branches"]["pros"], x["branches"]["cons"]))
)

# here RunnableLambda(lambda x : combine_pros_cons(x["branches"]["pros"], x["branhes"]["cons"])): we are getting a dictionary, in which pros and cons are other dictionary
# running the chain
response = chain.invoke({"product_name": "Macbook Air"})

print(response)

# NOT WORKING PROPERLY - ERROR !!