from typing import Final

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

from fractint.type_aliases import FractIntOrderSearchMethod, StationarityTest

__all__ = ["FractionalDifferencer"]


class FractionalDifferencer(BaseEstimator, TransformerMixin):

    def __init__(
            self,
            method: FractIntOrderSearchMethod = "bisection",
            bisection_conv: float = 1e-3,
            stat_test: StationarityTest = "ADF",
            significance_level: float = 0.01
    ):
        self._method: Final[FractIntOrderSearchMethod] = method
        self._d: float | None = None
        self._bisection_conv: float = bisection_conv

    def _validate_data(self, X: np.ndarray) -> None:
        if X.ndim != 2:
            raise ValueError
        if X.shape[1] != 1:
            raise ValueError
        if X.shape[0] <= 10:
            raise ValueError

    def _bisection_fract_int_order(
            self,
            X: np.ndarray,
            lower: float = 0,
            upper: float = 1
    ):
        if upper == 1:
            pass

    def _geweke_porter_hudak_fract_int_order(self):
        pass

    def fit(
            self,
            X: np.ndarray,
            y=None # noqa
    ):
        self._validate_data(X)
        if self._method == "bisection":
            self._bisection_fract_int_order(X)
        raise ValueError

    def transform(self, X, y=None):
        pass
