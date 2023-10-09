from abc import ABC, abstractmethod
import string
import typing
from etls.dataframe_wrapper import DataFrameWrapper
from etls.product import Product
from etls.operator_identity import OperatorIdentity


class ETLOperator(ABC):
    def __init__(self,
                 identity: OperatorIdentity):
        self._name: typing.Final[OperatorIdentity] = identity

    @property
    def identity(self):
        return self._identity

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
    def get_products_partially_ready_for_creation(self, ready_products: typing.Sequence[Product]) \
            -> typing.Sequence[Product]:
        """
        Will see all products that at least one required product for their creation is redy for use.
        :param ready_products:
        :return: Sequence of ProductWrapper objects
        """
        pass

    @abstractmethod
    def get_products_ready_to_be_created_now(self, ready_products: typing.Sequence[Product]) \
            -> typing.Sequence[Product]:
        """
        Returns products that can now be created.
        :param ready_products:
        :return:  Sequence of ProductWrapper objects
        """
        pass


