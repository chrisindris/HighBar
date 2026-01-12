"""Grounding Citation Precision (GCP) metric."""

from typing import Any, Dict, List

from pydantic import BaseModel


class GCPInput(BaseModel):
    """Input for GCP metric calculation."""

    generated_text: str
    citations: List[str]
    ground_truth_citations: List[str]
    context: Dict[str, Any] = {}


class GCPOutput(BaseModel):
    """Output from GCP metric calculation."""

    precision: float
    true_positives: int
    false_positives: int
    details: Dict[str, Any]


class GroundingCitationPrecision:
    """Calculate precision of grounding citations in legal text."""

    def __init__(self, **kwargs: Any) -> None:
        """Initialize GCP metric.

        Args:
            **kwargs: Additional configuration parameters
        """
        self.config = kwargs

    def compute(self, input_data: GCPInput) -> GCPOutput:
        """Compute GCP metric.

        Args:
            input_data: Input data for metric calculation

        Returns:
            GCPOutput with precision score
        """
        # Stub implementation
        return GCPOutput(
            precision=0.0,
            true_positives=0,
            false_positives=0,
            details={"note": "stub implementation"},
        )

    def batch_compute(self, inputs: List[GCPInput]) -> List[GCPOutput]:
        """Compute GCP metric on batch.

        Args:
            inputs: List of input data

        Returns:
            List of GCPOutput results
        """
        return [self.compute(input_data) for input_data in inputs]

    def aggregate(self, outputs: List[GCPOutput]) -> Dict[str, float]:
        """Aggregate GCP scores across multiple outputs.

        Args:
            outputs: List of GCP outputs

        Returns:
            Dictionary with aggregated metrics
        """
        if not outputs:
            return {"mean_precision": 0.0}

        precisions = [output.precision for output in outputs]
        return {
            "mean_precision": sum(precisions) / len(precisions),
            "min_precision": min(precisions),
            "max_precision": max(precisions),
        }
