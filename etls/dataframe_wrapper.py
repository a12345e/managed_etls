from abc import ABC, abstractmethod
import string
import typing
from product import Product


class DataFrameWrapper(ABC):
    def __int__(self, product: Product):
        self._product = product
        pass

    @abstractmethod
    def get(self) -> typing.Any:
        pass
