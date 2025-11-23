from langchain_astradb import AstraDBVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
from Chatbot.data_converter import convert_reviews_to_documents

load_dotenv()

# Environment variables
ASTRA_DB_API = os.getenv("ASTRA_DB_API")
ASTRA_DB_TOKEN = os.getenv("ASTRA_DB_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
HF_TOKEN = os.getenv("HF_TOKEN")

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def safe_embed_documents(docs):
    """Safely embed documents, skip any that fail."""
    embedded_docs = []
    for doc in docs:
        try:
            emb = embeddings.embed_query(doc.page_content)
            if emb is not None:
                embedded_docs.append(doc)
        except Exception as e:
            print(f"Embedding failed for doc {doc.metadata}: {e}")
    return embedded_docs

def data_ingestion(status=None):
    vstore = AstraDBVectorStore(
        embedding=embeddings,
        collection_name="Product_Reviews_amazon",
        api_endpoint=ASTRA_DB_API,
        token=ASTRA_DB_TOKEN,
        namespace=ASTRA_DB_KEYSPACE
    )

    if status is None:
        docs = convert_reviews_to_documents()
        docs = safe_embed_documents(docs)  # filter out docs with failed embeddings
        if docs:
            insert_ids = vstore.add_documents(docs)
            print(f"\nInserted {len(insert_ids)} documents.")
            return vstore, insert_ids
        else:
            print("No documents could be embedded.")
            return vstore, []
    else:
        return vstore

if __name__ == "__main__":
    vstore, insert_ids = data_ingestion(None)
    query = "Can you tell me the low budget sound basshead?"
    results = vstore.similarity_search(query)
    for res in results:
        print(f"\n{res.page_content} [{res.metadata}]")
