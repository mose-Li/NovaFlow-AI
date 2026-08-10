System_Architecture.md

1. Introduction

2. Design Objectives

3. Overall Architecture

4. Layered Architecture

5. Core Components

6. Data Flow

7. Module Interaction

8. Design Principles

9. Scalability

10. Future Architecture

# System Architecture

## 1. Introduction

NovaFlow AI is an enterprise-oriented Retrieval-Augmented Generation (RAG) platform designed for intelligent knowledge management and AI-powered question answering.

The architecture adopts a modular and service-oriented design to ensure maintainability, scalability, and production readiness.

Each functional component is isolated behind well-defined interfaces, allowing future replacement or extension without affecting the overall system.

The current implementation focuses on local deployment using Ollama and SQLite while keeping compatibility with future distributed databases and cloud-native infrastructure.

## 2. Design Objectives

The architecture is designed according to the following principles:

- High Cohesion
- Low Coupling
- Modular Design
- Explainable Retrieval
- Easy Deployment
- Enterprise Scalability
- Privacy-first AI
- Production-oriented Architecture

## 3. Overall Architecture

NovaFlow AI consists of five major layers:

1. Client Layer
2. API Layer
3. Service Layer
4. Retrieval Layer
5. Data Layer

Each layer communicates only with adjacent layers, ensuring clean architecture and separation of responsibilities.

                    User
                      │
                      ▼
               FastAPI REST API
                      │
                      ▼
                Chat Service
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   Retrieval Engine          Document Service
          │
          ▼
 Hybrid Retrieval Engine
          │
   ┌──────┴────────┐
   ▼               ▼
Vector Search   BM25 Search
   │               │
   └──────┬────────┘
          ▼
Score Fusion
          ▼
Metadata Filter
          ▼
Diversity Filter
          ▼
Dynamic Top-K
          ▼
CrossEncoder
          ▼
Prompt Builder
          ▼
Ollama LLM
          ▼
Final Answer

| Component         | Responsibility                 |
| ----------------- | ------------------------------ |
| API Layer         | REST interface                 |
| Document Service  | Document upload and management |
| Chunk Engine      | Smart document chunking        |
| Embedding Service | Generate embeddings            |
| Vector Search     | Semantic retrieval             |
| BM25 Search       | Keyword retrieval              |
| Hybrid Search     | Score fusion                   |
| Reranker          | Candidate reranking            |
| Prompt Builder    | Build LLM prompts              |
| Chat Service      | Coordinate end-to-end workflow |
| Ollama            | Local LLM inference            |
| Repository Layer  | Database access                |


Document Upload

↓

Chunking

↓

Embedding

↓

Database

↓

User Question

↓

Embedding

↓

Hybrid Search

↓

Rerank

↓

Prompt

↓

LLM

↓

Answer

↓

Source Attribution

## 7. Module Interaction

NovaFlow AI adopts a layered and modular architecture where each component has a single responsibility and communicates through well-defined interfaces. This design minimizes coupling and allows individual modules to evolve independently.

### 7.1 Document Processing Workflow

The document processing workflow begins when a user uploads a document through the REST API.

1. The **FastAPI** endpoint receives the uploaded file.
2. The **Document Service** validates the file type, checksum, and metadata.
3. The **Smart Chunk Engine** splits the document into semantic chunks.
4. The **Embedding Service** generates vector embeddings for every chunk.
5. The **Repository Layer** stores the document, chunks, and embeddings in the database.

The indexing process is completed only after all chunks and embeddings have been successfully stored.

---

### 7.2 Retrieval Workflow

When a user submits a question:

1. The **Chat Service** receives the request.
2. The **Embedding Service** converts the question into a semantic vector.
3. **Vector Search** retrieves semantically similar chunks.
4. **BM25 Search** retrieves keyword-matching chunks.
5. **Hybrid Search** merges both result sets.
6. Scores are normalized and fused using weighted score fusion.
7. Metadata filtering removes irrelevant documents.
8. Diversity filtering reduces redundant contexts.
9. Dynamic Top-K selects the most appropriate number of contexts.
10. The **CrossEncoder Reranker** performs semantic reranking.
11. The **Prompt Builder** constructs the final prompt.
12. The prompt is sent to the local **Ollama LLM**.
13. The generated answer is returned together with source attribution.

---

### 7.3 Component Dependencies

The dependency relationships are intentionally simple.

FastAPI
→ Chat Service
→ Hybrid Search
→ Vector Search / BM25 Search
→ Repository Layer
→ SQLite Database

The LLM is isolated behind the LLM Service, allowing future replacement without affecting other modules.

---

### 7.4 Loose Coupling

Each module exposes only public interfaces.

For example:

- Chat Service does not know how embeddings are generated.
- Hybrid Search does not know how vectors are stored.
- Prompt Builder does not know how retrieval is implemented.

This separation improves maintainability and future extensibility.

## 8. Design Principles

NovaFlow AI follows modern software engineering principles commonly adopted in enterprise AI systems.

### 8.1 Separation of Concerns

Each module is responsible for a single business capability.

Examples:

- Chunk Engine only performs document chunking.
- Embedding Service only generates embeddings.
- Vector Search only performs semantic retrieval.
- Chat Service orchestrates the complete workflow.

This design significantly reduces system complexity.

---

### 8.2 High Cohesion

Business logic belonging to the same domain is grouped into a dedicated module.

For example:

backend/chunk/

backend/retrieval/

backend/services/

backend/repositories/

Each package has clear responsibilities and minimal overlap.

---

### 8.3 Low Coupling

Modules communicate only through interfaces.

Replacing one implementation should require little or no modification to other components.

Examples include:

- SQLite → PostgreSQL
- Ollama → OpenAI
- Cosine Search → FAISS
- BM25 → Elasticsearch

---

### 8.4 Explainable AI

Every generated answer should be traceable.

NovaFlow AI records:

- Document ID
- Chunk ID
- Chunk Index
- Retrieval Score

This improves transparency and user trust.

---

### 8.5 Local-first Deployment

The current implementation is designed for local execution.

Benefits include:

- Data privacy
- No cloud dependency
- Lower operational cost
- Enterprise compliance

---

### 8.6 Extensibility

Future technologies can be integrated without redesigning the entire system.

Planned integrations include:

- PostgreSQL
- Milvus
- FAISS
- Redis
- Docker
- Kubernetes

The modular architecture minimizes migration costs.

## 9. Scalability

NovaFlow AI has been designed with future scalability in mind.

Although the current implementation targets single-machine deployment, the architecture supports gradual evolution toward enterprise-scale systems.

---

### 9.1 Database Scalability

Current:

- SQLite

Future:

- PostgreSQL
- MySQL
- Microsoft SQL Server

Database access is isolated inside the Repository Layer, making migration straightforward.

---

### 9.2 Vector Database Scalability

Current:

- SQLite + JSON Embeddings

Future:

- FAISS
- Milvus
- ChromaDB
- Qdrant
- Weaviate

Only the Vector Search module requires replacement.

---

### 9.3 Retrieval Scalability

Current retrieval pipeline includes:

- Vector Search
- BM25 Search
- Hybrid Retrieval
- CrossEncoder Reranking

Future improvements may include:

- Query Expansion
- Multi-stage Retrieval
- Learning-to-Rank
- Reciprocal Rank Fusion
- Graph-based Retrieval

---

### 9.4 LLM Scalability

Current:

- Ollama
- Llama3.2

Future:

- GPT-5
- Claude
- Gemini
- DeepSeek
- Enterprise private models

The LLM Service abstracts all model interactions.

---

### 9.5 Deployment Scalability

Current deployment:

Single-machine deployment

Future deployment:

- Docker
- Docker Compose
- Kubernetes
- Cloud-native deployment
- Load balancing
- Horizontal scaling

## 10. Future Architecture

The current implementation represents the foundation of the NovaFlow AI platform.

Future releases will progressively extend the architecture toward enterprise-grade AI infrastructure.

---

### Version 0.6

Planned features:

- Streaming Chat
- Conversation Memory
- Prompt Templates
- Multi-document Retrieval
- Better Prompt Engineering

---

### Version 0.7

Infrastructure upgrades:

- PostgreSQL
- Redis Cache
- Docker Deployment
- Docker Compose
- Background Task Queue

---

### Version 0.8

Enterprise Retrieval:

- Milvus Integration
- FAISS Integration
- Incremental Indexing
- Distributed Retrieval
- Large-scale Knowledge Base

---

### Version 1.0

Enterprise AI Platform:

- Workflow Engine
- Multi-Agent Collaboration
- User Authentication
- Role-based Permission Control
- Knowledge Management Dashboard
- Monitoring & Logging
- API Gateway
- Enterprise Deployment

---

### Long-term Vision

NovaFlow AI aims to evolve into a complete enterprise AI platform capable of supporting:

- Intelligent document management
- Internal enterprise copilots
- AI customer service
- Knowledge automation
- Workflow orchestration
- Multi-agent collaboration
- Large-scale Retrieval-Augmented Generation (RAG)

The architecture is intentionally designed to support continuous evolution while maintaining backward compatibility and modular extensibility.

