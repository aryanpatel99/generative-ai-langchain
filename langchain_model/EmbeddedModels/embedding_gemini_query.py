from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", dimensions=32)

vector = embeddings.embed_query("What is the capital of France?")

print(str(vector[:5]))