"""Data ingestion modules for legal documents."""

from highbar.ingest.api import APIIngester
from highbar.ingest.hf import HuggingFaceIngester
from highbar.ingest.parquet import ParquetIngester
from highbar.ingest.mcp import MCPIngester

__all__ = [
    "APIIngester",
    "HuggingFaceIngester",
    "ParquetIngester",
    "MCPIngester",
]
