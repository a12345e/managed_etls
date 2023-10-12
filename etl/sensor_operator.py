import datetime
import string
from abc import ABC, abstractmethod
from typing import Sequence
from common.product import Product
from etl.operator_identity import OperatorIdentity
from manager.realm import Realm
from etl.etl_operation import ETLOperation


class SensorOperator(ABC):
    def __init__(self, identity: OperatorIdentity):
        self._identity = identity
        pass

    @property
    def identity(self):
        return self._identity

    @abstractmethod
    def create(self, realm: Realm,
               exists_already: Sequence[Product],
               partitions: Sequence[string],
               end_time: datetime.datetime) -> ETLOperation:
        pass

