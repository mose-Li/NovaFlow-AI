Database_Design.md

1. Introduction

2. Database Overview

3. Entity Relationship

4. Table Design

5. Repository Layer

6. Data Flow

7. Design Principles

8. Performance Considerations

9. Scalability

10. Future Improvements

# Database Design

## 1. Introduction

NovaFlow AI stores documents, semantic chunks, and vector embeddings in a relational database.

The current implementation uses SQLite for simplicity and local deployment. However, the architecture has been intentionally designed to support future migration to enterprise database systems such as PostgreSQL without major changes to the business logic.

All database access is encapsulated inside the Repository Layer, ensuring a clear separation between persistence and application logic.

## 2. Database Overview

The current database consists of three primary entities:

- Documents
- Chunks
- Embeddings

These entities form the foundation of the Retrieval-Augmented Generation (RAG) pipeline.

Each uploaded document is divided into multiple semantic chunks, and each chunk is associated with one embedding vector.

This normalized structure minimizes data redundancy while supporting efficient retrieval.

## 3. Entity Relationship

The relationships between entities are illustrated below.

```

Documents
│
├──────────────┐
│ 1 : N │
▼
Chunks
│
├──────────────┐
│ 1 : 1 │
▼
Embeddings

```

Relationship Summary

• One document contains multiple chunks.

• Each chunk has one embedding.

• Embeddings are generated only after chunk creation.


## 4. Table Design

### Documents

Stores metadata for uploaded documents.

| Column | Type | Description |
|---------|------|-------------|
| id | INTEGER | Primary key |
| filename | TEXT | Original filename |
| stored_filename | TEXT | Stored filename |
| checksum | TEXT | SHA256 checksum |
| file_size | INTEGER | File size |
| status | TEXT | Processing status |
| created_at | DATETIME | Upload timestamp |

---

### Chunks

Stores semantic chunks extracted from documents.

| Column | Type | Description |
|---------|------|-------------|
| id | INTEGER | Primary key |
| document_id | INTEGER | Foreign key |
| chunk_index | INTEGER | Chunk sequence |
| content | TEXT | Chunk text |

---

### Embeddings

Stores embedding vectors for each chunk.

| Column | Type | Description |
|---------|------|-------------|
| id | INTEGER | Primary key |
| chunk_id | INTEGER | Foreign key |
| model | TEXT | Embedding model |
| embedding | TEXT | JSON vector |

## 5. Repository Layer

NovaFlow AI uses the Repository Pattern to isolate database access from business logic.

Current repositories include:

- DocumentRepository
- EmbeddingRepository

Responsibilities include:

- CRUD operations
- Database abstraction
- Query encapsulation
- Future database migration support

Business services never execute SQL directly. All persistence logic is delegated to repositories.

## 6. Data Flow

The database interaction follows two primary workflows.

### Document Indexing

```

Upload Document

↓

Document Table

↓

Chunk Table

↓

Embedding Table

```

---

### Retrieval

```

User Question

↓

Embedding Generation

↓

Embedding Table

↓

Chunk Table

↓

Document Table

↓

Retrieved Contexts

```


## 7. Design Principles

The database design follows several engineering principles.

### Normalization

Documents, chunks, and embeddings are stored separately to reduce redundancy.

---

### Consistency

Each embedding always references exactly one chunk.

Each chunk always belongs to exactly one document.

---

### Maintainability

Repository classes encapsulate all persistence logic.

Future database changes require minimal modifications.

---

### Extensibility

Additional metadata fields can be introduced without affecting existing modules.

## 8. Performance Considerations

Current implementation prioritizes simplicity and readability.

Performance optimizations include:

- Store embeddings only once
- Avoid duplicate document uploads using SHA256 checksum
- Retrieve only Top-K contexts
- Lazy loading through repositories

Future optimization may include:

- Database indexing
- Batch insertion
- Connection pooling
- Vector indexes

## 9. Scalability

Although SQLite is sufficient for local deployment, the architecture supports enterprise scalability.

Planned database upgrades include:

- PostgreSQL
- MySQL
- Microsoft SQL Server

Vector storage may migrate to:

- Milvus
- FAISS
- Qdrant
- ChromaDB
- Weaviate

Because repositories isolate persistence logic, these migrations require only minimal modifications.

## 10. Future Improvements

Future versions of the database layer may include:

- Multi-user support
- Role-based permissions
- Conversation history
- Prompt history
- Retrieval logs
- Usage statistics
- Model configuration
- Workflow storage
- Agent memory

These enhancements will support enterprise knowledge management and large-scale AI applications.

+--------------------+
| Documents          |
+--------------------+
| id                 |
| filename           |
| stored_filename    |
| checksum           |
| file_size          |
| status             |
| created_at         |
+--------------------+
          |
          | 1
          |
          | N
+--------------------+
| Chunks             |
+--------------------+
| id                 |
| document_id (FK)   |
| chunk_index        |
| content            |
+--------------------+
          |
          | 1
          |
          | 1
+--------------------+
| Embeddings         |
+--------------------+
| id                 |
| chunk_id (FK)      |
| model              |
| embedding          |
+--------------------+