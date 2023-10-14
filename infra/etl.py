from abc import abstractmethod
import typing
import string
from abc import ABC
from operation import Operation
from infra.principal import Principal
from infra.operator import Operator
from product import Product


class ETL(ABC, Operator):
    """
        The ETL operator is an abstract operator with 3 functions:
        Execution of a mission on behalf of a principal resulting with an ETL operation
        Respond what products is can operate on potentially from as set of raw materials
        Respond what products it can effectively create from a set of raw materials, meaning all dependencies exist
    """

    def __init__(self, name: string,
                 version_number: string = None,
                 version_description: string = None):
        """
        This is to create the
        :param name:
        :param version_number: version number
        :param version_description:
        """
        super().__init__(name, version_number, version_description)

    @abstractmethod
    def execute(self, principal: Principal, mission: Product) -> Operation:
        """
        Execute a mission on behalf of a principal
        :param principal:
        :param mission:
        :return: Operation
        """

        pass

    @abstractmethod
    def get_raw_materials_it_can_use_potentially(self,
                                                 ready_raw_materials: typing.Sequence[Product]) -> (
            typing.Sequence)[Product]:
        """
        Return all raw materials it can use potentially. Potentially and not effectively
        means that it may require other raw materials not provided.
        :param ready_raw_materials:
        :return: Sequence of ETL missions
        """
        pass

    @abstractmethod
    def create_missions_from_raw_materials(self, ready_products: typing.Sequence[Product]) \
            -> typing.Sequence[Product]:
        """
        Returns ETL missions that it can form from the given raw materials
        :param ready_products:
        :return:  Sequence of ETL missions
        """
        pass