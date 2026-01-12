"""Tests for API ingester."""

import pytest

from highbar.ingest.api import APIConfig, APIIngester


def test_api_config() -> None:
    """Test API config creation."""
    config = APIConfig(base_url="https://api.example.com", api_key="test-key")
    assert config.base_url == "https://api.example.com"
    assert config.api_key == "test-key"


def test_api_ingester_init() -> None:
    """Test API ingester initialization."""
    config = APIConfig(base_url="https://api.example.com")
    ingester = APIIngester(config)
    assert ingester.config == config


def test_api_fetch() -> None:
    """Test API fetch method."""
    config = APIConfig(base_url="https://api.example.com")
    ingester = APIIngester(config)
    docs = ingester.fetch({"query": "test"})
    assert isinstance(docs, list)


def test_api_ingest() -> None:
    """Test API ingest method."""
    config = APIConfig(base_url="https://api.example.com")
    ingester = APIIngester(config)
    result = ingester.ingest({"query": "test"}, "./output")
    assert "documents_ingested" in result
    assert "output_path" in result
