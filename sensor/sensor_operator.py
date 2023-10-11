import datetime
from abc import ABC, abstractmethod
from typing import Sequence
from common.product import Product
from etl.operator_identity import OperatorIdentity
from etl.realm import Realm
from sensor.sensor_operation import SensorOperation


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
               start_time: datetime.datetime,
               end_time: datetime.datetime) -> SensorOperation:
        pass

