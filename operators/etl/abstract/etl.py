from abc import abstractmethod
import typing
from abc import ABC
from data_cntrl.data_classes.model import Operation
from application.abstract.application import Context
from component_id.abstract.component_id import ComponentId
from data_cntrl.data_classes.model import Product


class Etl(ABC, ComponentId):
    """
        The Etl operators is an abstract operators with 3 functions:
        Execution of a mission on behalf of a principal resulting with an Etl operators
        Respond what products it can operate on potentially from as set of raw materials
        Respond what products it can effectively create from a set of raw materials, meaning all dependencies exist
    """

    def __init__(self, id: ComponentId):
        """
        :param id: ComponentId
        """
        self._id = id

    @abstractmethod
    def execute(self, principal: Context, mission: Product) -> Operation:
        """
        Execute a mission on behalf of a principal
        :param principal:
        :param mission:
        :return: Operation
        """
        pass

    @abstractmethod
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
    def ready_missions(self, ready_products: typing.Sequence[Product]) \
            -> typing.Sequence[Product]:
        """
        Returns Etl missions that it can form from the given raw materials
        :param ready_products:
        :return:  Sequence of Etl missions/products
        """
        pass
