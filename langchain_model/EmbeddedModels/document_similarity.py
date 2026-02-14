from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001",output_dimensionality=300)

document  = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting style and leadership skills.",
    "Ms Dhoni is a former Indian cricketer and captain of the Indian national team, known for his calm demeanor and finishing abilities.",
    "Sachin Tendulkar is a former Indian cricketer, also know as 'God of Cricket', who is widely regarded as one of the greatest batsmen in the history of cricket.",
    "Rohit Sharma is known for his elegant batting style and ability to score big centuries, especially in limited-overs formats.",
    "Jasprit Bumrah is an Indian fast bowler known for his unique bowling action and ability to bowl yorkers consistently."
]

query = "Tell me about the Bumrah"

document_embeddings = embeddings.embed_documents(document)
query_embedding = embeddings.embed_query(query)

# both should be 2D lists for cosine similarity to work
similarity_scores = cosine_similarity([query_embedding], document_embeddings)[0]
index, score = sorted(list(enumerate(similarity_scores)), key=lambda x: x[1])[-1]

print("Similarity Scores:", similarity_scores)
print(document[index], score)
