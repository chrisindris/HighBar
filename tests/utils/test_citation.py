"""Tests for citation checker."""

import pytest

from highbar.utils.citation import Citation, CitationChecker


def test_citation_model() -> None:
    """Test Citation model."""
    citation = Citation(
        text="R.S.O. 1990, c. H.19",
        source="Ontario Human Rights Code",
        type="statute",
    )
    assert citation.text == "R.S.O. 1990, c. H.19"
    assert citation.source == "Ontario Human Rights Code"


def test_citation_checker_init() -> None:
    """Test citation checker initialization."""
    checker = CitationChecker()
    assert checker.config is not None


def test_extract_citations(sample_legal_text: str) -> None:
    """Test citation extraction."""
    checker = CitationChecker()
    citations = checker.extract_citations(sample_legal_text)
    assert isinstance(citations, list)


def test_check_citations(sample_legal_text: str, sample_citations: list[str]) -> None:
    """Test citation checking."""
    checker = CitationChecker()
    result = checker.check(sample_legal_text, sample_citations)
    assert hasattr(result, "is_valid")
    assert hasattr(result, "citations_found")
