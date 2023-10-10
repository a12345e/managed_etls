from abc import ABC, abstractmethod
import string
import typing
from etls.dataframe_wrapper import DataFrameWrapper
from etls.product import Product
from etls.operator_identity import OperatorIdentity
from etls.etl_mission import ETLMission


class ETLOperator(ABC):
    """
    So what is the ETLOperator?
    This is an operator/tool that,
      1. Has identity
      2. Can execute a mission of which it is a tool/operator for doing
      3. Can say what raw materials it can potentially use
      4. Can say what mission it can build from given raw materials

      The set of raw in those missions are a subset of the raw materials it can use


    """
    def __init__(self,
                 identity: OperatorIdentity):
        self._name: typing.Final[OperatorIdentity] = identity
    @property
    def identity(self):
        return self._identity
    @abstractmethod
    def execute(self, mission: ETLMission):
        pass
    @abstractmethod
    def get_raw_materials_it_can_use_potentially(self,
            ready_raw_materials: typing.Sequence[Product]) -> typing.Sequence[Product]:
        """
        Return all raw materials it can use potentially. Potentially and not effectively
        means that it may require other raw materials not given.
        :param ready_raw_materials:
        :return: Sequence of ETL missions
        """
        pass
    @abstractmethod
    def create_missions_from_raw_materials(self, ready_products: typing.Sequence[Product]) \
            -> typing.Sequence[ETLMission]:
        """
        Returns ETL missions that it can form from the given raw materials
        :param ready_products:
        :return:  Sequence of ETL missions
        """
        pass


