import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

vector_embed = OpenAIEmbeddings(model="text-embedding-3-small")

vector_db = QdrantVectorStore.from_existing_collection(
    collection_name="learning_rag",
    embedding=vector_embed,
    url="http://localhost:6333",
)

user_query = input("Ask question : ")

docs = vector_db.similarity_search(query=user_query, k=3)

context = "\n".join([doc.page_content for doc in docs])

SYSTEM_PROMPT = f"""answer the following question based on the context provided
if the answer is not in the context, say i don't know

Context : {context}
Question : {user_query}
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ],
)

print(response.choices[0].message.content)
