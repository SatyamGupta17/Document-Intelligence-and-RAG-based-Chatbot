
import streamlit as st
import requests

st.title("Document Intelligence Chatbot")

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    files = {
        "file": uploaded_file
    }

    response = requests.post(
        "http://127.0.0.1:8000/upload",
        files=files
    )

    st.success("Document uploaded successfully")


# Chat
question = st.text_input(
    "Ask a Question"
)

if st.button("Ask"):

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        params={
            "query": question
        }
    )

    answer = response.json()

    st.write(answer["answer"])
    
if "history" not in st.session_state:
    st.session_state.history = []