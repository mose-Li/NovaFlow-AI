# 🚀 NovaFlow AI

> **Enterprise AI Knowledge Platform powered by Retrieval-Augmented Generation (RAG), Hybrid Retrieval, Semantic Chunking and Local Large Language Models.**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-v1.0-success)

NovaFlow AI is an enterprise-oriented AI platform designed for intelligent document management, knowledge retrieval, AI-powered question answering, and enterprise knowledge assistants.

Unlike traditional chatbot demos, NovaFlow AI focuses on production-ready Retrieval-Augmented Generation (RAG) architecture with modular design, explainable retrieval, hybrid search, and local Large Language Model deployment.

---

# Current Version

**Version 1.0**

Enterprise Retrieval-Augmented Generation Platform

---

# Table of Contents

1. Project Overview
2. Key Features
3. System Architecture
4. Technology Stack
5. Project Structure
6. Core Modules
7. Retrieval Pipeline
8. Database Design
9. Quick Start
10. REST API
11. Testing
12. Performance
13. Screenshots
14. Roadmap
15. Project Highlights
16. Documentation
17. License
18. Contact

---

# Project Overview

NovaFlow AI is a modular enterprise Retrieval-Augmented Generation platform designed for intelligent knowledge management.

The platform combines dense semantic retrieval, sparse lexical retrieval, reranking, metadata filtering, diversity retrieval, dynamic ranking, and local Large Language Models to provide accurate, explainable, and privacy-preserving AI assistants.

The architecture emphasizes:

- Enterprise scalability
- High maintainability
- Modular design
- Explainable retrieval
- Production readiness
- Local deployment

NovaFlow AI can serve as the foundation for enterprise knowledge bases, AI copilots, intelligent document search, customer support systems, and future multi-agent workflows.

---

# Key Features

| Feature | Status |
|----------|--------|
| Document Upload | ✅ |
| Smart Chunking | ✅ |
| Semantic Embedding | ✅ |
| Vector Retrieval | ✅ |
| BM25 Retrieval | ✅ |
| Hybrid Retrieval | ✅ |
| Score Normalization | ✅ |
| Weighted Score Fusion | ✅ |
| Metadata Filtering | ✅ |
| Diversity Retrieval | ✅ |
| Dynamic Top-K | ✅ |
| CrossEncoder Reranking | ✅ |
| Source Attribution | ✅ |
| Local LLM Integration | ✅ |
| REST API | ✅ |
| Docker | 🚧 |
| PostgreSQL | 🚧 |
| Redis Cache | 🚧 |
| Milvus / FAISS | 🚧 |
| Multi-user Support | 🚧 |

---

# System Architecture

> Enterprise Architecture

![Architecture](docs/images/architecture.png)

---

# Technology Stack

| Layer | Technology |
|---------|------------|
| Language | Python 3.12 |
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| Vector Search | Cosine Similarity |
| Sparse Retrieval | BM25 |
| Hybrid Retrieval | Weighted Score Fusion |
| Reranker | BAAI/bge-reranker-base |
| LLM | Ollama + Llama3.2 |
| API | RESTful API |
| Testing | Pytest |
| Version Control | Git |
| Documentation | Markdown |
| Future Database | PostgreSQL |
| Future Vector DB | Milvus / FAISS |

---

## Engineering Principles

NovaFlow AI follows several software engineering principles.

- High Cohesion
- Low Coupling
- Modular Architecture
- Explainable AI
- Enterprise Scalability
- Local-first AI
- Production-oriented Design

---

# Project Structure

```text
NovaFlow-AI
│
├── backend/
│   ├── api/
│   ├── chunk/
│   ├── embedding/
│   ├── llm/
│   ├── rag/
│   ├── retrieval/
│   ├── repositories/
│   ├── services/
│   └── utils/
│
├── config/
├── database/
├── docs/
├── frontend/
├── tests/
├── uploads/
│
├── README.md
├── LICENSE
└── requirements.txt
```

---

# Core Modules

- Document Management
- Smart Chunk Engine
- Embedding Service
- Vector Search
- BM25 Search
- Hybrid Search
- Metadata Filter
- Diversity Filter
- Dynamic Top-K
- CrossEncoder Reranker
- Prompt Builder
- Chat Service
- REST API

---

# Retrieval Pipeline

![Retrieval Pipeline](docs/images/retrieval_pipeline.png)

---

# Database Design

![Database ER](docs/images/database_er.png)

---

# Quick Start

## Clone Repository

```bash
git clone https://github.com/yourname/NovaFlow-AI.git
cd NovaFlow-AI
```

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Ollama

```bash
ollama serve
```

```bash
ollama pull llama3.2
```

## Initialize Database

```bash
python -m database.init_db
```

## Import Demo Documents

```bash
python -m tests.test_import_documents
```

## Start FastAPI

```bash
uvicorn backend.main:app --reload
```

Open Swagger:

```
http://127.0.0.1:8000/docs
```

---

# REST API

## Document APIs

| Method | Endpoint |
|---------|----------|
| POST | /documents/upload |
| GET | /documents |
| DELETE | /documents/{id} |

## Retrieval APIs

| Method | Endpoint |
|---------|----------|
| POST | /search |

## Chat APIs

| Method | Endpoint |
|---------|----------|
| POST | /chat |

## Health

| Method | Endpoint |
|---------|----------|
| GET | /health |

---

# Testing

The complete Retrieval-Augmented Generation pipeline has been validated through unit tests and integration tests.

| Test | Status |
|--------|--------|
| Smart Chunking | ✅ |
| Overlap Chunking | ✅ |
| Large Document Chunking | ✅ |
| Vector Retrieval | ✅ |
| Hybrid Retrieval | ✅ |
| Metadata Filtering | ✅ |
| Diversity Filtering | ✅ |
| Dynamic Top-K | ✅ |
| Source Attribution | ✅ |
| Chat Service | ✅ |

Detailed screenshots are available under:

```
docs/testing/
```

---

# Performance

| Metric | Current |
|---------|---------|
| Retrieval Strategy | Hybrid Retrieval |
| Ranking | CrossEncoder |
| Source Attribution | Supported |
| Local Deployment | Supported |
| Explainable Answer | Supported |

Future benchmarks will include latency, throughput, retrieval accuracy, and memory usage.

---

# Screenshots

## Swagger API

![Swagger](docs/images/swagger.png)

---

## Chat Service

![Chat](docs/images/chat.png)

---

## Upload Documents

![Upload](docs/images/upload.png)

---

## Retrieval Pipeline

![Pipeline](docs/images/retrieval_pipeline.png)

---

# Roadmap

## v1.1

- Streaming Responses
- Prompt Templates
- Multi-file Retrieval

## v1.2

- PostgreSQL
- Redis Cache
- Docker Deployment

## v1.5

- Milvus
- FAISS
- Authentication
- RBAC

## v2.0

- Enterprise Knowledge Base
- Multi-Agent Collaboration
- Workflow Engine
- Kubernetes Deployment

---

# Project Highlights

### Enterprise Architecture

Modular service-oriented architecture suitable for enterprise deployment.

### Hybrid Retrieval

Combines semantic retrieval and lexical retrieval for improved recall and precision.

### Explainable AI

Every generated answer supports source attribution.

### Local AI

Runs completely offline through Ollama.

### Future-ready

Designed for PostgreSQL, Redis, Milvus, Docker, Kubernetes and cloud-native deployment.

---

# Documentation

Detailed technical documentation is available under:

```
docs/
```

Including:

- Architecture Design
- Retrieval Pipeline
- Database Design
- API Documentation
- Technical Specification

---

# License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

# Contact

GitHub

```
https://github.com/yourname
```

Freelancer

```
https://www.freelancer.com/u/yourname
```

Email

```
your@email.com
```