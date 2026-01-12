"""Evaluation metrics for legal AI tasks."""

from highbar.metrics.gcp import GroundingCitationPrecision
from highbar.metrics.ac import AttributionCoverage
from highbar.metrics.hr import HallucinationRate
from highbar.metrics.fgs import FactualGroundingScore

__all__ = [
    "GroundingCitationPrecision",
    "AttributionCoverage",
    "HallucinationRate",
    "FactualGroundingScore",
]
