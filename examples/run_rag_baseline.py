"""Example: Using RAG baseline for legal QA."""

from highbar.baselines import RAGBaseline, RAGConfig, RAGInput
from highbar.utils import set_seed

# Set seed for reproducibility
set_seed(42)

# Configure RAG baseline
config = RAGConfig(
    retriever_model="sentence-transformers/all-MiniLM-L6-v2",
    generator_model="gpt2",
    top_k=3,
)

# Initialize baseline
rag = RAGBaseline(config)

# Prepare input
documents = [
    "The Criminal Code, R.S.C. 1985, c. C-46, outlines federal criminal law in Canada.",
    "The Ontario Highway Traffic Act governs road safety and traffic regulations.",
    "The Family Law Act, R.S.O. 1990, c. F.3, addresses family law matters in Ontario.",
]

input_data = RAGInput(
    query="What legislation governs family law in Ontario?",
    documents=documents,
    context={"jurisdiction": "ontario"},
)

# Run baseline
output = rag.run(input_data)

# Print results
print(f"Generated Answer: {output.generated_text}")
print(f"\nRetrieved Documents:")
for i, (doc, score) in enumerate(zip(output.retrieved_docs, output.retrieval_scores), 1):
    print(f"{i}. Score: {score:.2f}")
    print(f"   {doc[:100]}...")
