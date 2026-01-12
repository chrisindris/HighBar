"""HighBar package metadata and configuration."""

from pathlib import Path

# Package metadata
PACKAGE_ROOT = Path(__file__).parent
PROJECT_ROOT = PACKAGE_ROOT.parent

# Version
__version__ = "0.1.0"

# Legal jurisdictions supported
SUPPORTED_JURISDICTIONS = [
    "ontario",
    "canada",
]

# Task types
TASK_TYPES = [
    "rgc",  # Regulatory Grounding Check
    "extract",  # Entity Extraction
    "summc",  # Summary Completion
    "claout",  # Clause Outlining
    "qar",  # Question Answering with Retrieval
]

# Metric types
METRIC_TYPES = [
    "gcp",  # Grounding Citation Precision
    "ac",  # Attribution Coverage
    "hr",  # Hallucination Rate
    "fgs",  # Factual Grounding Score
]

# Baseline types
BASELINE_TYPES = [
    "rag",  # Retrieval-Augmented Generation
    "encoder",  # Encoder baseline
    "seq2seq",  # Sequence-to-Sequence
]

# Ingest source types
INGEST_SOURCES = [
    "api",  # REST API
    "hf",  # HuggingFace
    "parquet",  # Parquet files
    "mcp",  # Model Context Protocol
]
