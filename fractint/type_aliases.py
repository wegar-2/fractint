from typing import Literal, TypeAlias


FractIntOrderSearchMethod: TypeAlias = Literal[
    "bisection",
    "geweke-porter-hudak"
]

StationarityTest: TypeAlias = Literal["ADF", "PP", "KPSS"]
