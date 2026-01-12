"""Example: Computing metrics on task outputs."""

from highbar.metrics import GroundingCitationPrecision, GCPInput
from highbar.metrics import HallucinationRate, HRInput

# Example 1: Grounding Citation Precision
gcp = GroundingCitationPrecision()

gcp_input = GCPInput(
    generated_text="According to R.S.O. 1990, c. H.19, discrimination is prohibited.",
    citations=["R.S.O. 1990, c. H.19", "Section 1"],
    ground_truth_citations=["R.S.O. 1990, c. H.19", "Section 1", "Section 7"],
)

gcp_output = gcp.compute(gcp_input)
print(f"GCP Precision: {gcp_output.precision:.2f}")
print(f"True Positives: {gcp_output.true_positives}")
print(f"False Positives: {gcp_output.false_positives}")

# Example 2: Hallucination Rate
hr = HallucinationRate()

hr_input = HRInput(
    generated_text="The law requires immediate action within 24 hours.",
    source_documents=[
        "The legislation suggests action within a reasonable timeframe.",
    ],
    statements=[
        "The law requires immediate action",
        "Action must be taken within 24 hours",
    ],
)

hr_output = hr.compute(hr_input)
print(f"\nHallucination Rate: {hr_output.hallucination_rate:.2f}")
print(f"Hallucinated: {hr_output.hallucinated_statements}/{hr_output.total_statements}")
print(f"Hallucinations: {hr_output.hallucinations}")

# Example 3: Batch processing and aggregation
batch_inputs = [gcp_input, gcp_input]  # Duplicate for example
batch_outputs = gcp.batch_compute(batch_inputs)

aggregated = gcp.aggregate(batch_outputs)
print(f"\nAggregated GCP:")
print(f"Mean Precision: {aggregated['mean_precision']:.2f}")
print(f"Min Precision: {aggregated['min_precision']:.2f}")
print(f"Max Precision: {aggregated['max_precision']:.2f}")
