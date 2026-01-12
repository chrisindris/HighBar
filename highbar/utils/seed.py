"""Seed control for reproducibility."""

import random
from typing import Optional

import numpy as np


def set_seed(seed: int, deterministic: bool = True) -> None:
    """Set random seeds for reproducibility.

    Args:
        seed: Random seed value
        deterministic: Whether to use deterministic algorithms
    """
    random.seed(seed)
    np.random.seed(seed)

    try:
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed(seed)
            torch.cuda.manual_seed_all(seed)

        if deterministic:
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False
    except ImportError:
        pass  # PyTorch not available


def get_seed() -> Optional[int]:
    """Get current random seed if set.

    Returns:
        Current seed or None
    """
    # This is a simplified stub - in practice, retrieving the seed
    # after it's been set is non-trivial
    return None


class SeedContext:
    """Context manager for temporary seed changes."""

    def __init__(self, seed: int, deterministic: bool = True) -> None:
        """Initialize seed context.

        Args:
            seed: Temporary seed value
            deterministic: Whether to use deterministic algorithms
        """
        self.seed = seed
        self.deterministic = deterministic
        self.previous_seed: Optional[int] = None

    def __enter__(self) -> "SeedContext":
        """Enter context and set seed."""
        self.previous_seed = get_seed()
        set_seed(self.seed, self.deterministic)
        return self

    def __exit__(self, *args: object) -> None:
        """Exit context and restore previous seed."""
        if self.previous_seed is not None:
            set_seed(self.previous_seed, self.deterministic)
