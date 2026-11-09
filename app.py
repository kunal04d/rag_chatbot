import os
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
from backend.retrieval import ask
from langchain_groq import ChatGroq

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
 st.error("GROQ_API_KEY not found. Check your .env file.")
 st.stop()

llm = ChatGroq(
model="openai/gpt-oss-120b",
groq_api_key=api_key
)

st.title("College RAG Chatbot")
st.write("Welcome to my application!")

question = st.text_input("Ask your question")

if st.button("Submit"):
    if question.strip():
        with st.spinner("Finding an answer..."):
            answer, sources = ask(question, llm)

        st.write("### Answer")
        st.write(answer)

        st.write("### Sources")
        for source, page in sources:
            st.write(f"{source} — Page {page}")
    else:
        st.warning("Please enter a question.")