from abc import abstractmethod
import typing
from abc import ABC
import pydantic
from data_cntrl.data_classes.model.component_id import ComponentId
from data_cntrl.data_classes.model.product import Product
from data_cntrl.data_classes.model.operation import Operation


class Etl(ABC, pydantic.BaseModel):
    """
        The Etl functions is an abstract functions with 3 functions:
        Execution of a mission on behalf of a principal resulting with an Etl functions
        Respond what products it can operate on potentially from as set of raw materials
        Respond what products it can effectively create from a set of raw materials, meaning all dependencies exist
    """
    id: ComponentId

    @abstractmethod
    def execute(self, operation: Operation) -> Operation:
        """
        Execute a mission on behalf of a principal
        :param operation:
        :return: Operation
        """
        pass

    @abstractmethod
    @classmethod
    def usable_products(self, ready_raw_materials: typing.Sequence[Product]) -> (
            typing.Sequence)[Product]:
        """
        Return all raw materials it can use potentially. Potentially and not effectively
        means that it may require other raw materials not provided.
        :param ready_raw_materials:
        :return: Sequence of Etl missions
        """
        pass

    @abstractmethod
    def get_ready_to_produce(self, ready_products: typing.Sequence[Product]) \
            -> typing.Sequence[Product]:
        """
        Returns Etl missions that it can form from the given raw materials
        :param ready_products:
        :return:  Sequence of Etl missions/products
        """
        pass
