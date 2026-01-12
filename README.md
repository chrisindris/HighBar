# HighBar

**HighBar: An LLM Benchmark for Ontario Law**

A comprehensive benchmark suite for evaluating Large Language Models on Ontario legal tasks, including regulatory grounding, entity extraction, summarization, clause outlining, and question answering.

## Features

- **🎯 Five Legal Tasks**: RGC (Regulatory Grounding Check), Entity Extraction, Summary Completion, Clause Outlining, and Question Answering with Retrieval
- **📊 Four Metrics**: Grounding Citation Precision (GCP), Attribution Coverage (AC), Hallucination Rate (HR), and Factual Grounding Score (FGS)
- **📥 Multiple Ingest Sources**: API, HuggingFace, Parquet, and MCP (Model Context Protocol)
- **🔄 Authority-Based Reranking**: Legal document retrieval with citation authority
- **🛡️ Governance Modules**: Content bans, PII detection, and license gating
- **🎨 Baseline Models**: RAG, Encoder, and Seq2Seq baselines
- **🔧 CLI Interface**: Typer-based command-line interface
- **🐳 Docker Support**: Containerized deployment
- **✅ CI/CD**: GitHub Actions integration

## Installation

### Using Poetry (recommended)

```bash
# Clone the repository
git clone https://github.com/chrisindris/HighBar.git
cd HighBar

# Install with Poetry
poetry install

# Activate the virtual environment
poetry shell
```

### Using pip

```bash
pip install -e .
```

### Using Docker

```bash
# Build the image
docker build -t highbar .

# Run with Docker Compose
docker-compose up highbar
```

## Quick Start

### Command-Line Interface

HighBar provides a Typer-based CLI with four main commands:

```bash
# Show help
highbar --help

# Ingest data
highbar ingest hf --input "legal/ontario-cases" --output ./data

# Run evaluation tasks
highbar run rgc --model llama-3 --data ./data --output ./results

# Score model outputs
highbar score ./results --metrics gcp,hr --output ./scores

# Generate reports
highbar report ./scores --format table
```

### Python API

```python
from highbar.tasks import RegulatoryGroundingCheck, RGCInput
from highbar.metrics import GroundingCitationPrecision, GCPInput
from highbar.utils import set_seed

# Set random seed for reproducibility
set_seed(42)

# Run a task
rgc = RegulatoryGroundingCheck(model_name="llama-3")
input_data = RGCInput(
    text="Legal text to evaluate...",
    regulations=["R.S.O. 1990, c. H.19"],
)
output = rgc.run(input_data)

# Compute metrics
gcp = GroundingCitationPrecision()
metric_input = GCPInput(
    generated_text=output.explanation or "",
    citations=output.citations,
    ground_truth_citations=["R.S.O. 1990, c. H.19"],
)
score = gcp.compute(metric_input)
print(f"GCP Score: {score.precision}")
```

## Project Structure

```
highbar/
├── tasks/              # Legal AI tasks
│   ├── rgc.py         # Regulatory Grounding Check
│   ├── extract.py     # Entity Extraction
│   ├── summc.py       # Summary Completion
│   ├── claout.py      # Clause Outlining
│   └── qar.py         # Question Answering with Retrieval
├── metrics/           # Evaluation metrics
│   ├── gcp.py        # Grounding Citation Precision
│   ├── ac.py         # Attribution Coverage
│   ├── hr.py         # Hallucination Rate
│   └── fgs.py        # Factual Grounding Score
├── ingest/           # Data ingestion
│   ├── api.py        # API ingestion
│   ├── hf.py         # HuggingFace datasets
│   ├── parquet.py    # Parquet files
│   └── mcp.py        # Model Context Protocol
├── rerank/           # Document reranking
│   └── authority_ranker.py
├── governance/       # Compliance and governance
│   ├── bans.py       # Content ban checker
│   ├── pii.py        # PII detector
│   └── license_gate.py
├── baselines/        # Baseline models
│   ├── rag.py        # RAG baseline
│   ├── encoder.py    # Encoder baseline
│   └── seq2seq.py    # Seq2Seq baseline
├── utils/            # Utilities
│   ├── citation.py   # Citation checker
│   ├── authority.py  # Authority checker
│   ├── snapshot.py   # Snapshot manifests
│   └── seed.py       # Seed control
└── cli.py            # Command-line interface
```

## Development

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=highbar --cov-report=html

# Run specific test file
poetry run pytest tests/tasks/test_rgc.py
```

### Linting and Formatting

```bash
# Run ruff linter
poetry run ruff check highbar tests

# Format with black
poetry run black highbar tests

# Type checking with mypy
poetry run mypy highbar
```

### Building Documentation

```bash
# Install documentation dependencies
poetry install --with docs

# Build docs (if configured)
cd docs
make html
```

## Reproducibility

HighBar includes seed control utilities for reproducible experiments:

```python
from highbar.utils import set_seed

# Set seed for all random number generators
set_seed(42, deterministic=True)

# Use context manager for temporary seed
from highbar.utils.seed import SeedContext

with SeedContext(123):
    # Code with seed 123
    pass
# Previous seed restored
```

## Citation

If you use HighBar in your research, please cite:

```bibtex
@software{highbar2026,
  title={HighBar: An LLM Benchmark for Ontario Law},
  author={Indris, Christopher},
  year={2026},
  url={https://github.com/chrisindris/HighBar}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built with PyTorch, HuggingFace Transformers, and LLaMA-Factory
- Designed for Ontario legal AI research and evaluation
