"""Factual Grounding Score (FGS) metric."""

from typing import Any, Dict, List

from pydantic import BaseModel


class FGSInput(BaseModel):
    """Input for FGS metric calculation."""

    generated_text: str
    reference_text: str
    facts: List[str]
    context: Dict[str, Any] = {}


class FGSOutput(BaseModel):
    """Output from FGS metric calculation."""

    grounding_score: float
    grounded_facts: int
    total_facts: int
    ungrounded_facts: List[str]
    details: Dict[str, Any]


class FactualGroundingScore:
    """Calculate factual grounding score for generated legal text."""

    def __init__(self, **kwargs: Any) -> None:
        """Initialize FGS metric.

        Args:
            **kwargs: Additional configuration parameters
        """
        self.config = kwargs

    def compute(self, input_data: FGSInput) -> FGSOutput:
        """Compute FGS metric.

        Args:
            input_data: Input data for metric calculation

        Returns:
            FGSOutput with grounding score
        """
        # Stub implementation
        return FGSOutput(
            grounding_score=0.0,
            grounded_facts=0,
            total_facts=len(input_data.facts),
            ungrounded_facts=input_data.facts,
            details={"note": "stub implementation"},
        )

    def batch_compute(self, inputs: List[FGSInput]) -> List[FGSOutput]:
        """Compute FGS metric on batch.

        Args:
            inputs: List of input data

        Returns:
            List of FGSOutput results
        """
        return [self.compute(input_data) for input_data in inputs]

    def aggregate(self, outputs: List[FGSOutput]) -> Dict[str, float]:
        """Aggregate FGS scores across multiple outputs.

        Args:
            outputs: List of FGS outputs

        Returns:
            Dictionary with aggregated metrics
        """
        if not outputs:
            return {"mean_grounding_score": 0.0}

        scores = [output.grounding_score for output in outputs]
        return {
            "mean_grounding_score": sum(scores) / len(scores),
            "min_grounding_score": min(scores),
            "max_grounding_score": max(scores),
        }
