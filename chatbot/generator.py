import dotenv
from langchain_openai import ChatOpenAI
# from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.schema.runnable import RunnablePassthrough

BOOKS_CHROMA_PATH = "chroma_data/"

dotenv.load_dotenv()

review_template_str = """Your job is to answer questions based on given context. If you don't know an answer, say
you don't know.

{context}
"""

review_system_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["context"],
        template=review_template_str,
    )
)

review_human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["question"],
        template="{question}",
    )
)
messages = [review_system_prompt, review_human_prompt]

review_prompt_template = ChatPromptTemplate(
    input_variables=["context", "question"],
    messages=messages,
)

chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", model_name="gpt-3.5-turbo-0125", temperature=0)


reviews_vector_db = Chroma(
    persist_directory=BOOKS_CHROMA_PATH,
    embedding_function=OpenAIEmbeddings()
)

reviews_retriever = reviews_vector_db.as_retriever(k=10)


output_parser = StrOutputParser()


review_chain = (
    {
        "context": reviews_retriever,
        "question": RunnablePassthrough(),
    }
    | review_prompt_template
    | chat_model
    | output_parser
)

# context = "I had a great stay!"
# question = "Who are the cardiology specialists?"
# print(review_chain.invoke(question))