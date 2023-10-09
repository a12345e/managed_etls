import datetime
from abc import ABC, abstractmethod
import string
from typing import Sequence
from dataframe_wrapper import DataFrameWrapper
from product import Product
from etls.operator_identity import OperatorIdentity


class SensorOperator(ABC):
    def __init__(self, identity: OperatorIdentity):
        self._identity = identity
        pass

    @property
    def identity(self):
        return self._identity

    @abstractmethod
    def create(self,
               exists_already: Sequence[Product],
               start_time: datetime.datetime,
               end_time: datetime.datetime):
        pass

