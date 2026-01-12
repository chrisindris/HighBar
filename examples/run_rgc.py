"""Example: Running RGC task with custom configuration."""

from highbar.tasks import RegulatoryGroundingCheck, RGCInput
from highbar.utils import set_seed

# Set seed for reproducibility
set_seed(42)

# Initialize RGC task
rgc = RegulatoryGroundingCheck(
    model_name="llama-3",
    max_length=512,
    batch_size=8,
)

# Prepare input data
input_data = RGCInput(
    text="""
    The employer must provide reasonable accommodation for employees with
    disabilities, as required under the Ontario Human Rights Code, R.S.O. 1990, c. H.19.
    """,
    regulations=[
        "Ontario Human Rights Code, R.S.O. 1990, c. H.19",
        "Accessibility for Ontarians with Disabilities Act, 2005",
    ],
    context={
        "jurisdiction": "ontario",
        "domain": "employment_law",
    },
)

# Run task
output = rgc.run(input_data)

# Print results
print(f"Grounded: {output.grounded}")
print(f"Confidence: {output.confidence:.2f}")
print(f"Citations: {output.citations}")
if output.explanation:
    print(f"Explanation: {output.explanation}")
