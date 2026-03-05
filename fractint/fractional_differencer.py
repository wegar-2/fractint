from typing import Final

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from fractint.type_aliases import FractIntOrderSearchMethod


class FractionalDifferencer(BaseEstimator, TransformerMixin):

    def __init__(
            self,
            method: FractIntOrderSearchMethod = "bisection"
    ):
        self._method: Final[FractIntOrderSearchMethod] = method
        self._d: float | None = None

    def _validate_data(self, X):
        pass

    def _bisection_fract_int_order(
            self
    ):
        pass

    def _geweke_porter_hudak_fract_int_order(self):
        pass

    def fit(
            self,
            X: np.ndarray,
            y=None
    ):
        pass

    def transform(self, X, y=None):
        pass
