from abc import ABC
from typing import final
import string
from infra.abstracts.operator.operator import Operator


@final
class Product(ABC):
    """
       The product is a tuple (operator, name, and batch)
    """
    def __init__(self, operator: Operator,
                 name: string,
                 batch: string):
        self._etl_operator = operator
        self._name = name
        self._batch = batch

    @property
    def operator(self):
        return self._operator

    @property
    def name(self):
        return self._name

    @property
    def _batch(self):
        return self._batch
