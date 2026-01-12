# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-01-12

### Added
- Initial scaffold of HighBar benchmark repository
- Five legal AI tasks: RGC, Entity Extraction, Summary Completion, Clause Outlining, QA with Retrieval
- Four evaluation metrics: GCP, AC, HR, FGS
- Data ingestion modules: API, HuggingFace, Parquet, MCP
- Authority-based reranking for legal documents
- Governance modules: content bans, PII detection, license gating
- Three baseline models: RAG, Encoder, Seq2Seq
- Utility modules: citation checker, authority checker, snapshot manifests, seed control
- Typer-based CLI with ingest, run, score, and report commands
- Poetry-based project configuration with Python 3.10+ support
- Pytest-based test infrastructure
- GitHub Actions CI/CD pipeline
- Docker and docker-compose support
- Comprehensive documentation and examples

### Dependencies
- PyTorch 2.0+
- HuggingFace Transformers 4.35+
- Typer for CLI
- Pydantic for data validation
- Rich for console output
