"""Hallucination Rate (HR) metric."""

from typing import Any, Dict, List

from pydantic import BaseModel


class HRInput(BaseModel):
    """Input for HR metric calculation."""

    generated_text: str
    source_documents: List[str]
    statements: List[str]
    context: Dict[str, Any] = {}


class HROutput(BaseModel):
    """Output from HR metric calculation."""

    hallucination_rate: float
    hallucinated_statements: int
    total_statements: int
    hallucinations: List[str]
    details: Dict[str, Any]


class HallucinationRate:
    """Calculate rate of hallucinations in generated legal text."""

    def __init__(self, **kwargs: Any) -> None:
        """Initialize HR metric.

        Args:
            **kwargs: Additional configuration parameters
        """
        self.config = kwargs

    def compute(self, input_data: HRInput) -> HROutput:
        """Compute HR metric.

        Args:
            input_data: Input data for metric calculation

        Returns:
            HROutput with hallucination rate
        """
        # Stub implementation
        return HROutput(
            hallucination_rate=0.0,
            hallucinated_statements=0,
            total_statements=len(input_data.statements),
            hallucinations=[],
            details={"note": "stub implementation"},
        )

    def batch_compute(self, inputs: List[HRInput]) -> List[HROutput]:
        """Compute HR metric on batch.

        Args:
            inputs: List of input data

        Returns:
            List of HROutput results
        """
        return [self.compute(input_data) for input_data in inputs]

    def aggregate(self, outputs: List[HROutput]) -> Dict[str, float]:
        """Aggregate HR scores across multiple outputs.

        Args:
            outputs: List of HR outputs

        Returns:
            Dictionary with aggregated metrics
        """
        if not outputs:
            return {"mean_hallucination_rate": 0.0}

        rates = [output.hallucination_rate for output in outputs]
        return {
            "mean_hallucination_rate": sum(rates) / len(rates),
            "min_hallucination_rate": min(rates),
            "max_hallucination_rate": max(rates),
        }
