from abc import ABC, abstractmethod
from typing import final, Final
import string


@final
class Product(ABC):
    def __init__(self, name: string, partition: string):
        self._name: Final[str] = name
        self._partition: Final[str] = partition

    @property
    def name(self):
        return self._name

    @property
    def partition(self):
        return self._partition

