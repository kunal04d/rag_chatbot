from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Delhi is the capital of India",
    "delhi is capital of india with good infra as delhi need good infra",
    "india need delhi as capital",
    "dhaka is capital of Bangladesh ",
    
    
    "Kolkata is the capital of West Bengal"

]

query = "what is the capital of India"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

similarities = cosine_similarity(
    [query_embedding],
    doc_embeddings
)

scores = similarities[0]

index , score = sorted(list(enumerate(scores)),key = lambda x : x[1])[-1]

print(query)

print(documents[index])

print("similarity score :" ,score)
