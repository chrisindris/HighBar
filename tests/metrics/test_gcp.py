"""Tests for GCP metric."""

import pytest

from highbar.metrics.gcp import GroundingCitationPrecision, GCPInput, GCPOutput


def test_gcp_init() -> None:
    """Test GCP initialization."""
    gcp = GroundingCitationPrecision()
    assert gcp.config is not None


def test_gcp_compute(sample_legal_text: str, sample_citations: list[str]) -> None:
    """Test GCP compute method."""
    gcp = GroundingCitationPrecision()
    input_data = GCPInput(
        generated_text=sample_legal_text,
        citations=sample_citations,
        ground_truth_citations=sample_citations,
    )
    output = gcp.compute(input_data)

    assert isinstance(output, GCPOutput)
    assert isinstance(output.precision, float)
    assert 0.0 <= output.precision <= 1.0


def test_gcp_aggregate() -> None:
    """Test GCP aggregate method."""
    gcp = GroundingCitationPrecision()
    outputs = [
        GCPOutput(precision=0.8, true_positives=4, false_positives=1, details={}),
        GCPOutput(precision=0.9, true_positives=9, false_positives=1, details={}),
    ]
    aggregated = gcp.aggregate(outputs)

    assert "mean_precision" in aggregated
    assert "min_precision" in aggregated
    assert "max_precision" in aggregated
