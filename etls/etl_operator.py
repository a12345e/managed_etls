from abc import ABC, abstractmethod
import string
import typing
from dataframe_wrapper import DataFrameWrapper
from product_wrapper import ProductWrapper


class ETLOperator(ABC):

    def __init__(self, product: ProductWrapper):
        self._product = product
        pass

    @abstractmethod
    @property
    def etl(self):
        pass

    @abstractmethod
    def extract(self) -> dict[string, DataFrameWrapper]:
        pass

    @abstractmethod
    def transform(self, dataframes_map: dict[string, DataFrameWrapper]) -> DataFrameWrapper:
        pass

    @abstractmethod
    def load(self, dataframe: DataFrameWrapper) -> string:
        pass

    @abstractmethod
    def get_create_potential_products(self, ready_products: typing.Sequence[ProductWrapper]) \
            -> typing.Sequence[ProductWrapper]:
        pass

    @abstractmethod
    def get_create_ready_products(self, ready_products: typing.Sequence[ProductWrapper]) \
            -> typing.Sequence[ProductWrapper]:
        pass


