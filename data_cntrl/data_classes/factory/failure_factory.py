from data_cntrl.data_classes.model.failure import Failure
from typing import Sequence


def create_failure(category: str, details: Sequence[str] = []) -> Failure:
    return Failure(category= category, details=details)

