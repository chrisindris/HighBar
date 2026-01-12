"""Tests for RAG baseline."""

import pytest

from highbar.baselines.rag import RAGBaseline, RAGConfig, RAGInput


def test_rag_config() -> None:
    """Test RAG config creation."""
    config = RAGConfig(
        retriever_model="test-retriever",
        generator_model="test-generator",
        top_k=3,
    )
    assert config.retriever_model == "test-retriever"
    assert config.top_k == 3


def test_rag_init() -> None:
    """Test RAG baseline initialization."""
    config = RAGConfig()
    baseline = RAGBaseline(config)
    assert baseline.config == config


def test_rag_run(sample_documents: list[str]) -> None:
    """Test RAG run method."""
    config = RAGConfig()
    baseline = RAGBaseline(config)
    input_data = RAGInput(query="What is criminal law?", documents=sample_documents)
    output = baseline.run(input_data)

    assert hasattr(output, "generated_text")
    assert hasattr(output, "retrieved_docs")
    assert isinstance(output.retrieved_docs, list)
