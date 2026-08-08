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
