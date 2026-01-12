"""Tests for RGC task."""

import pytest

from highbar.tasks.rgc import RegulatoryGroundingCheck, RGCInput, RGCOutput


def test_rgc_init() -> None:
    """Test RGC initialization."""
    rgc = RegulatoryGroundingCheck(model_name="test-model")
    assert rgc.model_name == "test-model"


def test_rgc_run(sample_legal_text: str, sample_citations: list[str]) -> None:
    """Test RGC run method."""
    rgc = RegulatoryGroundingCheck()
    input_data = RGCInput(text=sample_legal_text, regulations=sample_citations)
    output = rgc.run(input_data)

    assert isinstance(output, RGCOutput)
    assert isinstance(output.grounded, bool)
    assert isinstance(output.citations, list)
    assert isinstance(output.confidence, float)


def test_rgc_batch_run(sample_legal_text: str, sample_citations: list[str]) -> None:
    """Test RGC batch run method."""
    rgc = RegulatoryGroundingCheck()
    inputs = [
        RGCInput(text=sample_legal_text, regulations=sample_citations),
        RGCInput(text=sample_legal_text, regulations=sample_citations),
    ]
    outputs = rgc.batch_run(inputs)

    assert len(outputs) == 2
    assert all(isinstance(o, RGCOutput) for o in outputs)
