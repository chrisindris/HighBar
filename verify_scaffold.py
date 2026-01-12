#!/usr/bin/env python3
"""Verification script to check HighBar scaffold completeness."""

import sys
from pathlib import Path


def check_file_exists(path: str) -> bool:
    """Check if file exists."""
    return Path(path).exists()


def main() -> int:
    """Run verification checks."""
    print("🔍 Verifying HighBar scaffold...")
    print()

    checks = [
        # Core files
        ("pyproject.toml", "Project configuration"),
        ("README.md", "Documentation"),
        ("Dockerfile", "Docker support"),
        ("docker-compose.yml", "Docker Compose"),
        (".github/workflows/ci.yml", "CI/CD pipeline"),
        
        # Main package
        ("highbar/__init__.py", "Main package"),
        ("highbar/cli.py", "CLI interface"),
        ("highbar/config.py", "Configuration"),
        
        # Tasks
        ("highbar/tasks/rgc.py", "RGC task"),
        ("highbar/tasks/extract.py", "Entity extraction task"),
        ("highbar/tasks/summc.py", "Summary completion task"),
        ("highbar/tasks/claout.py", "Clause outlining task"),
        ("highbar/tasks/qar.py", "QA with retrieval task"),
        
        # Metrics
        ("highbar/metrics/gcp.py", "GCP metric"),
        ("highbar/metrics/ac.py", "AC metric"),
        ("highbar/metrics/hr.py", "HR metric"),
        ("highbar/metrics/fgs.py", "FGS metric"),
        
        # Ingest
        ("highbar/ingest/api.py", "API ingester"),
        ("highbar/ingest/hf.py", "HuggingFace ingester"),
        ("highbar/ingest/parquet.py", "Parquet ingester"),
        ("highbar/ingest/mcp.py", "MCP ingester"),
        
        # Rerank
        ("highbar/rerank/authority_ranker.py", "Authority ranker"),
        
        # Governance
        ("highbar/governance/bans.py", "Content bans"),
        ("highbar/governance/pii.py", "PII detector"),
        ("highbar/governance/license_gate.py", "License gate"),
        
        # Baselines
        ("highbar/baselines/rag.py", "RAG baseline"),
        ("highbar/baselines/encoder.py", "Encoder baseline"),
        ("highbar/baselines/seq2seq.py", "Seq2Seq baseline"),
        
        # Utils
        ("highbar/utils/citation.py", "Citation checker"),
        ("highbar/utils/authority.py", "Authority checker"),
        ("highbar/utils/snapshot.py", "Snapshot manifests"),
        ("highbar/utils/seed.py", "Seed control"),
        
        # Tests
        ("tests/conftest.py", "Test configuration"),
        ("tests/tasks/test_rgc.py", "RGC tests"),
        ("tests/metrics/test_gcp.py", "GCP tests"),
        ("tests/utils/test_citation.py", "Citation tests"),
        
        # Examples
        ("examples/run_rgc.py", "RGC example"),
        ("examples/run_rag_baseline.py", "RAG example"),
        ("examples/compute_metrics.py", "Metrics example"),
    ]
    
    passed = 0
    failed = 0
    
    for file_path, description in checks:
        if check_file_exists(file_path):
            print(f"✓ {description}: {file_path}")
            passed += 1
        else:
            print(f"✗ {description}: {file_path}")
            failed += 1
    
    print()
    print(f"Results: {passed}/{len(checks)} checks passed")
    
    if failed == 0:
        print("🎉 All checks passed! HighBar scaffold is complete.")
        return 0
    else:
        print(f"⚠️  {failed} checks failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
