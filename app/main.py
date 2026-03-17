import streamlit as st
from retriever import store_docs, retrieve
from generator import generate_answer

# Load data
with open("data/sample.txt", "r") as f:
    texts = f.read().split("\n")

store_docs(texts)

st.title("AI Document Assistant")

query = st.text_input("Ask a question:")

if query:
    context = retrieve(query)
    answer = generate_answer(context, query)
    st.write("Answer:", answer)