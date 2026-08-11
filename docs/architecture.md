document-search-platform/
│
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── chat/
│   │   │   ├── documents/
│   │   │   ├── health/
│   │   │   └── evaluation/
│   │   └── router.py
│   │
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── retrieval_agent.py
│   │   ├── verifier_agent.py
│   │   ├── response_agent.py
│   │   └── crew.py
│   │
│   ├── rag/
│   │   ├── ingestion/
│   │   ├── retrieval/
│   │   ├── embeddings/
│   │   ├── index/
│   │   └── evaluation/
│   │
│   ├── database/
│   │   ├── postgres.py
│   │   ├── pgvector.py
│   │   └── models.py
│   │
│   ├── llm/
│   │   ├── ollama_client.py
│   │   └── prompts/
│   │
│   ├── observability/
│   │   ├── phoenix.py
│   │   └── tracing.py
│   │
│   ├── services/
│   ├── schemas/
│   ├── config.py
│   ├── dependencies.py
│   └── main.py
│
├── docs/
├── docker/
├── tests/
├── scripts/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md

Folder Structure (Final)
document-search-platform/
│
├── app/
│   ├── api/
│   ├── agents/
│   ├── rag/
│   ├── llm/
│   ├── prompts/
│   ├── database/
│   ├── observability/
│   ├── evaluation/
│   ├── services/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── utils/
│   └── main.py
│
├── docs/
├── docker/
├── tests/
├── scripts/
├── uploads/
├── data/
├── logs/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md


Clean Architecture

API Layer
     │
Service Layer
     │
AI Layer (CrewAI + LlamaIndex)
     │
Repository Layer
     │
PostgreSQL / PGVector



FOLDER STRUCTURE:
app/

api/
└── v1/
    └── endpoints/
        └── upload.py

application/
├── dto/
│   ├── upload_request.py
│   └── upload_response.py
│
├── services/
│   └── upload_service.py
│
└── use_cases/
    └── upload_document.py

domain/
├── entities/
│   └── document.py
│
├── enums/
│   └── document_status.py
│
├── repositories/
│   └── document_repository.py
│
├── ports/
│   ├── file_storage.py
│   ├── checksum.py
│   └── clock.py
│
└── exceptions/
    ├── duplicate_document.py
    └── invalid_document.py

infrastructure/

├── storage/
│   └── local_storage.py
│
├── checksum/
│   └── sha256_service.py
│
├── repositories/
│   └── postgres_document_repository.py
│
└── database/
    └── models/
        └── document_model.py

tests/

├── unit/
│   ├── upload_service_test.py
│   ├── checksum_test.py
│   └── storage_test.py
│
└── integration/
    └── upload_api_test.py
