document-search-platform/

app/
│
├── api/
│
├── application/
│   ├── dto/
│   ├── dependencies.py
│   ├── services/
│   └── use_cases/
│
├── domain/
│   ├── entities/
│   ├── enums/
│   ├── events/
│   ├── exceptions/
│   ├── ports/
│   ├── repositories/
│   └── value_objects/
│
├── infrastructure/
│   ├── persistence/
│   │   ├── database.py
│   │   ├── session.py
│   │   ├── unit_of_work.py
│   │   ├── repositories/
│   │   ├── mappers/
│   │   ├── models/
│   │   └── migrations/
│   │
│   ├── storage/
│   ├── parser/
│   ├── embeddings/
│   ├── llm/
│   ├── vectorstore/
│   └── observability/
│
├── agents/
├── rag/
├── core/
└── tests/




Coding Standards
1. One Responsibility Per File

✅

document_mapper.py

❌

mapper.py

with 20 mappers.

2. One Class Per File

Good

class UploadService:

Bad

class UploadService:

class ChunkService:

class EmbedService:
3. No Wildcard Imports

Never

from x import *

Always

from app.domain.entities.document import Document
4. Absolute Imports Only

Good

from app.domain.entities.document import Document

Bad

from ....entities.document import Document
5. Type Hints Everywhere

Every function

def upload(
    file: UploadFile
) -> Document:
6. Async First

Database

↓

Storage

↓

LLM

↓

Everything async.

7. No Business Logic

Inside

Controller

Repository

Mapper

Only

Use Case

Domain
8. No SQLAlchemy

Inside

Domain

Ever.

9. Domain Knows Nothing

About

PostgreSQL
FastAPI
Docling
Ollama
LlamaIndex
10. Infrastructure Knows Everything

Infrastructure can import

everything.

Layer Rules
API

↓

Application

↓

Domain

↓

Infrastructure

Allowed

↓

API

↓

Application

Not allowed

↓

Domain

↓

FastAPI
Naming Convention

Interfaces

IDocumentRepository

IUnitOfWork

IStorage

IChecksumService

Implementations

PostgresDocumentRepository

LocalStorage

SHA256ChecksumService
Folder Convention

One file

↓

One class

document_model.py

DocumentModel

Always.

Exception Rule

Never

except Exception:
    pass

Always

logger.exception(...)

raise
Logging Rule

Every

Upload
Parsing
Embedding
Retrieval
Evaluation

gets logged.

Commit Rule

One feature

↓

One commit

Example

feat(upload): implement upload use case

feat(storage): implement local storage

feat(vector): implement pgvector search

test(upload): add upload integration tests
Testing Rule

Every production file

↓

Eventually

gets

Unit Test

Integration Test

No exceptions.

Build Order (Final)

Now we never change it.

Sprint 0

Engineering Standards
    ✅

Sprint 1

Foundation
    ✅

Sprint 2

Persistence
    Current

Sprint 3

Infrastructure

Sprint 4

Application

Sprint 5

API

Sprint 6

Worker

Sprint 7

Docling

Sprint 8

Chunking

Sprint 9

Embeddings

Sprint 10

PGVector

Sprint 11

LlamaIndex

Sprint 12

CrewAI

Sprint 13

Phoenix

Sprint 14

RAGAs

Sprint 15

OpenWebUI
🚀 The Very Next File

Now that the architecture is frozen, I recommend we continue with this exact sequence:

1. database.py
2. session.py
3. postgres_document_repository.py
4. unit_of_work.py
5. alembic
6. tests
Why This Order?

Because the dependency chain is correct:

Database Engine
       │
       ▼
Session Factory
       │
       ▼
Repository
       │
       ▼
Unit Of Work
       │
       ▼
Use Case
       │
       ▼
FastAPI Controller

This prevents circular dependencies and minimizes future refactoring.