"""Test configuration and fixtures."""

import pytest


@pytest.fixture
def sample_legal_text() -> str:
    """Sample Ontario legal text for testing."""
    return """
    The Ontario Human Rights Code, R.S.O. 1990, c. H.19, prohibits discrimination
    based on protected grounds. Section 1 provides that every person has a right
    to equal treatment with respect to services, goods and facilities.
    """


@pytest.fixture
def sample_citations() -> list[str]:
    """Sample legal citations for testing."""
    return [
        "R.S.O. 1990, c. H.19",
        "Ontario Human Rights Code",
        "Section 1",
    ]


@pytest.fixture
def sample_documents() -> list[str]:
    """Sample legal documents for testing."""
    return [
        "The Criminal Code, R.S.C. 1985, c. C-46, outlines federal criminal law.",
        "The Ontario Rules of Civil Procedure govern civil litigation in Ontario.",
        "The Family Law Act, R.S.O. 1990, c. F.3, addresses family law matters.",
    ]
