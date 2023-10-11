from abc import ABC, abstractmethod
from typing import final, Final, Sequence
import string
from etl.etl_operator import ETLOperator
from etl.etl_operation import ETLOperation


@final
class Product(ABC):
    """
       A product has name and partition and may have also source materials,
       yet it is not the source materials that drives our decision to create a product,
       but the very operations that had created them. Also notice that externally coming products
       will not have source raw materials.
       We also write down the etl_operator doing to job as it is part of the very product identification
    """
    def __init__(self, etl_operator: ETLOperator, name: string, partition: string,
                 source_operations: Sequence[ETLOperation] = None):
        self._etl_operator= etl_operator
        self._name: Final[str] = name
        self._partition: Final[str] = partition
        self._source_operations = source_operations

    @property
    def etl_operator(self):
        return self._etl_operator

    @property
    def name(self):
        return self._name

    @property
    def partition(self):
        return self._partitio
    @property
    def source_operations(self):
        return self._source_operations
