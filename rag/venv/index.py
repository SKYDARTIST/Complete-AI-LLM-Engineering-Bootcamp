from dotenv import load_dotenv



from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore


load_dotenv()


pdf_path = Path(__file__).parent / "nodejs.pdf"

#load this file into python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

#split the doc into smaller chunks


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

chunks = text_splitter.split_documents(docs)

#vector embedding

vector_embed = OpenAIEmbeddings(
    model_name="text-embedding-3-small",
)


vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=vector_embed,
    url="http://localhost:6333",
    collection_name="learning_rag",
)

print("Vector store created successfully")