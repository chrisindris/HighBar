"""Command-line interface for HighBar benchmark."""

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from highbar import __version__

app = typer.Typer(
    name="highbar",
    help="HighBar: An LLM Benchmark for Ontario Law",
    add_completion=False,
)
console = Console()


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        console.print(f"HighBar version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit.",
    ),
) -> None:
    """HighBar: An LLM Benchmark for Ontario Law."""
    pass


@app.command()
def ingest(
    source: str = typer.Argument(..., help="Data source type (api/hf/parquet/mcp)"),
    input_path: str = typer.Option(..., "--input", "-i", help="Input path or identifier"),
    output_path: str = typer.Option("./data", "--output", "-o", help="Output directory"),
    config_file: Optional[Path] = typer.Option(None, "--config", "-c", help="Config file"),
) -> None:
    """Ingest legal documents from various sources.

    Examples:
        highbar ingest hf --input "legal/ontario-cases" --output ./data
        highbar ingest parquet --input cases.parquet --output ./data
        highbar ingest api --input "https://api.example.com" --config api_config.yaml
    """
    console.print(f"[bold blue]Ingesting data from {source}...[/bold blue]")
    console.print(f"Input: {input_path}")
    console.print(f"Output: {output_path}")

    if config_file:
        console.print(f"Config: {config_file}")

    # Stub implementation
    console.print("[green]✓[/green] Ingestion completed (stub)")


@app.command()
def run(
    task: str = typer.Argument(..., help="Task to run (rgc/extract/summc/claout/qar)"),
    model: str = typer.Option("default", "--model", "-m", help="Model to use"),
    data_path: Path = typer.Option("./data", "--data", "-d", help="Data directory"),
    output_path: Path = typer.Option("./results", "--output", "-o", help="Output directory"),
    baseline: Optional[str] = typer.Option(None, "--baseline", "-b", help="Baseline (rag/encoder/seq2seq)"),
    seed: int = typer.Option(42, "--seed", "-s", help="Random seed"),
    batch_size: int = typer.Option(8, "--batch-size", help="Batch size"),
) -> None:
    """Run evaluation tasks on legal AI models.

    Examples:
        highbar run rgc --model llama-3 --data ./data --output ./results
        highbar run qar --baseline rag --data ./data
        highbar run extract --model gpt-4 --seed 42
    """
    console.print(f"[bold blue]Running task: {task}[/bold blue]")
    console.print(f"Model: {model}")
    console.print(f"Data: {data_path}")
    console.print(f"Output: {output_path}")
    console.print(f"Seed: {seed}")

    if baseline:
        console.print(f"Baseline: {baseline}")

    # Stub implementation
    from highbar.utils.seed import set_seed
    set_seed(seed)

    console.print("[green]✓[/green] Task execution completed (stub)")


@app.command()
def score(
    results_path: Path = typer.Argument(..., help="Path to results directory"),
    metrics: Optional[str] = typer.Option(None, "--metrics", "-m", help="Comma-separated metrics (gcp,ac,hr,fgs)"),
    output_path: Path = typer.Option("./scores", "--output", "-o", help="Output directory"),
    reference_path: Optional[Path] = typer.Option(None, "--reference", "-r", help="Reference data path"),
) -> None:
    """Score model outputs using evaluation metrics.

    Examples:
        highbar score ./results --metrics gcp,hr --output ./scores
        highbar score ./results --reference ./ground_truth --metrics all
    """
    console.print(f"[bold blue]Scoring results...[/bold blue]")
    console.print(f"Results: {results_path}")
    console.print(f"Output: {output_path}")

    if metrics:
        console.print(f"Metrics: {metrics}")
    else:
        console.print("Metrics: all")

    if reference_path:
        console.print(f"Reference: {reference_path}")

    # Stub implementation
    console.print("[green]✓[/green] Scoring completed (stub)")


@app.command()
def report(
    scores_path: Path = typer.Argument(..., help="Path to scores directory"),
    format: str = typer.Option("table", "--format", "-f", help="Output format (table/json/html)"),
    output_file: Optional[Path] = typer.Option(None, "--output", "-o", help="Output file"),
    compare: Optional[Path] = typer.Option(None, "--compare", "-c", help="Compare with baseline"),
) -> None:
    """Generate evaluation reports.

    Examples:
        highbar report ./scores --format table
        highbar report ./scores --format json --output report.json
        highbar report ./scores --compare ./baseline_scores
    """
    console.print(f"[bold blue]Generating report...[/bold blue]")
    console.print(f"Scores: {scores_path}")
    console.print(f"Format: {format}")

    if output_file:
        console.print(f"Output: {output_file}")

    if compare:
        console.print(f"Comparing with: {compare}")

    # Stub implementation - show example table
    table = Table(title="HighBar Evaluation Results (Example)")
    table.add_column("Task", style="cyan")
    table.add_column("Model", style="magenta")
    table.add_column("GCP", justify="right")
    table.add_column("AC", justify="right")
    table.add_column("HR", justify="right")
    table.add_column("FGS", justify="right")

    table.add_row("rgc", "llama-3", "0.85", "0.78", "0.12", "0.82")
    table.add_row("qar", "gpt-4", "0.92", "0.88", "0.08", "0.90")
    table.add_row("summc", "claude-3", "0.88", "0.85", "0.10", "0.87")

    console.print(table)
    console.print("[green]✓[/green] Report generated (stub)")


if __name__ == "__main__":
    app()
