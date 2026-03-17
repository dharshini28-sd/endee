from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = []
embeddings = []

def store_docs(texts):
    global documents, embeddings
    documents = texts
    embeddings = [model.encode(t) for t in texts]

def retrieve(query):
    query_vec = model.encode(query)
    scores = [np.dot(query_vec, emb) for emb in embeddings]
    best_idx = scores.index(max(scores))
    return documents[best_idx]