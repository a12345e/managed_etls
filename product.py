from abc import ABC
from typing import final, Final, Sequence
import string
from operator import Operator
from operation import Operation
from product_name import ProductName


@final
class Product(ABC):
    """
       The product is a relation/predicate namely the Operator, between source materials materialized
       by previous operations and the product name standing for the outcome
    """
    def __init__(self, operator: Operator,
                 product_name: ProductName,
                 source_operations: Sequence[Operation] = None):
        self._etl_operator = operator
        self._name: Final[ProductName] = product_name
        self._source_operations = source_operations

    @property
    def operator(self):
        return self._operator

    @property
    def product_name(self):
        return self._product_name

    @property
    def source_operations(self):
        return self._source_operations
