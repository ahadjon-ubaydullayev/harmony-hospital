import dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

PDF_BOOK_PATH = "../data/harmony.pdf"
BOOK_CHROMA_PATH = "chroma_data"

dotenv.load_dotenv()

loader = loader = PyPDFLoader(PDF_BOOK_PATH)
pdf_documents = loader.load()

reviews_vector_db = Chroma.from_documents(
    pdf_documents, OpenAIEmbeddings(), persist_directory=BOOK_CHROMA_PATH
)