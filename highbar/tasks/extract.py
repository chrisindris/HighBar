"""Entity Extraction task for legal documents."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class ExtractInput(BaseModel):
    """Input for Entity Extraction task."""

    text: str
    entity_types: List[str]
    context: Optional[Dict[str, Any]] = None


class Entity(BaseModel):
    """Extracted entity."""

    text: str
    type: str
    start: int
    end: int
    confidence: float


class ExtractOutput(BaseModel):
    """Output from Entity Extraction task."""

    entities: List[Entity]
    raw_text: str


class EntityExtraction:
    """Extract legal entities from Ontario legal documents."""

    def __init__(self, model_name: str = "default", **kwargs: Any) -> None:
        """Initialize the entity extraction task.

        Args:
            model_name: Name of the model to use
            **kwargs: Additional configuration parameters
        """
        self.model_name = model_name
        self.config = kwargs

    def run(self, input_data: ExtractInput) -> ExtractOutput:
        """Run entity extraction.

        Args:
            input_data: Input data for the task

        Returns:
            ExtractOutput with extracted entities
        """
        # Stub implementation
        return ExtractOutput(entities=[], raw_text=input_data.text)

    def batch_run(self, inputs: List[ExtractInput]) -> List[ExtractOutput]:
        """Run entity extraction on batch.

        Args:
            inputs: List of input data

        Returns:
            List of ExtractOutput results
        """
        return [self.run(input_data) for input_data in inputs]
