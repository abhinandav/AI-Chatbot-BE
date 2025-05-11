import chromadb
from chromadb.utils import embedding_functions

# Use persistent directory
client = chromadb.PersistentClient(path="chroma_db")

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# This collection will now be persisted
collection = client.get_or_create_collection(name="news_articles", embedding_function=embedding_fn)

def add_documents(documents: list[str], metadatas: list[dict], ids: list[str]):
    collection.add(documents=documents, metadatas=metadatas, ids=ids)
    # client.persist()  # No need to save manually, it's persisted automatically

def retrieve_top_k(query: str, k: int = 5):
    print(">>> Total documents in collection:", collection.count())
    results = collection.query(query_texts=[query], n_results=k)
    return results["documents"][0]
