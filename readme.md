# Product Recommender RAG Chatbot

![Chatbot Demo]()

## Overview

Whenever a product is purchased online, users first scroll through reviews and ratings. This project provides an **AI-driven product recommendation system** that generates personalized responses based solely on customer reviews from marketplaces like Amazon and Flipkart. Unlike conventional chatbots, this RAG (Retrieval-Augmented Generation) chatbot combines real-time retrieval of relevant information with large language models to answer queries contextually and accurately.

The system is trained on **5000+ curated reviews** and can handle follow-up questions while maintaining conversational context. It is designed to help users make informed decisions without sifting manually through countless reviews.

---

## Key Features

- **Context-Aware Responses**: Maintains chat history to answer questions referencing prior interactions.  
- **Personalized Product Recommendations**: Generates insights from user reviews and ratings.  
- **RAG Pipeline**: Combines vector retrieval with LLM generation for precise and relevant answers.  
- **Interactive Web Interface**: Chat sessions are supported via a Flask/Gunicorn backend.  
- **Deployment-Ready**: Fully Dockerized and CI/CD integrated for easy cloud deployment.

---

## Tech Stack

- **Python 3.10** – Core programming language for backend and pipeline.  
- **LangChain & LangChain-Community** – Framework for RAG pipelines and history-aware retrievers.  
- **HuggingFace & Groq LLMs** – Large language models for natural language generation.  
- **AstraDB** – Cloud vector database storing embeddings for fast semantic search.  
- **Docker** – Containerization for reproducible deployments across environments.  
- **CI/CD with GitHub Actions** – Automates testing, build, and deployment processes.  
- **Streamlit / Flask** – Optional front-end for interactive chat demos.  

---

## Architecture

1. **Data Ingestion**: Collects product reviews, cleans, preprocesses, and creates embeddings using HuggingFace models.  
2. **Vector Store**: Embeddings stored in AstraDB allow fast semantic search and retrieval.  
3. **Retriever**: Reformulates queries based on chat history and fetches relevant review context.  
4. **Generator**: LLM generates precise responses using retrieved context.  
5. **Conversation Management**: Supports session-based chat history for follow-up and multi-turn conversations.



git clone https://github.com/preetibhattacharya/Product-Recommender-RAG.git
cd Product-Recommender-RAG
