import datetime
import string
from abc import abstractmethod
from typing import Sequence
from product import Product
from operator import Operator
from manager.principal import Principal
from operation import Operation


class SensorOperator(Operator):
    def __init__(self, name: string,
                 version_number: string,
                 version_description: string):
        super().__init__(name, version_number, version_description)

    @abstractmethod
    def discover(self, principal: Principal,
                 exists_already: Sequence[Product],
                 above_partition: string,
                 equal_or_below_partition: string,
                 end_time: datetime.datetime) -> Operation:
        pass
