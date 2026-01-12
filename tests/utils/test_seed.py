"""Tests for seed control utilities."""

import pytest

from highbar.utils.seed import set_seed, SeedContext


def test_set_seed() -> None:
    """Test set_seed function."""
    # Should not raise
    set_seed(42)
    set_seed(42, deterministic=True)
    set_seed(42, deterministic=False)


def test_seed_context() -> None:
    """Test SeedContext manager."""
    with SeedContext(42):
        # Inside context with seed 42
        pass
    # Outside context
