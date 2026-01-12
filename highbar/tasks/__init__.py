"""Legal AI task modules for Ontario law."""

from highbar.tasks.rgc import RegulatoryGroundingCheck
from highbar.tasks.extract import EntityExtraction
from highbar.tasks.summc import SummaryCompletion
from highbar.tasks.claout import ClauseOutlining
from highbar.tasks.qar import QuestionAnsweringRetrieval

__all__ = [
    "RegulatoryGroundingCheck",
    "EntityExtraction",
    "SummaryCompletion",
    "ClauseOutlining",
    "QuestionAnsweringRetrieval",
]
