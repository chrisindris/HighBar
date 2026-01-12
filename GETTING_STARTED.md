# Getting Started with HighBar

This guide will help you get started with the HighBar Ontario legal AI benchmark.

## Installation

### Prerequisites

- Python 3.10 or higher
- Poetry (for dependency management)

### Step 1: Clone the Repository

```bash
git clone https://github.com/chrisindris/HighBar.git
cd HighBar
```

### Step 2: Install Dependencies

```bash
# Install Poetry if you haven't already
pip install poetry

# Install project dependencies
poetry install

# Activate the virtual environment
poetry shell
```

### Step 3: Verify Installation

```bash
# Run the verification script
python verify_scaffold.py

# Check the CLI
highbar --help
```

## Quick Start

### 1. Running a Task

```bash
# Run the RGC (Regulatory Grounding Check) task
highbar run rgc --model llama-3 --data ./data --output ./results

# Run with a specific seed for reproducibility
highbar run rgc --model llama-3 --seed 42
```

### 2. Using Python API

Create a Python script:

```python
from highbar.tasks import RegulatoryGroundingCheck, RGCInput
from highbar.utils import set_seed

# Set seed for reproducibility
set_seed(42)

# Initialize task
rgc = RegulatoryGroundingCheck(model_name="llama-3")

# Prepare input
input_data = RGCInput(
    text="The employer must provide reasonable accommodation...",
    regulations=["R.S.O. 1990, c. H.19"],
)

# Run task
output = rgc.run(input_data)
print(f"Grounded: {output.grounded}")
print(f"Citations: {output.citations}")
```

### 3. Computing Metrics

```python
from highbar.metrics import GroundingCitationPrecision, GCPInput

gcp = GroundingCitationPrecision()

input_data = GCPInput(
    generated_text="According to R.S.O. 1990, c. H.19...",
    citations=["R.S.O. 1990, c. H.19"],
    ground_truth_citations=["R.S.O. 1990, c. H.19", "Section 1"],
)

output = gcp.compute(input_data)
print(f"Precision: {output.precision:.2f}")
```

### 4. Data Ingestion

```bash
# Ingest from HuggingFace
highbar ingest hf --input "legal/ontario-cases" --output ./data

# Ingest from Parquet file
highbar ingest parquet --input cases.parquet --output ./data

# Ingest from API
highbar ingest api --input "https://api.example.com" --config api_config.yaml
```

## Project Structure

```
highbar/
├── tasks/              # Legal AI tasks
│   ├── rgc.py         # Regulatory Grounding Check
│   ├── extract.py     # Entity Extraction
│   ├── summc.py       # Summary Completion
│   ├── claout.py      # Clause Outlining
│   └── qar.py         # Question Answering
├── metrics/           # Evaluation metrics
├── ingest/            # Data ingestion
├── baselines/         # Baseline models
├── governance/        # Compliance modules
└── utils/             # Utility functions
```

## Configuration

Copy the example configuration:

```bash
cp config.example.yaml config.yaml
```

Edit `config.yaml` to customize:
- Model names and parameters
- Task configurations
- Metric thresholds
- Governance settings

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=highbar --cov-report=html

# Run specific test file
pytest tests/tasks/test_rgc.py
```

## Development

### Code Style

```bash
# Format code
black highbar tests

# Lint code
ruff check highbar tests

# Type check
mypy highbar
```

### Adding a New Task

1. Create a new file in `highbar/tasks/`
2. Define input/output Pydantic models
3. Implement the task class with `run()` and `batch_run()` methods
4. Add imports to `highbar/tasks/__init__.py`
5. Add tests in `tests/tasks/`
6. Update CLI in `highbar/cli.py` if needed

### Adding a New Metric

1. Create a new file in `highbar/metrics/`
2. Define input/output Pydantic models
3. Implement the metric class with `compute()`, `batch_compute()`, and `aggregate()` methods
4. Add imports to `highbar/metrics/__init__.py`
5. Add tests in `tests/metrics/`

## Docker Usage

### Build and Run

```bash
# Build the image
docker build -t highbar .

# Run a command
docker run highbar --help

# Use docker-compose for development
docker-compose up highbar-dev
```

### With Volumes

```bash
# Mount local data directory
docker run -v $(pwd)/data:/app/data highbar ingest hf --input "legal/ontario-cases"
```

## Examples

Check the `examples/` directory for more usage examples:

- `examples/run_rgc.py` - Running the RGC task
- `examples/run_rag_baseline.py` - Using RAG baseline
- `examples/compute_metrics.py` - Computing metrics

Run an example:

```bash
python examples/run_rgc.py
```

## Troubleshooting

### Import Errors

If you get import errors, make sure you've installed the package:

```bash
poetry install
```

### Poetry Not Found

Install Poetry:

```bash
pip install poetry
# or
curl -sSL https://install.python-poetry.org | python3 -
```

### CUDA/GPU Issues

If you want to use CPU only:

```python
# In your code
import torch
torch.set_default_device('cpu')
```

Or set in config.yaml:

```yaml
general:
  device: "cpu"
```

## Next Steps

1. **Implement Models**: Replace stub implementations with actual models
2. **Add Data**: Integrate real Ontario legal datasets
3. **Run Benchmarks**: Evaluate models on the tasks
4. **Contribute**: See CONTRIBUTING.md for guidelines

## Resources

- **Repository**: https://github.com/chrisindris/HighBar
- **Documentation**: See README.md
- **Issues**: https://github.com/chrisindris/HighBar/issues
- **Discussions**: https://github.com/chrisindris/HighBar/discussions

## Support

If you encounter any issues or have questions:

1. Check the README.md and this guide
2. Search existing issues on GitHub
3. Open a new issue with details about your problem

---

Happy benchmarking! 🚀
