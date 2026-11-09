College RAG Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot that allows students to interact with their college notes and study materials through natural language queries.

The application uses semantic search to retrieve relevant information from uploaded PDF documents and generates context-aware answers using a Large Language Model (LLM).

Overview

Students often need to search through multiple PDF documents to find specific information. This project simplifies that process by providing an AI-powered interface where users can ask questions and receive answers based on their study materials.

Instead of relying entirely on an LLM’s pretrained knowledge, the chatbot retrieves relevant context from uploaded documents before generating a response.

Features

* PDF Document Processing: Extract text from PDF study materials using PyMuPDF.
* Text Chunking: Split extracted text into smaller, manageable chunks.
* Semantic Search: Convert text chunks into vector embeddings using Sentence Transformers.
* Vector Database: Store and retrieve embeddings using Qdrant.
* Context-Aware Responses: Generate answers using retrieved document context.
* FastAPI Backend: Handle document ingestion and chatbot API requests.
* Interactive Interface: Chat with your study materials through Streamlit.
* Source Metadata: Maintain document names and page numbers for retrieved chunks.

Tech Stack

Component	Technology
Programming Language	Python
Backend	FastAPI
Frontend	Streamlit
LLM	Groq API
LLM Model	Llama 3.3 70B Versatile
Embedding Model	all-MiniLM-L6-v2
Vector Database	Qdrant
PDF Processing	PyMuPDF
ML Framework	Sentence Transformers

Architecture

The application follows a Retrieval-Augmented Generation pipeline.

1. Document Ingestion

* Load PDF documents from the documents directory.
* Extract text using PyMuPDF.
* Split extracted text into smaller chunks.
* Generate vector embeddings for each chunk.
* Store embeddings and metadata in Qdrant.

2. Retrieval

* Receive a user’s question.
* Convert the question into a vector embedding.
* Perform similarity search against stored document embeddings.
* Retrieve the most relevant chunks.

3. Generation

* Pass the retrieved context and user’s question to the LLM.
* Generate a response using the Groq API.
* Return the generated answer to the frontend.

Workflow

          PDF Documents
                |
                v
         Text Extraction
                |
                v
           Text Chunking
                |
                v
       Generate Embeddings
                |
                v
          Qdrant Database
                |
                |
       User Asks a Question
                |
                v
       Generate Query Embedding
                |
                v
         Semantic Retrieval
                |
                v
       Retrieve Relevant Chunks
                |
                v
          Groq LLM API
                |
                v
        Contextual Answer
                |
                v
          Streamlit UI

Project Structure

rag_chatbot/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── ingestion.py
│   ├── retrieval.py
│   └── config.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── documents/
│       ├── OS_Notes.pdf
│       ├── DBMS_Notes.pdf
│       └── Computer_Networks.pdf
│
├── qdrant_data/
│
├── .env
├── .gitignore
└── requirements.txt

Installation and Setup

1. Clone the Repository

git clone https://github.com/kunal04d/rag_chatbot.git
cd rag_chatbot

2. Create a Virtual Environment

python -m venv venv

Activate the environment:

macOS / Linux

source venv/bin/activate

Windows

venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the root directory.

GROQ_API_KEY=your_groq_api_key

Get your API key from the Groq developer platform.

5. Add Documents

Place your PDF study materials inside:

data/documents/

6. Run the Backend

uvicorn backend.main:app --reload

The FastAPI backend will be available at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

7. Run the Frontend

Open another terminal, activate your virtual environment, and execute:

streamlit run frontend/app.py

The Streamlit interface will open in your browser.

How It Works

The chatbot uses Retrieval-Augmented Generation (RAG) to combine information retrieval with LLM-based response generation.

Unlike a traditional chatbot that generates answers using only its pretrained knowledge, this system first searches the uploaded study materials to find relevant information.

This helps generate answers grounded in the provided documents and reduces the chances of irrelevant or unsupported responses.

Future Improvements

* Support for additional document formats.
* Source citations with document names and page numbers.
* Conversation history and multi-turn interactions.
* Subject-wise document filtering.
* Improved retrieval using hybrid search.
* Reranking for better retrieval accuracy.
* Deployment using Docker and cloud infrastructure.

Author

Kunal Duvey

B.Tech – Computer Science and Engineering (AI)

GitHub: kunal04d

⸻

Built to make studying and accessing academic resources easier through Retrieval-Augmented Generation.
