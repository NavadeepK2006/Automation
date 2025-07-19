import chromadb
from chromadb.config import Settings
from config import CHROMA_COLLECTION
client=chromadb.Client(Settings(anonymized_telemetry=False))
def add_version(doc_id,content):
    collection=client.get_or_create_collection(name=CHROMA_COLLECTION)
    collection.add(documents=[content],ids=[doc_id])
def search_versions(query):
    collection=client.get_collection(name=CHROMA_COLLECTION)
    results=collection.query(query_texts=[query],n_results=3)
    return results