from abc import ABC, abstractmethod
from typing import final, Final
import string


@final
class ProductWrapper(ABC):
    def __init__(self, etl: string, name: string, partition: string):
        self._etl: Final[str] = etl
        self._name: Final[str] = name
        self._partition: Final[str] = partition

    @property
    def etl(self):
        return self._etl

    @property
    def name(self):
        return self._name

    @property
    def partition(self):
        return self._partition

