from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", dimensions=32)

docs = [
    "The capital of France is Paris.",
    "The capital of Germany is Berlin.",    
    "The capital of Italy is Rome.",
]

result = embeddings.embed_documents(docs)

print(str(result[:5]))