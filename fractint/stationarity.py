import numpy as np

from .type_aliases import StationarityTest

__all__ = ["is_stationary"]


def is_stationary(
        X: np.ndarray,
        stat_test: StationarityTest = "ADF",
        significance_level: float = 0.01
) -> bool:
    pass
