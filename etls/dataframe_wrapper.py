from abc import ABC, abstractmethod
import string
import typing
from product_wrapper import ProductWrapper


class DataFrameWrapper(ABC):
    def __int__(self, product: ProductWrapper):
        self._product = product
        pass

    @abstractmethod
    def get(self) -> typing.Any:
        pass
